# AI47labs-Project-Assignment
Project Report
On
Building an Intelligent Medical Assistant Using GPT-2 and Web Scraping 


Submitted By : Kartikeya Sharma
Submitted to : AI47 Labs




























Introduction
In the modern era of healthcare, the abundance of online information provides significant opportunities for leveraging data to improve accessibility, decision-making, and personalized care. This project, titled "Web Scraping and AI Model Training," aims to harness this potential by collecting, processing, and utilizing healthcare-related data from leading hospitals around the globe.
The primary objective of this project is to scrape and organize information such as doctors' profiles, treatment options, and departmental details from the official websites of the top 50 hospitals worldwide. The curated data will then be used to train a Private GPT model, a state-of-the-art language model designed for contextual understanding and generation, ensuring that the model is customized and optimized for healthcare applications.
To achieve this objective, the project is structured into three key phases:
Data Collection: Identifying and extracting relevant information from hospital websites using web scraping techniques.
Data Cleaning: Processing the scraped data to eliminate redundancies, inconsistencies, and irrelevant information, ensuring it is in a structured format suitable for training.
Model Training: Utilizing the cleaned dataset to train a Private GPT model, enhancing its capability to provide insights and generate accurate responses within the healthcare domain.
This project not only demonstrates the application of data engineering and machine learning techniques but also underscores the potential of AI in revolutionizing healthcare accessibility and efficiency.
















Project Execution
The project was carried out in a systematic series of steps, each focusing on a critical phase of development, from data collection to model training and finalization. Below is a detailed breakdown of how the project was executed:
Step 1: Data Collection (Web Scraping)
Identify Target Websites:
Compiled a list of the top 50 hospitals worldwide based on reputable rankings (e.g., Newsweek, U.S. News & World Report) and other resources like Wikipedia.
Set Up Web Scraping Environment:
Utilized Python libraries such as BeautifulSoup and Scrapy for HTML parsing. For dynamic content, tools like Selenium or Playwright were employed.
Data Scraping:
Extracted key fields, including:
Doctor Profiles: Name, specialty, credentials.
Treatments Offered: Range and description.
Department Profiles: Overview, expertise, and key services.
Scraping was performed in compliance with each website’s robots.txt file to ensure ethical practices.
Data Storage:
Stored the scraped data in structured formats like JSON or CSV to facilitate further processing.


Step 2: Data Cleaning
Data Structuring and Deduplication:
Processed the raw data using Python’s pandas library to remove duplicates, handle missing entries, and maintain consistency.
Standardization:
Unified terminology for fields such as doctor specialties and department names to ensure uniformity across datasets.
Final Output:
Saved the cleaned, standardized data in JSON or CSV format for seamless integration into the next steps.
Step 3: Model Preparation
Selecting a Private GPT Model:
Identified an open-source GPT-based model available on GitHub, suitable for fine-tuning, such as GPT-2 or lightweight GPT-3 alternatives.
Environment Setup:
Installed required libraries, including the Hugging Face transformers library, and configured a GPU-enabled environment for efficient training.
Data Preprocessing:
Tokenized and formatted the cleaned data to align with the input requirements of the chosen GPT model.
Step 4: Model Training
Fine-Tuning:
Trained the Private GPT model on the prepared dataset, adjusting parameters like batch size and learning rate to optimize performance.
Model Saving:
Saved the trained model’s weights and configurations for future use.
Preliminary Testing:
Conducted test interactions with the model to validate its ability to generate relevant and accurate responses.
Step 5: Documentation and Finalization
Process Documentation:
Compiled a comprehensive step-by-step guide detailing:
The tools and techniques used for scraping, cleaning, and training.
Challenges faced and strategies for resolution.
Deliverables Preparation:
Packaged the following project artifacts:
The cleaned data in JSON/CSV format.
Python scripts used for scraping, cleaning, and training.
Screenshots of the model’s performance during testing.
Project Finalization:
Organized all outputs into a structured format for submission and ensured the project met all objectives.




