import json
import requests
from bs4 import BeautifulSoup
import psycopg2

# PostgreSQL Configuration
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Satyam@2608",
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
