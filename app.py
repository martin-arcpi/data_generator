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

num_of_customers = 10

credit_scores = [randint(400, 999) for score in range(0,10)]

with open('credit_scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['first_name', 'last_name', 'credit_score'])
    for i in range(num_of_customers):
        writer.writerow([choice(first_names), choice(last_names), choice(credit_scores)])
