from random import randint, choice, shuffle
import csv
from datetime import date

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
customer_count = 100

credit_scores = [randint(400, 999) for score in range(0,10)]

birth_dates = []
for i in range(customer_count):
    birth_dates.append(date(randint(1937, 2005), randint(1, 12), randint(1, 30)))

employment_status = ['Employed', 'Self-Employed', 'Unemployed', 'Student']

# cities = [
#     "Tokyo", "New York", "Shanghai", "São Paulo", "Mumbai", 
#     "Beijing", "London", "Los Angeles", "Paris", "Mexico City",
#     "Barcelona", "Vancouver", "Munich", "Cape Town", "Kuala Lumpur", 
#     "Bogotá", "Hanoi", "Stockholm", "Milan", "Jakarta",
#     "Bruges", "Innsbruck", "Santorini", "Ushuaia", "Queenstown", 
#     "Reykjavik", "Luang Prabang", "Bergen", "Siem Reap", "Zermatt"
# ]
# shuffle(cities)


countries = [
    "China", "India", "United States", "Indonesia", "Pakistan",
    "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico",
    "Canada", "Australia", "Argentina", "South Korea", "Spain",
    "Poland", "Saudi Arabia", "Netherlands", "Thailand", "Turkey",
    "Iceland", "Luxembourg", "Malta", "Fiji", "Bhutan",
    "Monaco", "Liechtenstein", "San Marino", "Andorra", "Seychelles"
]
shuffle(countries)

with open('credit_scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'first_name', 'last_name',
                     'credit_score', 'birth_date', 'employment_status',
                     'country'])
    for i in range(customer_count):
        writer.writerow([i+1, choice(first_names), choice(last_names),
                              choice(credit_scores), choice(birth_dates),
                              choice(employment_status),
                              choice(countries)])


