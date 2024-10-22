import setup
import random
import csv

def generate_random_identity():
    row_count = 0
        
    with open(setup.creds_file_path, 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)

    row = [None, None, None]
    random_number = random.randint(0, row_count - 1)
    with open(setup.creds_file_path, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == random_number:
                row = row
                break

    return row