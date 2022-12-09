import os
from time import time

import requests
from bs4 import BeautifulSoup
from aiohttp import ClientSession

import asyncio
from queue import Queue
from threading import Thread


BASIC_DIR = 'img'
THREAD_DIR = 'thread_img'
AS_PART = 'async_img'
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


async def get_list_img_async(url_site, guantity_img):
    async with ClientSession() as session:
        response = await session.get(url=url_site)
        bs_obj = BeautifulSoup((await response.read()), features='html.parser')
        img_div = bs_obj.find_all('div', class_='goods-tile')
        list_images = []

        for div in img_div:
            images = div.find_all('img', class_='lazy_img_hover')
            for image in images:
                link = image.get('src')
                list_images.append(link)
            
        return list_images[:guantity_img]


async def upload_img_async(url_img, dir_to_save):
    async with ClientSession() as session:
        response = await session.get(url=url_img)
        if not os.path.isdir(dir_to_save):
            os.mkdir(dir_to_save)
        filename = f"{dir_to_save}/{url_img.split('/')[-1]}"

        with open(filename, 'wb') as f:
            f.write(await response.read())


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
    
    
    start_time = time()
    loop = asyncio.get_event_loop()
    tasks = []
    tasks.append(loop.create_task(get_list_img_async(url, QUANTITY_IMG)))
    group = asyncio.gather(*tasks)
    results = loop.run_until_complete(group)

    tasks = []
    for result in results:
        for url_img in result:
            tasks.append(loop.create_task(upload_img_async(url_img, AS_PART)))
    group = asyncio.gather(*tasks)
    loop.run_until_complete(group)
    print("As IO: %s seconds" % round((time() - start_time), 2)) 
