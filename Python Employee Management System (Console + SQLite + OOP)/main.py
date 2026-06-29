from database import connect_db
from employee import Employee
from utils import heading

conn, cursor = connect_db()


def add_employee():

    heading("ADD EMPLOYEE")

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    department = input("Enter Department : ")
    salary = float(input("Enter Salary : "))

    emp = Employee(name, age, department, salary)

    cursor.execute(
        "INSERT INTO employees(name,age,department,salary) VALUES(?,?,?,?)",
        (emp.name, emp.age, emp.department, emp.salary)
    )

    conn.commit()

    print("\nEmployee Added Successfully.\n")


def view_employee():

    heading("EMPLOYEE LIST")

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    if not employees:
        print("No Employee Found")
        return

    for row in employees:

        print("-" * 50)
        print("Employee ID :", row[0])
        print("Name        :", row[1])
        print("Age         :", row[2])
        print("Department  :", row[3])
        print("Salary      :", row[4])
        print("-" * 50)


def search_employee():

    heading("SEARCH EMPLOYEE")

    emp_id = int(input("Enter Employee ID : "))

    cursor.execute(
        "SELECT * FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    row = cursor.fetchone()

    if row:

        print("-" * 50)
        print("Employee ID :", row[0])
        print("Name        :", row[1])
        print("Age         :", row[2])
        print("Department  :", row[3])
        print("Salary      :", row[4])
        print("-" * 50)

    else:
        print("Employee Not Found")
def update_employee():

    heading("UPDATE EMPLOYEE")

    emp_id = int(input("Enter Employee ID : "))

    cursor.execute("SELECT * FROM employees WHERE emp_id=?", (emp_id,))
    row = cursor.fetchone()

    if row:

        name = input("Enter New Name : ")
        age = int(input("Enter New Age : "))
        department = input("Enter New Department : ")
        salary = float(input("Enter New Salary : "))

        cursor.execute("""
        UPDATE employees
        SET name=?, age=?, department=?, salary=?
        WHERE emp_id=?
        """, (name, age, department, salary, emp_id))

        conn.commit()

        print("\nEmployee Updated Successfully.\n")

    else:
        print("\nEmployee Not Found.\n")


def delete_employee():

    heading("DELETE EMPLOYEE")

    emp_id = int(input("Enter Employee ID : "))

    cursor.execute("SELECT * FROM employees WHERE emp_id=?", (emp_id,))
    row = cursor.fetchone()

    if row:

        cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
        conn.commit()

        print("\nEmployee Deleted Successfully.\n")

    else:
        print("\nEmployee Not Found.\n")
while True:

    heading("EMPLOYEE MANAGEMENT SYSTEM")

    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employee()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Thank You...")
        conn.close()
        break

    else:
        print("Invalid Choice")        