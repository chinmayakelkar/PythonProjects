import csv
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

mech = Browser()
url = "https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s"
page = mech.open(url)
html = page.read()

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'collapse shadow BCSDTable'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
