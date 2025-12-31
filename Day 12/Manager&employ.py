from collections import defaultdict

# Data
managers = ['M1', 'M2', 'M3']             #A list of manager names (M1, M2, M3).
employees = [f'E{i}' for i in range(1, 13)] #A list of employee names (E1, E2, ..., E12).

# Function to map employees to managers
def map_employees(managers, employees): # Maps employees to managers and returns a dictionary-like object.
    # Create a cyclic iterator over managers
    manager_cycle = iter(managers * (len(employees) // len(managers) + 1))
    
    # Map employees to managers
    mapping = defaultdict(list)
    for employee in employees:
        manager = next(manager_cycle)
        mapping[manager].append(employee)
    
    return mapping

# Map employees to managers
employee_mapping = map_employees(managers, employees)

# Display the mapping
print("Employee Mapping:")
for manager, employees in employee_mapping.items():
    print(f"{manager}: {employees}")

# Function to get employees under a specific manager
def get_employees_under_manager(manager): #Returns a list of employees under a specific manager.
    return employee_mapping.get(manager, [])

# Function to get busy managers
def get_busy_managers(min_employees=4): # Returns a list of managers with at least min_employees employees.
    return list(filter(lambda x: len(x[1]) >= min_employees, employee_mapping.items()))

# Main loop
while True:
    print("\nOptions:")
    print("1. Display employee mapping")
    print("2. Get employees under a manager")
    print("3. Get busy managers")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Employee Mapping:")
        for manager, employees in employee_mapping.items():
            print(f"{manager}: {employees}")
    elif choice == '2':
        manager = input("Enter manager name (e.g., M1, M2, M3): ")
        employees = get_employees_under_manager(manager)
        if employees:
            print(f"Employees under {manager}: {employees}")
        else:
            print(f"No employees found under {manager}")
    elif choice == '3':
        min_employees = int(input("Enter minimum employees for a busy manager: "))
        busy_managers = get_busy_managers(min_employees)
        if busy_managers:
            print("Busy Managers:")
            for manager, employees in busy_managers:
                print(f"{manager}: {employees}")
        else:
            print("No busy managers found")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