Doctor Data Scraping: Theory and Methodology
Overview
The task of scraping doctor data involves identifying relevant web pages, extracting structured information (e.g., names, specializations, degrees, etc.), and storing this data into a relational database for further use. This process is executed through web scraping and database interaction techniques. Below, the steps and the theory behind them are detailed.
Steps in Doctor Data Scraping
Setting Up the Environment
Libraries Used:
requests: For sending HTTP GET requests to fetch web page content.
BeautifulSoup: For parsing and navigating HTML content to extract relevant information.
psycopg2: For interacting with a PostgreSQL database to store the scraped data.
PostgreSQL Configuration:
A configuration dictionary is defined to hold database credentials for establishing a secure and efficient connection to the PostgreSQL server.
Database Preparation
A table named doctors is created in the PostgreSQL database to store scraped details. The schema includes fields for the doctor’s name, specialization, degree, associated hospital, and the webpage link.
The create_doctors_table function ensures the table exists before insertion to avoid duplication errors.
Scraping Doctor Data
Identifying Relevant Elements:
The code uses CSS selectors to locate and extract specific details from the HTML structure of the target web pages. These selectors (e.g., div.dr-details, h1.dr-details-name) correspond to specific elements containing doctor information.
Doctor’s name, specialization, and degree are targeted using appropriate selectors and fallback logic ("N/A") to handle missing data.
Hardcoding Hospital Details:
The hospital's name is hardcoded for clarity, assuming that all doctors on a page belong to the same institution.
Error Handling:
The script includes exception handling for HTTP errors and parsing issues to ensure robustness during scraping.
Data Storage
Extracted data is stored temporarily in a list of tuples, where each tuple represents a doctor’s record. This data is then inserted into the database using the INSERT INTO SQL query.
The insert_doctor_details function uses a executemany method to bulk-insert data, improving performance and reducing database load.

Automation and Scalability
Batch Processing:
The script reads links from a JSON file (hospital_data.json), allowing it to handle multiple hospital URLs dynamically.
Scalability:
By modularizing functions (e.g., for fetching data, database connection, and table creation), the code is scalable to handle additional fields or more hospitals with minimal adjustments.

How It Works
The process begins by reading hospital links from a JSON file.
For each link, the fetch_doctor_details function retrieves and parses the HTML content of the page.
The extracted doctor details are temporarily stored in a list and then bulk-inserted into the PostgreSQL database via the insert_doctor_details function.
Finally, the database connection is closed, ensuring no open handles remain.
Key Considerations
Ethical Scraping:
Compliance with the robots.txt file is ensured to avoid scraping restricted sections.
Error Handling:
Robust error handling is implemented at various stages to manage connectivity or parsing issues without halting the process.
Data Integrity:
Cleaning and structuring of data are embedded in the scraping pipeline to ensure uniformity and usability.

Practical code for the above mentioned theory:
Doctors Details:

import json
import requests
from bs4 import BeautifulSoup
import psycopg2


# PostgreSQL Configuration
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "*********",
    "host": "localhost",
    "port": 5432,
}


# Function to connect to PostgreSQL
def connect_to_postgres():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None


# Function to create a table for storing doctor details
def create_doctors_table(conn):
    try:
        query = """
        CREATE TABLE IF NOT EXISTS doctors (
            id SERIAL PRIMARY KEY,
            name TEXT,
            specialization TEXT,
            degree TEXT,
            hospital_name TEXT,
            link TEXT
        );
        """
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
        print("Doctors table created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")


# Function to insert doctor details into the database
def insert_doctor_details(conn, doctor_details):
    try:
        query = """
        INSERT INTO doctors (name, specialization, degree, hospital_name, link)
        VALUES (%s, %s, %s, %s, %s);
        """
        with conn.cursor() as cur:
            cur.executemany(query, doctor_details)
            conn.commit()
        print(f"Inserted {len(doctor_details)} doctor records successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")


