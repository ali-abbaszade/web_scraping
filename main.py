import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.truecar.com/used-cars-for-sale/listings/?page='

# Create csv file
csv_file = open('output.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['make', 'mileage', 'price'])

# Request to first five pages
for page in range(1, 6):
    res = requests.get(url + str(page))

# Check request status
    if not res.ok:
        print('server responsed: ', res.status_code)
    else:
        soup = BeautifulSoup(res.text, 'html.parser')

    all_cars = soup.find_all(
        'div', attrs={'class': 'card-content vehicle-card-body order-3'})

    # Extract data from html 
    for car in all_cars:
        make = car.find(
            'span', attrs={'class': 'vehicle-header-make-model text-truncate'}).text
        mileage = car.find(
            'div', attrs={'class': 'd-flex w-100 justify-content-between'}).text
        price = car.find(
            'div', attrs={'class': 'heading-3 margin-y-1 font-weight-bold'}).text

        # write to csv file
        csv_writer.writerow([make, mileage, price])


csv_file.close()
