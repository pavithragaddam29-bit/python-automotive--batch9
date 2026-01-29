# Import pandas library to create Excel file
import pandas as pd

# ---------------------------------
# Dictionary 1: Employee Name -> Employee ID
# ---------------------------------
D1 = {
    "nathin": "01",
    "rahul": "02",
    "sita": "03",
    "arjun": "04",
    "meena": "05",
    "kiran": "06",
    "priya": "07",
    "vijay": "08"
}

# ---------------------------------
# Dictionary 2: Employee ID -> Computer Number 
# ---------------------------------
D2 = {
    "01": "pc10",
    "02": "pc11",
    "03": "pc12",
    "04": "pc13",
    "05": "pc14",
    "06": "pc15",
    "07": "pc16",
    "08": "pc17"
}

# ---------------------------------
# Empty list to store rows for Excel
# ---------------------------------
rows = []

# ---------------------------------
# Loop through D1 and match with D2
# ---------------------------------
for employee_name, employee_id in D1.items():
    computer_number = D2.get(employee_id, "Not Assigned")
    rows.append([employee_name, employee_id, computer_number])

# ---------------------------------
# Create DataFrame (table)                               Pandas DataFrame = Excel sheet inside Python
# ---------------------------------
df = pd.DataFrame(
    rows,
    columns=["Employee Name", "Employee Id", "Computer Number"]
)

# ---------------------------------
# Save data to Excel
# ---------------------------------
df.to_excel("employee_details.xlsx", index=False)                  #“Take this table (DataFrame) and save it as an Excel file”

# ---------------------------------
# Success message
# ---------------------------------
print("Excel file  created successfully!")
