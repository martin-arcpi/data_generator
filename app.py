from random import randint, choice, shuffle
import csv

first_names = ['Jose', 'Kevin', 'Steven',
              'Richard', 'David', 'Christopher',
              'Brian', 'Joshua', 'Anthony', 'Daniel'
                'Cynthia', 'Karen', 'Christine',
                'Nancy', 'Maria', 'Betty',
                'Margaret', 'Ying', 'Linda', 'Michelle']


shuffle(first_names)

last_names = ['Ma', 'Das', 'Pham', 'Duong',
              'Hassan', 'Park', 'Miller', 'Petrov',
              'Mehta', 'Kumar', 'Zheng', 'Lim',
              'Pérez', 'Yadav', 'Sánchez', 'Joshi',
              'Kumar', 'He', 'Wilson', 'Yoon']

shuffle(last_names)

# TODO add age and dob column using timedeltas
customer_count = 10

credit_scores = [randint(400, 999) for score in range(0,10)]

with open('credit_scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['first_name', 'last_name', 'credit_score'])
    for i in range(customer_count):
        writer.writerow([choice(first_names), choice(last_names), choice(credit_scores)])
