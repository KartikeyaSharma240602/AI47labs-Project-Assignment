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
