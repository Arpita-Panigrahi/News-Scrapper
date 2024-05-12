import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

# URL of the article
url = 'https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/'

# Send an HTTP GET request to the URL
r = requests.get(url)

# Check if the request was successful (status code 200)
if r.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Extract and print the title of the article
    print("The title is", soup.title.string)
    
    # Find the author information within the appropriate HTML element
    author_tag = soup.find(rel="author")
    
    # Check if author information exists before trying to access it
    if author_tag:
        print("The author is", author_tag.get_text())
    else:
        print("Author information not found")
else:
    # Print an error message if the request was not successful
    print('Error', r.status_code)

