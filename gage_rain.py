import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.ladpw.org/wrd/Precip/alert_rain/season_raindata.cfm?id=384"
response = requests.get(url)
code = response.content

soup = BeautifulSoup(code, "html.parser")
table = soup.find('table', attrs={"border" : "1"})

headers = [header.text for header in table.find_all('th')]
headers.append("id")
list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_cells.append(url[-3:])    
    list_of_rows.append(list_of_cells)

outfile = open("./rainfall.csv", "w")
writer = csv.writer(outfile, lineterminator ="\n")
writer.writerow(headers)
writer.writerows(list_of_rows)


