import requests
from bs4 import BeautifulSoup
from queue import Queue
from threading import Thread

import os
from time import time

BASIC_DIR = 'img'
THREAD_DIR = 'thread_img'
NUM_THREADS = 4
QUANTITY_IMG = 10
q = Queue()
url = 'https://rozetka.com.ua/notebooks/c80004/'


def get_list_img(url, guantity_img):
    response = requests.get(url)
    response_content = response.content
    bs_obj = BeautifulSoup(response_content, features='html.parser')
    img_div = bs_obj.find_all('div', class_='goods-tile')
    list_images = []

    for div in img_div:
        images = div.find_all('img', class_='lazy_img_hover')
        for image in images:
            link = image.get('src')
            list_images.append(link)
            
    return list_images[:guantity_img]


def upload_img(url_img, dir_to_save):
    response = requests.get(url_img, stream=True)
    if not os.path.isdir(dir_to_save):
        os.mkdir(dir_to_save)
    filename = f"{dir_to_save}/{url_img.split('/')[-1]}"

    with open(filename, 'wb') as f:
        for block in response.iter_content(chunk_size=64):
            f.write(block)


def find_and_download_img_thread(q_for_thread, guantity_img, dir_to_save):
    while True:
        main_url_img = q_for_thread.get()
        list_url_images = get_list_img(main_url_img, guantity_img)
        for url_img in list_url_images:
            upload_img(url_img, dir_to_save)
        q.task_done()


if __name__ == "__main__":

    start_time = time()
    img_list = get_list_img(url, QUANTITY_IMG)
    for url_img in img_list:
        upload_img(url_img, BASIC_DIR)
        
    print(f"Basic uploading: {round((time() - start_time), 2)} seconds")
    

    start_time = time()
    q.put(url)
    for t in range(NUM_THREADS):
        worker = Thread(target=find_and_download_img_thread, args=(q, QUANTITY_IMG, THREAD_DIR))
        worker.daemon = True
        worker.start()
    q.join()

    print("Thread: %s seconds" % round((time() - start_time), 2))
    
