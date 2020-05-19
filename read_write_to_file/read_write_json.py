""" Small function that dumps and loads json file"""
import json
import os

def write_to_file(input_list):
    with open("json_write.json", "w") as json_write:
        json.dump(input_list, json_write)


def load_list_of_books():
    if not os.path.exists("json_write.json"):
        return []
    else:
        with open("json_write.json") as read_list_of_book:
            data = json.load(read_list_of_book)
            return data

if __name__ == "__main__":
    write_to_file({'author': 'Anne', 'read': False, 'title': 'The Gift'})

