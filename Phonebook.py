import sqlite3

def connect_db():
    # Connect to the employees database
    conn = sqlite3.connect("employees.db")
    return conn

def view_employees(conn):
    # Display all employees, department, and location
    view = '''
    SELECT e.EmployeeID, e.Name, e.Position, d.DepartmentName, l.City
    FROM Employees e
    JOIN Departments d ON e.DepartmentID = d.DepartmentID
    JOIN Locations l ON e.LocationID = l.LocationID
    '''
    rows = conn.execute(view).fetchall()
    if rows:
        print("\nEmployees:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, "
                  f"Department: {row[3]}, Location: {row[4]}")
    else:
        print("No employees found.")


def update_employee(conn):
    # Update an employee's name, position, department, or location
    employee_id = input("Enter the ID of the employee to update: ")
    row = conn.execute("SELECT * FROM Employees WHERE EmployeeID = ?", (employee_id,)).fetchone()
    if row:
        print("\nAvailable Departments:")
        for dept in conn.execute("SELECT * FROM Departments").fetchall():
            print(f"{dept[0]}: {dept[1]}")

        print("\nAvailable Locations:")
        for loc in conn.execute("SELECT * FROM Locations").fetchall():
            print(f"{loc[0]}: {loc[1]}")

        new_name = input(f"Enter new name (current: {row[1]}): ") or row[1]
        new_position = input(f"Enter new position (current: {row[2]}): ") or row[2]
        new_department = input(f"Enter new department ID (current: {row[3]}): ") or row[3]
        new_location = input(f"Enter new location ID (current: {row[4]}): ") or row[4]

        conn.execute('''
            UPDATE Employees
            SET Name = ?, Position = ?, DepartmentID = ?, LocationID = ?
            WHERE EmployeeID = ?
        ''', (new_name, new_position, new_department, new_location, employee_id))
        conn.commit()
        print("Employee updated successfully.")
    else:
        print("Employee not found.")


def delete_employee(conn):
    # Delete an employee by ID number
    employee_id = input("Enter the ID of the employee to delete: ")
    if conn.execute("DELETE FROM Employees WHERE EmployeeID = ?", (employee_id,)).rowcount:
        conn.commit()
        print("Employee deleted.")
    else:
        print("Employee not found.")

def main():
    # Main loop
    conn = connect_db()
    while True:
        print("\n1. View Employees\n2. Update an Employee\n3. Delete an Employee\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_employees(conn)
        elif choice == "2":
            update_employee(conn)
        elif choice == "3":
            delete_employee(conn)
        elif choice == "4":
            print("Adios")
            break
        else:
            print("Invalid choice.")
    conn.close()

if __name__ == "__main__":
    main()
