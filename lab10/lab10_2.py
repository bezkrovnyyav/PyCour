import os
from time import time

from random import choice
from string import ascii_letters

from multiprocessing import Process
from multiprocessing import Queue


CPU_CORES = os.cpu_count()
SYMBOL = choice(ascii_letters)
Q = Queue()
LEN_STRING = 2000000


def record_symbols(file_name, symbol, len_string):
    symbol_string = ""
    for i in range(len_string):
        symbol_string += symbol
    with open(file_name, 'w') as f:
        f.write(symbol_string)


def record_symbols_multiprocessing(processing_file_name, symbol, len_string):
    while not processing_file_name.empty():
        record_symbols(processing_file_name.get(), symbol, len_string)


if __name__ == "__main__":
    print(f'number CPU: {CPU_CORES}')

    start_time = time()
    for file_num in range(CPU_CORES):
        record_symbols(f'files/file_{file_num}.txt', SYMBOL, LEN_STRING)
    print(f"Basic recording: {round((time() - start_time), 2)} seconds")

    start_time = time()
    list_processing = []
    for file_num in range(CPU_CORES):
        Q.put(f'files_processing/file_{file_num}.txt')

    for p in range(CPU_CORES):
        process = Process(target=record_symbols_multiprocessing, args=(Q, SYMBOL, LEN_STRING,))
        list_processing.append(process)
        process.start()

    for p in list_processing:
        p.join()
    print(f"Processing recording: {round((time() - start_time), 2)} seconds")
