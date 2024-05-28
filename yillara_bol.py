import csv
from collections import defaultdict

# Function to read the CSV data and separate it by year
def separate_csv_by_year(input_file):
    data_by_year = defaultdict(list)
    with open(input_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            year = row[0].split('/')[0]
            data_by_year[year].append(row)

    for year, data in data_by_year.items():
        output_file = f'data_{year}.csv'
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f'Data for {year} written to {output_file}')

# Example usage
input_file = 'Data/AQI/ankara_ordered.csv'  # Name of your input CSV file
separate_csv_by_year(input_file)
