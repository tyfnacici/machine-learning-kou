import os
import pandas as pd

def order_data(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Drop any rows with missing data (if applicable)
    df = df.dropna()
    
    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort the DataFrame by the 'Date' column
    df = df.sort_values('Date')
    
    # Format the 'Date' column to 'YYYY/MM/DD'
    df['Date'] = df['Date'].dt.strftime('%Y/%m/%d')
    
    # Save the ordered data to a new CSV file
    output_file = os.path.splitext(file_path)[0] + '_ordered.csv'
    df.to_csv(output_file, index=False)
    print(f"Ordered data saved to '{output_file}'")

def main():
    # Directory containing CSV files
    directory = './Data/AQI/'
    
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            order_data(file_path)

if __name__ == "__main__":
    main()
