import csv
from collections import defaultdict
import locale

# Set locale for currency formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# File path to the downloaded CSV file
file_path = '2012_Expenditures.csv'

# Initialize a defaultdict to store expenditures by department
department_expenses = defaultdict(float)

# Read the CSV file and aggregate expenditures by department
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        department = row['Department']
        try:
            expense = locale.atof(row['2012 Actual'])
            department_expenses[department] += expense
        except ValueError:
            # Handle cases where '2012 Actual' is not a valid number
            continue

# Print the aggregated results
print("Department\tTotal 2012 Expenditure")
print("=" * 40)
for department, total_expense in department_expenses.items():
    formatted_expense = locale.currency(total_expense, grouping=True)
    print(f"{department}\t{formatted_expense}")