import requests

url = "https://kidkodschool.github.io/welcome.html"
response = requests.get(url)

with open("Welcome .html", "wb") as file:
    file.write(response.content)