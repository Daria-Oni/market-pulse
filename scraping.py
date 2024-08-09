import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract page title
    title = soup.find('title').text if soup.find('title') else 'No title'
    
    # Find meta-tag with keywords, safely handling missing content
    keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
    if keywords_tag and 'content' in keywords_tag.attrs:
        keywords = keywords_tag['content']
    else:
        keywords = 'No keywords'
    
    return {'url': url, 'title': title, 'keywords': keywords}

# Assume CSV with URLs has been read into 'urls'
urls = [
'https://www.infosys.com/industries/aerospace-defense.html',
'https://www.infosys.com/industries/agriculture.html',
'https://www.infosys.com/industries/automotive.html',
'https://www.infosys.com/industries/chemical-manufacturing.html',
'https://www.infosys.com/industries/communication-services.html',
'https://www.infosys.com/industries/consumer-packaged-goods.html',
'https://www.infosys.com/industries/education.html',
'https://www.infosys.com/industries/engineering-procurement-construction.html',
'https://www.infosys.com/industries/financial-services.html',
'https://www.infosys.com/industries/healthcare.html',
'https://www.infosys.com/industries/high-technology.html',
'https://www.infosys.com/industries/industrial-manufacturing.html',
'https://www.infosys.com/industries/publishing.html',
'https://www.infosys.com/industries/insurance.html',
'https://www.infosys.com/industries/life-sciences.html',
'https://www.infosys.com/industries/logistics-distribution.html',
'https://www.infosys.com/industries/media-entertainment.html',
'https://www.infosys.com/industries/mining.html',
'https://www.infosys.com/industries/oil-and-gas.html',
'https://www.infosys.com/industries/private-equity.html',
'https://www.infosys.com/industries/professional-services.html',
'https://www.infosys.com/industries/public-sector.html',
'https://www.infosys.com/industries/retail.html',
'https://www.infosys.com/industries/travel-hospitality.html',
'https://www.infosys.com/industries/utilities.html',
'https://www.infosys.com/industries/waste-management.html',
'https://www.infosys.com/industries/#tennismenu',
'https://www.infosys.com/industries/aerospace-defense.html',
'https://www.infosys.com/industries/agriculture.html',
'https://www.infosys.com/industries/automotive.html',
'https://www.infosys.com/industries/chemical-manufacturing.html',
'https://www.infosys.com/industries/communication-services.html',
'https://www.infosys.com/industries/consumer-packaged-goods.html',
'https://www.infosys.com/industries/education.html',
'https://www.infosys.com/industries/engineering-procurement-construction.html'
]

data = [scrape_data(url) for url in urls]
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