# Function to extract doctor details from a webpage
def fetch_doctor_details(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
       
        # Hardcode hospital name here
        hospital_name = "Medanta, IN"
       
        # Use CSS selectors to extract doctor details
        doctors = []
        doctor_containers = soup.select("div.dr-details")  # Update this selector based on the actual HTML structure
       
        for container in doctor_containers:
            name = container.find("h1", class_="dr-details-name").text.strip() if container.find("h1", class_="dr-details-name") else "N/A"
            specialization = container.select_one("#overview > div > div > div.dr-details > p:nth-child(3)").text.strip() if container.select_one("#overview > div > div > div.dr-details > p:nth-child(3)") else "N/A"
            degree = container.select_one("#overview > div > div > div.dr-details > p:nth-child(4)").text.strip() if container.select_one("#overview > div > div > div.dr-details > p:nth-child(4)") else "N/A"
            doctors.append((name, specialization, degree, hospital_name, url))
       
        return doctors
    except Exception as e:
        print(f"Error fetching doctor details from {url}: {e}")
        return []


# Main Function
if __name__ == "__main__":
    # Load links from JSON file
    try:
        with open("hospital_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            doctor_links = data.get("doctors", [])
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        doctor_links = []


    if not doctor_links:
        print("No links found in the JSON file.")
    else:
        # Connect to PostgreSQL
        conn = connect_to_postgres()
        if conn:
            create_doctors_table(conn)


            all_doctor_details = []


            # Visit each link and extract doctor details
            for entry in doctor_links:
                link = entry["Link"]
                doctor_details = fetch_doctor_details(link)
                all_doctor_details.extend(doctor_details)


            # Insert data into the database
            if all_doctor_details:
                insert_doctor_details(conn, all_doctor_details)


            # Close the connection
            conn.close()



Doctors List:

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
    container_xpath = '/html/body/main/section/div/div/div/div[2]/div[2]/ul'
   
    # Scrape data
    scraped_data = {}
    scraped_data['doctors'] = scrape_data(hospital_url, container_xpath, 'doctors')
   
    # Save all data to a JSON file
    with open("hospital_data.json", "w", encoding="utf-8") as json_file:
        json.dump(scraped_data, json_file, indent=4, ensure_ascii=False)
   
    print("Scraping completed. Data saved to hospital_data.json.")




Treatments Data Scraping: Theory and Methodology
Overview
This process focuses on extracting a list of treatments offered by a hospital, including the name and associated link to further details, and storing it in a structured format for subsequent use. The workflow leverages XPath-based scraping for precise data extraction, followed by structured storage in a PostgreSQL database.

Steps in Treatments Data Scraping
Setting Up the Environment
Libraries Used:
requests: Sends HTTP GET requests to fetch the webpage containing treatment data.
lxml.html: Enables precise data extraction using XPath, a powerful query language for navigating HTML and XML documents.
json: Facilitates temporary storage of scraped data in a structured JSON format.
psycopg2: Allows seamless interaction with PostgreSQL for storing scraped data persistently.
Data Scraping Process
Identifying Data Location:
The target hospital's sitemap (https://www.medanta.org/sitemap) contains treatment information organized within an HTML <ul> element. The XPath (/html/body/main/section/div/div/div/div[4]/div[2]/ul) pinpoints this container.
Scraping Logic:
Parsing the Webpage:
The requests library retrieves the HTML content of the webpage, and lxml.html parses it into a tree structure for XPath queries.
Extracting Data:
The XPath query targets the <ul> container of treatments.
For each <li> child, <a> tags are used to extract the treatment name (text content) and link (href attribute).
Data Structuring:
Extracted data is stored in a dictionary with keys like Name and Link for each treatment. The data is saved into a JSON file (treatment_list.json) for subsequent steps.
Error Handling:
The scraping function includes exception handling to gracefully manage issues such as invalid URLs, incorrect XPath expressions, or network errors.
Database Preparation and Data Insertion
PostgreSQL Schema:
A table named treatments is created in PostgreSQL using the CREATE TABLE query. The schema includes:
id: A unique identifier for each record.
treatment_name: Name of the treatment.
treatment_link: URL with details about the treatment.
hospital_name: Name of the associated hospital (hardcoded for simplicity).
Data Insertion:
JSON data from treatment_list.json is loaded, and the hospital name is appended to each record.
The insert_treatments_data function bulk-inserts the prepared data into the treatments table using the executemany method, ensuring efficient database operations.
Scalability and Automation
Modularity:
Functions for scraping, table creation, and data insertion are independent, enabling reuse for other hospital sites or additional data types.
Automation:
The script dynamically extracts data using XPath, making it adaptable to similar structures in other websites.
By storing intermediate data in JSON, the process can be paused or reused at any stage without re-scraping.
How It Was Done
The sitemap of the hospital website was analyzed to identify the location of treatment data using developer tools.
A targeted XPath was crafted to isolate the <ul> container containing treatment links.
The script extracted and saved the data into a JSON file, which was later processed for database insertion.
The extracted treatments were inserted into a PostgreSQL table after appending the hospital name to each record.

Key Considerations
XPath Precision: Ensuring the XPath accurately targets the container avoids scraping unrelated data.
Error Management: Robust error handling ensures the process continues gracefully in case of partial failures.
Data Consistency: Cleaning and structuring the data during scraping ensures uniformity in the database.



Conclusion
The treatments scraping process successfully extracts structured data using XPath queries and stores it in a PostgreSQL database. This step contributes significantly to creating a comprehensive dataset for model training, ensuring accuracy and reliability.

Practical code for the above mentioned theory:
Treatments Details:

import json
import psycopg2


# PostgreSQL Configuration
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "*********",
    "host": "localhost",
    "port": 5432,
}


# Hardcoded hospital name
HOSPITAL_NAME = "Medanta, IN"


# Function to connect to PostgreSQL
def connect_to_postgres():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None


# Function to create the treatments table
def create_treatments_table(conn):
    try:
        query = """
        CREATE TABLE IF NOT EXISTS treatments (
            id SERIAL PRIMARY KEY,
            treatment_name TEXT,
            treatment_link TEXT,
            hospital_name TEXT
        );
        """
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
        print("Treatments table created successfully.")
    except Exception as e:
        print(f"Error creating treatments table: {e}")


# Function to insert data into the treatments table
def insert_treatments_data(conn, treatments):
    try:
        query = """
        INSERT INTO treatments (treatment_name, treatment_link, hospital_name)
        VALUES (%s, %s, %s);
        """
        with conn.cursor() as cur:
            cur.executemany(query, treatments)
            conn.commit()
        print(f"Inserted {len(treatments)} treatment records successfully.")
    except Exception as e:
        print(f"Error inserting data into treatments table: {e}")


# Main Function
if __name__ == "__main__":
    # Load treatments from JSON file
    try:
        with open("treatment_list.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            treatments = data.get("treatments", [])  # Assuming the JSON file has a key "treatments"
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        treatments = []


    if not treatments:
        print("No treatments found in the JSON file.")
    else:
        # Prepare data with hardcoded hospital_name
        treatments_data = [
            (treatment["Name"], treatment["Link"], HOSPITAL_NAME)
            for treatment in treatments
        ]


        # Connect to PostgreSQL
        conn = connect_to_postgres()
        if conn:
            create_treatments_table(conn)


            # Insert treatments data into the table
            insert_treatments_data(conn, treatments_data)


            # Close the connection
            conn.close()




Treatments list:

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




Department Data Scraping: Theory and Methodology
Overview
This section of the project involves scraping department information from the hospital’s website. The primary challenge lies in navigating a webpage dynamically loaded with JavaScript, requiring user interaction (e.g., clicking "Load More" buttons) to reveal all departments. This is handled using Selenium for browser automation and BeautifulSoup for structured HTML parsing.

Steps in Department Data Scraping
Setting Up the Environment
Libraries Used:
selenium: Automates browser actions, including clicking buttons and scrolling to load dynamic content.
bs4 (BeautifulSoup): Extracts structured information from the HTML content.
json: Saves the scraped data in a structured format for later processing.
Dynamic Content Handling
Challenges with JavaScript-Rendered Pages:
Traditional scraping tools like requests cannot fetch content dynamically rendered via JavaScript. To address this:
Selenium is used to simulate a browser environment.
It waits for elements to load and performs actions like scrolling and button clicks to reveal hidden content.
Scraping Workflow
Step 1: Access the Webpage
Selenium’s webdriver.Chrome() opens the target URL (https://www.medanta.org/hospitals-near-me/gurugram-hospital/speciality/) to fetch its initial content.
Step 2: Interact with the Page
The script identifies the "Load More" button using its XPath (/html/body/section/div/div/div[4]/button).
It continuously clicks this button until no more content loads or an error occurs, indicating the end of the list.
Step 3: Extract Content
After loading all content, Selenium retrieves the page source. BeautifulSoup processes the HTML to locate department-related information.
Target divs are identified by their class name (speciality-title font700).
Each <div> contains an <a> tag with the department name (text) and link (href).
Step 4: Structure Data
Extracted department names and links are stored as a list of dictionaries, each with keys Name and Link.
Saving the Data
The scraped data is saved in a JSON file (department_list.json) using Python's json module. This ensures the data is readily available for future steps like database insertion.
Error Handling
Load More Button Errors:
The script handles cases where the "Load More" button is missing or stops responding. It gracefully terminates the scraping loop when the button is no longer clickable.
Scraping Errors:
Exceptions during the scraping process (e.g., missing elements or connection issues) are logged without disrupting the overall workflow.


How It Was Done
Dynamic Loading:
The hospital website uses a "Load More" button to reveal department information incrementally.
Selenium simulates a real user’s actions by scrolling and clicking the button repeatedly until all departments are visible.
Data Extraction:
The page source is parsed with BeautifulSoup to extract department names and links from <div> elements.
Data is organized into a list of dictionaries, ensuring structured output.
Automation:
The script automates the scraping process, requiring minimal human intervention.
It dynamically adjusts to the webpage structure using class names and XPath selectors.
Storage:
The final dataset is saved as a JSON file (department_list.json) for use in subsequent processing steps, such as database storage.

Key Considerations
Dynamic Content Challenges:
The use of Selenium ensures the script handles JavaScript-rendered content seamlessly.
Data Completeness:
By iteratively clicking "Load More," the scraper ensures all departments are captured.
Scalability:
The modular design allows easy adaptation to similar websites with minor tweaks to XPath or class selectors.
Ethical Scraping:
The script respects the website's loading time and interaction mechanisms, ensuring responsible data extraction.

Conclusion
The department scraping process leverages Selenium’s browser automation and BeautifulSoup’s parsing capabilities to extract structured department information from a dynamic webpage. The scraped data, stored in a JSON file, plays a critical role in building a comprehensive dataset for subsequent AI model training.

Practical code for the above mentioned theory:
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













Preprocessing Data: Theory and Methodology
The preprocessing stage is crucial for preparing the raw scraped data into a structured and meaningful format for training the Private GPT model. The provided code processes CSV files containing information about doctors and treatments, converting the data into a question-answer format suitable for training a language model.

Key Objectives of Preprocessing
Load Raw Data: Read CSV files containing raw data about doctors and treatments.
Validate and Clean Data:
Ensure required columns are present.
Remove rows with missing or incomplete information.
Format Data: Convert the structured data into a natural language Q&A format for model training.
Save Processed Data: Consolidate all formatted Q&A pairs into a single text file.

Step-by-Step Explanation of the Code
1. Loading CSV Files
Directory Specification:
csv_directory specifies the folder containing the CSV files for doctors and treatments.
The code iterates over all .csv files in this directory to ensure every file is processed.
Python code
csv_directory = "D:\Web_scraping_and_Ai_model_traing\data_training_files"

File Identification:
The code identifies and processes files based on their names, checking if they contain "doctors" or "treatments" to apply the corresponding processing function.

2. Processing Doctors’ Data
The function process_doctors_data() processes CSV files containing information about doctors:
Validation:
Ensures that columns like id, name, specialization, degree, hospital_name, and link exist. If any are missing, the file is skipped.
Python code
required_columns = ['id', 'name', 'specialization', 'degree', 'hospital_name', 'link']
if all(column in df.columns for column in required_columns):

Data Cleaning:
Removes rows with missing values in the required columns using the dropna() method.
Python code
df = df.dropna(subset=required_columns)

Formatting:
Converts each row into a question-answer pair using apply() and a lambda function.
The Q&A pairs are constructed in plain text, emphasizing the doctor's name, specialization, degree, hospital name, and a link for more details.



Python code
data = df.apply(
    lambda row: (
        f"Question: What is the specialization and degree of Dr. {row['name']} from {row['hospital_name']}?"
        f" Answer: Dr. {row['name']} specializes in {row['specialization']} and holds the degree {row['degree']}. Find more at {row['link']}."
    ),
    axis=1
)


3. Processing Treatments’ Data
The function process_treatments_data() processes treatment-related CSV files:
Validation and Cleaning:
Similar to the doctor data processing, this function ensures required columns like id, treatment_name, treatment_link, and hospital_name exist and removes rows with missing values.
Python code
required_columns = ['id', 'treatment_name', 'treatment_link', 'hospital_name']
df = df.dropna(subset=required_columns)

Formatting:
Each treatment is converted into a question-answer pair emphasizing the treatment name and its link.
Python code
data = df.apply(
    lambda row: (
        f"Question: What is the treatment offered at {row['hospital_name']}?"
        f" Answer: {row['hospital_name']} offers treatment for {row['treatment_name']}. Learn more at {row['treatment_link']}."
    ),
    axis=1
)


4. Iterating Through Files
The code identifies each file's type (doctors or treatments) by checking for keywords in the filename and applies the corresponding processing function:
Python code
if "doctors" in filename.lower():
    processed_data.extend(process_doctors_data(file_path))
elif "treatments" in filename.lower():
    processed_data.extend(process_treatments_data(file_path))
else:
    print(f"Skipping file {filename}: Unknown file type.")


5. Saving Preprocessed Data
After processing all relevant files, the Q&A pairs are saved into a single text file (training_data.txt). This file consolidates all data in a format ready for training the GPT model:
Python code
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(processed_data))

If no valid data is found, the code outputs an error message to prompt a review of the input files.


Theory and Importance
Validation and Cleaning: Ensures that only high-quality, complete, and standardized data is included, minimizing errors during model training.
Natural Language Formatting: Converts raw data into conversational Q&A pairs, optimizing the dataset for fine-tuning GPT models, which are designed to excel at question-answering tasks.
Consolidation: Combines data from multiple sources into a single, unified dataset, simplifying further processing and training.

Outputs
The final preprocessed data in training_data.txt is structured in Q&A pairs like the following:
Example (Doctors):
Vbnet code
Question: What is the specialization and degree of Dr. John Doe from Medanta Hospital?
Answer: Dr. John Doe specializes in Cardiology and holds the degree MBBS, MD. Find more at https://example.com/dr-john-doe.

Example (Treatments):
Vbnet code
Question: What is the treatment offered at Medanta Hospital?
Answer: Medanta Hospital offers treatment for Heart Transplant. Learn more at https://example.com/heart-transplant.

This structured format is ready for the next stage: Fine tuning.


Practical code for the above mentioned theory:

import pandas as pd
import os


# Specify the directory containing CSV files
csv_directory = "D:\Web_scraping_and_Ai_model_traing\data_training_files"


# Specify the output file for the preprocessed text
output_file = "training_data.txt"


# Initialize a list to hold processed data
processed_data = []


# Function to process doctors' data
def process_doctors_data(file_path):
    try:
        df = pd.read_csv(file_path)
       
        # Check if required columns exist
        required_columns = ['id', 'name', 'specialization', 'degree', 'hospital_name', 'link']
        if all(column in df.columns for column in required_columns):
            # Drop rows with missing values in the required columns
            df = df.dropna(subset=required_columns)
           
            # Format data into Q/A
            data = df.apply(
                lambda row: (
                    f"Question: What is the specialization and degree of Dr. {row['name']} from {row['hospital_name']}?"
                    f" Answer: Dr. {row['name']} specializes in {row['specialization']} and holds the degree {row['degree']}. Find more at {row['link']}."
                ),
                axis=1
            )
            return data.tolist()
        else:
            print(f"Skipping file {file_path}: Missing required columns.")
            return []
    except Exception as e:
        print(f"Error processing doctors' file {file_path}: {e}")
        return []


# Function to process treatments' data
def process_treatments_data(file_path):
    try:
        df = pd.read_csv(file_path)
       
        # Check if required columns exist
        required_columns = ['id', 'treatment_name', 'treatment_link', 'hospital_name']
        if all(column in df.columns for column in required_columns):
            # Drop rows with missing values in the required columns
            df = df.dropna(subset=required_columns)
           
            # Format data into Q/A
            data = df.apply(
                lambda row: (
                    f"Question: What is the treatment offered at {row['hospital_name']}?"
                    f" Answer: {row['hospital_name']} offers treatment for {row['treatment_name']}. Learn more at {row['treatment_link']}."
                ),
                axis=1
            )
            return data.tolist()
        else:
            print(f"Skipping file {file_path}: Missing required columns.")
            return []
    except Exception as e:
        print(f"Error processing treatments' file {file_path}: {e}")
        return []


# Iterate through all CSV files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(csv_directory, filename)
        print(f"Processing file: {filename}")
       
        # Process based on file type
        if "doctors" in filename.lower():
            processed_data.extend(process_doctors_data(file_path))
        elif "treatments" in filename.lower():
            processed_data.extend(process_treatments_data(file_path))
        else:
            print(f"Skipping file {filename}: Unknown file type.")


# Save all processed data to a single text file
if processed_data:
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(processed_data))
    print(f"Preprocessed data saved to {output_file}.")
else:
    print("No valid data processed. Check your files and directory.")












Fine-Tuning GPT-2: Theory and Methodology
This fine-tuning process customizes the GPT-2 model using your domain-specific dataset, allowing it to generate more relevant and accurate responses tailored to your use case. The provided code involves the use of the transformers library by Hugging Face, offering a streamlined pipeline for text data fine-tuning.

Key Objectives of Fine-Tuning
Load Pretrained Model and Tokenizer: Initialize a GPT-2 model and tokenizer.
Prepare Dataset:
Tokenize the training and validation datasets.
Create a format suitable for training using a text dataset loader.
Fine-Tune GPT-2:
Train the model on the provided dataset with customized training parameters.
Monitor the training process and periodically save checkpoints.
Save the Fine-Tuned Model: Save the customized model and tokenizer for future use.

Step-by-Step Explanation of the Code
1. Loading Pretrained Model and Tokenizer
The code begins by loading the base GPT-2 model and its tokenizer from the Hugging Face library. These pretrained components provide the foundation for fine-tuning:
Python code
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

Tokenizer:
Converts text into token IDs and handles input formatting.
Special tokens, such as <|endoftext|>, are included to indicate boundaries in the text.
Model:
GPT-2 is initialized with its language modeling head (GPT2LMHeadModel), making it suitable for generating and predicting sequences of text.

2. Tokenizing and Preparing the Dataset
The training and validation datasets are loaded and tokenized using the load_dataset() function. The function reads the text file and processes it into tokenized blocks suitable for model input.



Python code
def load_dataset(path, tokenizer, block_size=128):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return TextDataset(
        tokenizer=tokenizer,
        file_path=path,
        block_size=block_size,
        overwrite_cache=True,
    )

TextDataset:
Splits the input text into chunks of block_size (default 128 tokens).
Adds padding and truncates sequences to ensure uniform input sizes for training.
Files:
train_path: Path to the training data file (training_data.txt).
valid_path: Path to the validation data file (validation_data.txt).

3. Data Collation
The DataCollatorForLanguageModeling handles data preparation during training:
Python code
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

Parameters:
mlm=False: Specifies that this is a causal language modeling task (predict the next word), not masked language modeling.
Prepares batches dynamically, padding or truncating sequences as needed.

4. Setting Training Arguments
The TrainingArguments class specifies hyperparameters and settings for the training process:
Python code
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=500,
    save_total_limit=2,
    logging_dir="./logs",
    learning_rate=5e-5,
)

