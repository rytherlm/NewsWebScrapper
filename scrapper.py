import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://techxplore.com/news/2023-06-problems.html"

# Send a GET request and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Create BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the desired elements and extract data
stories = soup.find_all('article')

# Create a list to store the extracted data
data = []

for story in stories:
    title_element = story.find('h3', class_='article__title')
    if title_element:
        title = title_element.text.strip()
        url_element = title_element.find('a')
        if url_element:
            url = url_element['href']
            data.append({"Title": title, "URL": url})

# Print the extracted data
for item in data:
    print(f"Title: {item['Title']}\nURL: {item['URL']}\n")

# Save the extracted data to a file
filename = "hacker_news_data.txt"

with open(filename, "w") as file:
    for item in data:
        file.write(f"Title: {item['Title']}\nURL: {item['URL']}\n")

print(f"Data saved to {filename}")
