from pathlib import Path
import uuid
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

url = '-----------------------------------------'

output_folder = Path('new_directory')
output_folder.mkdir(exist_ok=True)

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=options, executable_path='path/chromedriver.exe')
driver.get(url)

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

images = []

for img in soup.find_all("img"):
    images.append(img.get('src'))

for target in images:
        re = requests.get(target)
        with open('new_directory/{}.png'.format(str(uuid.uuid4())), 'wb') as f:
            f.write(re.content)