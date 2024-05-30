#!/bin/usr/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            json_data = json.dumps([row for row in csv_reader])
            with open('data.json', 'w') as jsonfile:
                jsonfile.write(json_data)
        return True
    except FileNotFoundError:
        print("File not found.")
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")