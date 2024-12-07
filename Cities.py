import sqlite3

def displayData():
    # Display all data from the departments,lLocations, and employees tables
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()

    # Display departments table
    print("\nDepartments:")
    cur.execute("SELECT * FROM Departments")
    departments = cur.fetchall()
    if departments:
        for dept in departments:
            print(f"DepartmentID: {dept[0]}, DepartmentName: {dept[1]}")
    else:
        print("No data in Departments table.")

    # Display locations table
    print("\nLocations:")
    cur.execute("SELECT * FROM Locations")
    locations = cur.fetchall()
    if locations:
        for loc in locations:
            print(f"LocationID: {loc[0]}, City: {loc[1]}")
    else:
        print("No data in Locations table.")

    # Display employeees table
    print("\nEmployees:")
    cur.execute('''
        SELECT e.EmployeeID, e.Name, e.Position, d.DepartmentName, l.City
        FROM Employees e
        LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID
        LEFT JOIN Locations l ON e.LocationID = l.LocationID
    ''')
    employees = cur.fetchall()
    if employees:
        for emp in employees:
            print(f"EmployeeID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, "
                  f"Department: {emp[3]}, Location: {emp[4]}")
    else:
        print("No data in Employees table.")

    conn.close()

if __name__ == "__main__":
    displayData()

