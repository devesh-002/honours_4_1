import requests
from bs4 import BeautifulSoup
import pandas as pd
# URL of the website containing the table
list_=[]
for i in range(1, 23):
    url = 'https://www.census2011.co.in/district.php?page='+str(i)

    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table by inspecting the HTML structure or using its class or ID
    table = soup.find('table', class_='table-striped')  # Replace 'table-class' with the actual class name of the table

    # Extract data from the table
    if table:
        # Assuming the table contains rows and columns
        rows = table.find_all('tr')  # Find all table rows

        for row in rows:
            # Extract data from each row
            columns = row.find_all('td')  # Find all table cells in each row
            row_data = [col.text.strip() for col in columns]
            print(row_data)  # Do something with the extracted data, like printing or storing it
            if(row_data!=[]):
                list_.append(row_data)
    else:
        print("Table not found on the page.")
df = pd.DataFrame(list_, columns=["Sno", "District","State","Population","Growth","SR","Literacy"])

df.to_csv('literacy.csv', index=False, encoding='utf-8',sep='|')
