from bs4 import BeautifulSoup
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Aktivasi selenium
opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)
poco_link = 'https://shopee.co.id/search?keyword=poco&page=0'

driver.get(poco_link)
driver.set_window_size(1300, 800)

# Untuk Loading Scroll (pixel)
rentang = 500
for i in range(1, 8):  # 7 kali scroll agar bisa sampai halaman paling bawah
    akhir = rentang * i
    scroll = "window.scrollTo(0,"+str(akhir)+")"
    driver.execute_script(scroll)
    time.sleep(1)
time.sleep(5)

driver.save_screenshot(
    'D:\Coba code\Coba python\Web Scrapping\Shopee\home.png')
content = driver.page_source
driver.quit()

# Parsing
data = BeautifulSoup(content, 'html.parser')
# print(data.encode('utf-8'))

list_nama, list_gambar, list_harga, list_link, list_terjual, list_kota = [], [], [], [], [], []
# /Menentukan area
i = 1
base_url = 'https://shopee.co.id'
for area in data.find_all('div', class_='col-xs-2-4 shopee-search-item-result__item'):
    print(i)
    # Cari nama barang
    nama = area.find('div', class_='ie3A+n bM+7UW Cve6sh').get_text()
    gambar = area.find('img')['src']
    harga = area.find('div', class_='vioxXd rVLWG6').get_text()
    link_barang = base_url + area.find('a')['href']

    terjual = area.find('div', class_='r6HknA uEPGHT')
    if terjual != None:
        terjual = terjual.get_text()

    kota = area.find('div', class_='zGGwiV').get_text()

    list_nama.append(nama)
    list_gambar.append(gambar)
    list_harga.append(harga)
    list_link.append(link_barang)
    list_terjual.append(terjual)
    list_kota.append(kota)
    i += 1
    print('--------------------------------')

df = pd.DataFrame({'Nama': list_nama, 'Gambar': list_gambar, 'Harga': list_harga,
                  'Terjual': list_terjual, 'Kota': list_kota, 'Link': list_link})
df.head()
writer = pd.ExcelWriter(
    'D:\Coba code\Coba python\Web Scrapping\Shopee\Poco.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
