import json
import psycopg2

# PostgreSQL Configuration
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Satyam@2608",
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
