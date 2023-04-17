print("EXERCISE 5.1")

import os
import glob

def find_pdf_size(top):
    total_size = 0
    for root, dirs, files in os.walk(top):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
    return total_size
print(find_pdf_size("."))

print("EXERCISE 5.2")

import datetime

def print_working_days(date1, date2):
    date_format = 'YYYY-MM-DD'
    start_date = datetime.date.fromisoformat(date1)
    end_date = datetime.date.fromisoformat(date2)
    delta = datetime.timedelta(days=1)
    
    while start_date < end_date:
        if start_date.weekday() < 5:
            print(start_date.isoformat())
        start_date = start_date + delta

print_working_days('2023-04-01', '2023-05-02')

print("EXERCISE 5.3")

import random

def random_walk(start=0):
    position = start
    while True:
        yield position
        position += random.choice([-1, 1])

print("1D random walk")
for position in random_walk():
    print(position, end=' ')
    if abs(position) == 10:
        break
print()

print("the final position after 100 moves")

final_position = []
for i in range(10):
    walker = random_walk()
    for position in range(100):
        next(walker)
    final_position.append(next(walker))

print(final_position)
