from random import randint, choice, shuffle
import csv

first_names = ['Jose', 'Kevin', 'Steven',
              'Richard', 'David', 'Christopher',
              'Brian', 'Joshua', 'Anthony', 'Daniel'
                'Cynthia', 'Karen', 'Christine',
                'Nancy', 'Maria', 'Betty',
                'Margaret', 'Ying', 'Linda', 'Michelle']



last_names = ['Ma', 'Das', 'Pham', 'Duong',
              'Hassan', 'Park', 'Miller', 'Petrov',
              'Mehta', 'Kumar', 'Zheng', 'Lim',
              'Pérez', 'Yadav', 'Sánchez', 'Joshi',
              'Kumar', 'He', 'Wilson', 'Yoon']

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['first_name', 'last_name',])
    for i in range(10):
        writer.writerow([choice(first_names), choice(last_names)])