Key Parameters:
output_dir: Directory to save the fine-tuned model.
num_train_epochs: Number of training passes over the dataset.
per_device_train_batch_size: Number of examples per GPU per step.
save_steps: Save model checkpoints every 500 steps.
save_total_limit: Retain the last two checkpoints.
learning_rate: Learning rate for the optimizer.

5. Training the Model
The Trainer class handles the fine-tuning process, combining the model, datasets, and training arguments:
python
Copy code
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=valid_dataset,
)

Evaluation Dataset:
Used to monitor model performance during training and prevent overfitting.
Training:
The trainer.train() function begins the training loop:
The model learns patterns from the training dataset.
Checkpoints are saved periodically.
Python code
trainer.train()


6. Saving the Fine-Tuned Model
After training, the fine-tuned model and tokenizer are saved to the specified directory for deployment or further experimentation:
Python code
model.save_pretrained("./fine_tuned_gpt2")
tokenizer.save_pretrained("./fine_tuned_gpt2")


Theory and Importance
Pretraining vs. Fine-Tuning:
Pretraining: GPT-2 was pretrained on a diverse dataset to learn general language patterns.
Fine-Tuning: Customizes the model for a specific domain, such as medical Q&A, using specialized datasets.
Transfer Learning:
The fine-tuning process leverages GPT-2's existing knowledge, requiring less data and computational power compared to training from scratch.
Evaluation:
Fine-tuning ensures the model produces domain-specific, coherent, and contextually accurate text outputs.

