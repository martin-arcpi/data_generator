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


customer_count = 100

credit_scores = [randint(400, 999) for score in range(0,10)]


# TODO Fix value error that occurs to cause out of range for month
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
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", 
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", 
    "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", 
    "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", 
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", 
    "Congo (Democratic Republic of the Congo)", "Costa Rica", "Croatia", "Cuba", 
    "Cyprus", "Czechia (Czech Republic)", "Denmark", "Djibouti", "Dominica", "Dominican Republic", 
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", 
    "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", 
    "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", 
    "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", 
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", 
    "Korea (North)", "Korea (South)", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", 
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", 
    "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", 
    "Morocco", "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", 
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", 
    "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", 
    "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", 
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", 
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", 
    "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", 
    "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", 
    "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", 
    "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", 
    "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", 
    "Yemen", "Zambia", "Zimbabwe"
]



shuffle(countries)

with open('credit_scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'first_name', 'last_name',
                     'credit_score', 'birth_date', 'employment_status',
                     'country', 'annual_salary', 'mobile_number'])
    for i in range(customer_count):
        writer.writerow([i+1, choice(first_names), choice(last_names),
                              choice(credit_scores), choice(birth_dates),
                              choice(employment_status),
                              choice(countries), round(randint(10000, 500000)),
                              f'+555-{randint(100, 999)}-{randint(100, 999)}-{randint(100, 999)}'])
