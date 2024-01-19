from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://moringaschool.com/courses/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')

for course in doc.select("a.block"):
    print(course.contents[0].strip())