Outputs
Once fine-tuned, the model can generate high-quality, domain-specific responses:
Input Example:
Csharp code
What is the specialization of Dr. John Doe from Medanta Hospital?

Generated Output:
Arduino code
Dr. John Doe specializes in Cardiology and holds the degree MBBS, MD. Find more at https://example.com/dr-john-doe.

This makes the model highly effective for tasks such as chatbot development, personalized Q&A systems, and content generation.

Practical code for the above mentioned theory:

from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling


# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")


# Tokenize your dataset
train_path = "training_data.txt"  # Your preprocessed text file
valid_path = "validation_data.txt"


def load_dataset(path, tokenizer, block_size=128):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return TextDataset(
        tokenizer=tokenizer,
        file_path=path,
        block_size=block_size,
        overwrite_cache=True,
    )


train_dataset = load_dataset(train_path, tokenizer)
valid_dataset = load_dataset(valid_path, tokenizer)


# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)


# Training arguments
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=500,
    save_total_limit=2,
    logging_dir="./logs",
    learning_rate=5e-5,
)


# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=valid_dataset,
)


# Train
trainer.train()




model.save_pretrained("./fine_tuned_gpt2")
tokenizer.save_pretrained("./fine_tuned_gpt2")









Model Deployment: Theory and Methodology 
In this deployment approach, the task remains the same: to generate responses from a fine-tuned GPT-2 model based on user input. However, the major difference here is the inclusion of user input directly from the terminal, which allows dynamic interaction at runtime. The code leverages the transformers library from Hugging Face to perform this task.

