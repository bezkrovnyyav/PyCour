"""
NoSQL Blog
Create the db to store your blog posts using Mongo.
In this task you need:
create the db, collection and documents
insert objects
retrieve all objects and object via filtering
update at least 1 object
delete at least 1 object
"""


from pymongo import MongoClient
from random import randint

import datetime
import pprint
import pyjokes
import names

DB_NAME = 'blog'
COLLECTION_NAME = 'jokes'
QUANTITY_JOKES = 3


def insert_jokes(db_name: str, collection_name: str, quantity_jokes: int) -> object:
    insert_data = []
    for i in range(quantity_jokes):
        joke = pyjokes.get_joke()
        created_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        temp_mess = {
            "id_post": i,
            "body": joke,
            "author": names.get_full_name(),
            "created_time": created_time
        }
        insert_data.append(temp_mess)
    return client[db_name][collection_name].insert_many(insert_data)


def get_all_jokes(db_name: str, collection_name: str) -> object:
    return client[db_name][collection_name].find()


def delete_database(db_name: str) -> str:
    client.drop_database(db_name)
    return 'Database is deleted'


def change_random_joke(db_name: str, collection_name: str) -> object:
    list_id_joke = client[db_name][collection_name].find({'body': {'$ne': 'CHANGED BODY'}}).distinct('_id')
    if list_id_joke:
        id_joke = list_id_joke[randint(0, len(list_id_joke) - 1)]
        return client[db_name][collection_name].update_one({'_id': id_joke},
                                                           {'$set': {'body': 'CHANGED BODY'}})


def delete_random_joke(db_name: str, collection_name: str) -> object:
    list_id_joke = client[db_name][collection_name].find().distinct('_id')
    if list_id_joke:
        id_joke = list_id_joke[randint(0, len(list_id_joke) - 1)]
        return client[db_name][collection_name].delete_one({'_id': id_joke})


if __name__ == "__main__":
    with MongoClient() as client:
        while True:
            menu = '''
Make your choice:

1) Create database
2) Delete database
3) Get all data
4) Change body of random joke
5) Delete random joke
6) Exit
'''
            choice = input(menu)
            if choice == '1':
                result = insert_jokes(DB_NAME, COLLECTION_NAME, QUANTITY_JOKES)
                print(result.acknowledged)
            elif choice == '2':
                print(delete_database(DB_NAME))
            elif choice == '3':
                temp = get_all_jokes(DB_NAME, COLLECTION_NAME)
                for i in temp:
                    pprint.pprint(i)
            elif choice == '4':
                result = change_random_joke(DB_NAME, COLLECTION_NAME)
                print(result.raw_result)
            elif choice == '5':
                result = delete_random_joke(DB_NAME, COLLECTION_NAME)
                print(result.acknowledged)
            elif choice == '6':
                break
