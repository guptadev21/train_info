import requests
from bs4 import BeautifulSoup
import re
import json

# get pnr number for user
pnr_no = input('Please enter pnr number: ')


# Specify the URL you want to scrape
url = 'https://www.confirmtkt.com/pnr-status/' + str(pnr_no)


# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the script tag containing the variable 'data'
    script_tags = soup.find('script', string=re.compile('data = {'))

    data_match = re.search(r'data = ({.*?});', response.text, re.DOTALL)
    if data_match:
        # Extract the JSON part of the match
        data_content = data_match.group(1)

        # Parse the JSON content
        data_json = json.loads(data_content)

    # with open('data.html', 'w', encoding='utf-8') as file:
    #     file.write(str(data_json))


    train_number = data_json['TrainNo']
    train_name = data_json['TrainName']

    # Print the results
    print("Train Number:", train_number)
    print("Train Name:", train_name)
    print("Date of Journey:", data_json['Doj'])
    print("From:", data_json['From'], 'To:', data_json['To'])
    print("Boarding Station:", data_json['BoardingStationName'])
    passenger_status = data_json['PassengerStatus'][0]
    print("Status:", passenger_status)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
