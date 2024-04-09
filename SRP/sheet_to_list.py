import openpyxl

#Insert Variables
spreadsheet_path = "D:\\VSCode\\SRP\\NIHProjectData.xlsx"   #<---insert path to .xlsx file
sheet_number = 0
foa = 1
application_id = 4
project_title = 5
project_public_health_relevance = 6
project_abstract = 7
total_cost = 54
foa_text = 55

#Initialize spreadsheet
wb = openpyxl.load_workbook(spreadsheet_path)
ws = wb.worksheets[sheet_number]

#Order of data in list
info = [    
    application_id, 
    project_title, 
    project_abstract, 
    foa,
    foa_text, 
    project_public_health_relevance, 
    total_cost
]

data_list = []

# Iterate through each row in the sheet
for row in ws.iter_rows(min_row=2, values_only=True):  # Start from the second row (skipping the header row)
    row_data = [row[column - 1] for column in info]  # Extract the data from the specified columns
    data_list.append(row_data)  # Append the data for the current row to the main list

# Print the data list (for demonstration purposes)
#for row_data in data_list:
#    print(row_data)

print(data_list[0])