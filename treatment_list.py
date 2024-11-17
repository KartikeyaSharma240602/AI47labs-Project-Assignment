import requests
from lxml import html
import json

# Function to scrape data based on XPath
def scrape_data(url, container_xpath, item_type):
    try:
        print(f"Scraping {item_type} from {url}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the page content with lxml
        tree = html.fromstring(response.content)
        container = tree.xpath(container_xpath)
        
        if not container:
            print(f"No container found for {item_type} using XPath: {container_xpath}")
            return []
        
        items = []
        
        # Assuming the container is a <ul> element, extract its <li> children
        for item in container[0].xpath(".//li"):
            anchor = item.xpath(".//a")  # Find <a> tags inside <li>
            if anchor:
                item_name = anchor[0].text.strip()  # Extract the name or title
                item_link = anchor[0].get("href").strip()  # Extract the link
                items.append({"Name": item_name, "Link": item_link})
        
        print(f"Scraped {len(items)} {item_type}.")
        return items
    
    except Exception as e:
        print(f"Error scraping {item_type} from {url}: {e}")
        return []

# Main scraping logic
if __name__ == "__main__":
    # URL to scrape
    hospital_url = "https://www.medanta.org/sitemap"
    
    # Define the XPath for the data
    container_xpath = '/html/body/main/section/div/div/div/div[4]/div[2]/ul'
    
    # Scrape data
    scraped_data = {}
    scraped_data['treatments'] = scrape_data(hospital_url, container_xpath, 'treatments')
    
    # Save all data to a JSON file
    with open("treatment_list.json", "w", encoding="utf-8") as json_file:
        json.dump(scraped_data, json_file, indent=4, ensure_ascii=False)
    
    print("Scraping completed. Data saved to treatment_list.json.")
