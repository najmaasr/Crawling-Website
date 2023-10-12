
import csv
from pymongo import MongoClient
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

#Crawling Data
hasil = []  # Daftar untuk data yang akan disimpan
x = 0

current_date = datetime.now().date()
formatted_date = current_date.strftime('%Y-%m-%d')
print("current date:", formatted_date)
yy, mm, dd = formatted_date.split('-')
         
def tempo():
  tanggal = str(yy)+"-"+str(mm)+"-"+str(dd)

  url = "https://www.tempo.co/indeks/"+tanggal
  html = urlopen(url)
  data = BeautifulSoup(html, 'html.parser')

  title = data.findAll("h2", {"class":"title"})
  date = data.findAll("h4", {"class":"date"})

  for x in range(0, len(title)):
    if x < 5 :
      row = [title[x].text.strip(), date[x].text.strip(), "Tempo"]
      hasil.append(row)

def cnn():
  tanggal = str(yy)+"/"+str(mm)+"/"+str(dd)
  url = "https://www.cnnindonesia.com/indeks/?date="+tanggal
  html = urlopen(url)
  data = BeautifulSoup(html, 'html.parser')

  title = data.findAll("h2", {"class":"text-cnn_black_light dark:text-white mb-2 inline leading-normal text-xl group-hover:text-cnn_red"})
  date = data.findAll("span", {"class":"text-xs text-cnn_black_light3"})

  for x in range(5, len(title)):
    if x < 10 and x >= 5 :
      row = [title[x].text.strip(), date[x].text.strip(), "CNN"]
      hasil.append(row)

tempo()
cnn()

#Insert Data to MongoDB
mongo = MongoClient('mongodb://mongodb:27017/')
db=mongo.tugas_bigdata

formatted_data = []

for row in hasil:
    formatted_data.append({
        "Judul Berita": row[0],
        "Tanggal Publish": row[1],
        "Sumber Berita": row[2]
    })

try:
    db.crawling.insert_many(formatted_data)
    print("Data inserted successfully.")
    
except Exception as e:
    print("Error:",e)