import csv
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

mech = Browser()
url = "http://www.imdb.com/chart/top"
page = mech.open(url)   
html = page.read()

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'chart full-width'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('th'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./imdbtop250list.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
