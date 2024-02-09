"""
Import everything you need to launch the organizer
Load the colleagues from the excel file defined in the config file
Launch the organizer. Display the results.
"""
import csv

# Specify the path to your CSV file (converted from Excel)
csv_file_path = 'C:\Users\fabie\OneDrive\Documenten\BeCodeGhent\GNT-Arai-6\projects\01-openspace-organizer\new_colleagues.csv'

# Open the CSV file and read its contents
data_list = []

with open(csv_file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    
    # Skip the header row if present
    header = next(csv_reader, None)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # 'row' is a list containing values from each column
        data_list.append(row)

# Now, 'data_list' contains the data from the CSV file as a list of lists
for row in data_list:
    print(row)