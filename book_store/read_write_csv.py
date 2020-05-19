import csv

def write_to_csv(input_list):
    with open('file.csv', mode='w') as csv_file:
        write_to_scv = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_to_scv.writerow(["title", "author", "read"])
        for book in input_list:
            write_to_scv.writerow([book['title'], book['author'], book['read']])


#write_to_csv([{"title": "x", "author": "y", "read": False}, {"title": "c", "author": "d", "read": False}])


def read_from_csv():
    list_of_dict = []
    with open('file.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            list_of_dict.append(row)
        return list_of_dict

def cvs_reader():
    return_list = []
    with open('file.csv') as csv_file:
        file_read = csv.reader(csv_file)
        x = [line for line in file_read]
        HEADERS = x[0]
        for l in x[1:]:
            return_list.append(dict(zip(HEADERS, l)))
        return return_list