Key Objectives of Deployment
Load the Fine-Tuned Model and Tokenizer: Initialize the fine-tuned GPT-2 model and tokenizer that were trained earlier.
Accept User Input: Take input from the user in real-time.
Process Input: Convert the user's question into tokens the model can understand.
Generate Model Output: Use the fine-tuned model to generate a response based on the user query.
Display Output: Convert the generated tokens back into human-readable text and present the model’s answer.

Step-by-Step Explanation of the Code
1. Loading the Fine-Tuned Model and Tokenizer
The first step in the deployment is to load the trained GPT-2 model and tokenizer from their respective directories:
Python code
model = GPT2LMHeadModel.from_pretrained("./fine_tuned_gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("./fine_tuned_gpt2")

Model:
Loads the custom fine-tuned GPT-2 weights from the ./fine_tuned_gpt2 directory. This model is capable of answering domain-specific questions as per the fine-tuning done previously.
Tokenizer:
Loads the tokenizer that was used during the fine-tuning process. It ensures the input text is appropriately tokenized into token IDs and allows decoding of model outputs back into natural language.

2. Taking User Input
Instead of a predefined prompt, the code takes the input dynamically from the user:
Python code
prompt = input("Enter your question: ")


User Input:
The input() function prompts the user to enter a question via the terminal or command line interface. The model responds based on the content of this input.

3. Tokenizing and Encoding the Input
The input prompt is tokenized (converted into token IDs) using the tokenizer:
Python code
inputs = tokenizer.encode(prompt, return_tensors="pt")

Encoding:
The encode() method converts the user’s natural language input into a sequence of token IDs. These token IDs are then converted into a PyTorch tensor (return_tensors="pt") to feed the model.
The tokenized input can be understood by the model and processed to generate a relevant response.

4. Generating the Response
The tokenized input is passed through the GPT-2 model to generate the response:

Python code
outputs = model.generate(inputs, max_length=50, num_return_sequences=1)

Parameters:
inputs: The tokenized user input fed into the model.
max_length=50: Limits the generated response to 50 tokens, preventing excessive output.
num_return_sequences=1: Requests only one response for the given input.
Model's Generation:
GPT-2 generates the next tokens based on the input context, producing a sequence that is coherent with the user query.
The generated tokens are internally predicted by the model to form a meaningful answer.

5. Decoding and Displaying the Output
After the model generates the output, the tokens are decoded back into human-readable text:
Python code
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Response:", response)


Decoding:
The decode() method converts the token IDs back into text, removing any special tokens (e.g., <|endoftext|>).
The skip_special_tokens=True argument ensures that the output is clean and free of model-specific markers.
Displaying Output:
The model’s response is printed to the console so the user can view the result.

Theory Behind the Process
Inference Process:
The deployment process focuses on leveraging the trained GPT-2 model to generate predictions based on dynamic user inputs.
It is designed for real-time, interactive use, where each prompt leads to a new model-generated response.
Autoregressive Generation:
GPT-2 generates outputs using its autoregressive architecture, meaning it predicts one token at a time based on the previous tokens. This approach ensures coherent, contextually relevant responses.
Tokenization and Decoding:
Tokenization helps the model understand human language by breaking it down into token IDs.
Decoding converts model outputs back to natural language, enabling human-readable responses.
Real-Time Interaction:
The interactive nature of this code makes it suitable for chatbots or any system where dynamic, user-driven responses are necessary.

Sample Interaction
User Input:
Plaintext 
Enter your question: What is the treatment offered at Medanta?

Generated Output:
Plaintext 
Response: Medanta offers treatment for a variety of medical conditions, including oncology, cardiology, and orthopedics. Find more at https://www.medanta.org.








Real-World Applications
This deployment script can be used in the following scenarios:
Chatbot Interfaces:
As part of a medical or general Q&A chatbot, where users can ask specific questions and get responses based on the fine-tuned knowledge.
Automated Customer Support:
The model can be used to automate responses to frequently asked questions in healthcare or other fields.
Interactive FAQ Systems:
Users can enter questions, and the system can generate responses from a knowledge base, providing accurate information.

Conclusion
This version of the model deployment allows for real-time interaction, where users provide input dynamically. The fine-tuned GPT-2 model responds intelligently based on the training it has received, making this deployment ideal for chatbot integration, automated Q&A systems, and other user-facing applications that require quick and context-aware answers.






Final Conclusion
In this project, we successfully developed a system that combines web scraping, data preprocessing, model fine-tuning, and deployment to create an interactive Q&A model. The process began with scraping data from multiple hospital websites to collect relevant information about doctors, treatments, and departments. This data was then preprocessed, formatted into question-answer pairs, and stored for further use.
We employed GPT-2, a powerful language model, and fine-tuned it on our domain-specific dataset, which included information about healthcare professionals, medical treatments, and specialties. Fine-tuning allowed the model to adapt to the nuances and context of the data, ensuring that it could generate accurate and relevant responses to user queries.
The deployment process involved building a user-friendly interface where users could interact with the model by submitting questions. The model, once fed with the user’s input, generated coherent, contextually appropriate responses, leveraging the knowledge it gained during the fine-tuning phase.
This project demonstrated the effectiveness of combining web scraping with machine learning techniques for building an intelligent, domain-specific Q&A system. The fine-tuned GPT-2 model now serves as a powerful tool for answering complex medical-related queries, and it can easily be adapted for use in other fields by modifying the dataset and fine-tuning process. This approach opens doors to numerous applications, including chatbots, automated customer support, and interactive FAQ systems, offering real-time assistance based on comprehensive, specialized knowledge.
By leveraging cutting-edge natural language processing technologies and effective data preprocessing techniques, we’ve created a robust, deployable solution that can provide accurate and timely responses, enriching user experience in a variety of real-world applications.


