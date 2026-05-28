import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://quotes.toscrape.com/"

# Send request to website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("span", class_="text")

print("Quotes from Website:\n")

# Print quotes
for quote in quotes:
    print(quote.text)