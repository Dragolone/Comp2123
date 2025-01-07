import requests
from bs4 import BeautifulSoup

# url = "https://github.com/Dragolone"
url = ("https://github.com/Dragolone/INFO1113-Java-/tree/main/InkballGame")

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print(f"Successfully accessed {url}")

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the title of the webpage
    title = soup.title.string if soup.title else "No Title"
    print(f"Webpage Title: {title}")

    # Find and print all links on the webpage
    print("All links on the webpage:")
    links = soup.find_all('a')  # Find all <a> tags
    for link in links:
        href = link.get('href')  # Extract the href attribute
        if href:
            print(href)
else:
    print(f"Failed to access the page. Status code: {response.status_code}")
