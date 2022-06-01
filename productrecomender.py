from itertools import combinations
import csv

IN_DATA = "./browsing-data.txt"
OUT_DATA = "./output.txt"
SUPPORT = 100


def read_data(file_name):
    record = []
    with open(file_name) as input_file:
        lines = csv.reader(input_file, " ")
        for row in lines:
            record.append(row[:-1])
        return record
