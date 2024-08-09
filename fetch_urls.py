import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

# Function to get all links from a page
def get_all_links(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for anchor in soup.find_all('a', href=True):
        link = anchor['href']
        # Normalize URLs
        full_url = urljoin(base_url, link)
        if 'industries' in full_url:
            links.append(full_url)
    return links

# Function to check if a URL is valid
def is_valid_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

# URL of the Infosys Industries page
base_url = "https://www.infosys.com/industries/"
all_links = get_all_links(base_url)

# Filter out links that are not relevant (e.g., social media, general pages)
relevant_links = [link for link in all_links if '/industries/' in link and not any(x in link for x in ['facebook', 'twitter', 'linkedin', 'youtube', 'careers', 'contact', 'about', 'newsroom'])]

# Prepare data for CSV
data_to_csv = []

# Check each URL and add to CSV data
for link in relevant_links:
    status = is_valid_url(link)
    data_to_csv.append([link, status])

# Save data to CSV
with open('links_status.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['url', 'Status'])
    writer.writerows(data_to_csv)

print("Data has been written to CSV file.")

