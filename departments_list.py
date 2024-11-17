from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time

# Function to scrape links after clicking "Load More"
def scrape_links_with_load_more(url, class_name, load_more_button_selector):
    try:
        # Set up Selenium WebDriver
        driver = webdriver.Chrome()
        driver.get(url)

        # Wait for the page to load
        wait = WebDriverWait(driver, 10)

        # Continuously click the "Load More" button
        #driver.find_element_by_xpath("/html/body/section/div/div/div[4]/button").click()
        while True:
            try:
                # Scroll to the bottom to ensure the button is in view
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)  # Give time for scrolling

                # Check if the button exists
                load_more_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/div[4]/button')))
                if load_more_button.is_displayed():
                    print("Clicking 'Load More' button...")
                    ActionChains(driver).move_to_element(load_more_button).click(load_more_button).perform()
                    time.sleep(2)  # Allow time for new content to load
                else:
                    print("'Load More' button is not visible.")
                    break

            except Exception as e:
                print("No more 'Load More' buttons to click or an error occurred:", e)
                break

        # Parse the final page content with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        # Find all div elements with the given class name
        div_elements = soup.find_all("div", class_=class_name)

        # Extract name and links
        links = []
        for div in div_elements:
            anchor = div.find("a")  # Find the <a> tag inside the div
            if anchor and anchor.has_attr("href"):
                name = anchor.text.strip() if anchor.text else "Unnamed"
                href = anchor["href"].strip()
                links.append({"Name": name, "Link": href})

        print(f"Scraped {len(links)} links successfully.")
        return links

    except Exception as e:
        print(f"Error scraping links: {e}")
        return []

# Main function
if __name__ == "__main__":
    # URL of the webpage to scrape
    url = "https://www.medanta.org/hospitals-near-me/gurugram-hospital/speciality/"  # Replace with the actual URL

    # Class name to locate the divs containing the links
    target_class_name = "speciality-title font700"

    # CSS selector for the "Load More" button
    load_more_button_selector = "button.theme-button"  # Replace if different

    # Scrape links
    scraped_links = scrape_links_with_load_more(url, target_class_name, load_more_button_selector)

    # Save the links to a JSON file
    if scraped_links:
        try:
            with open("department_list.json", "w", encoding="utf-8") as file:
                json.dump(scraped_links, file, indent=4, ensure_ascii=False)
            print("Links saved to 'scraped_specialities.json'.")
        except Exception as e:
            print(f"Error saving to JSON file: {e}")
    else:
        print("No links to save.")
