employee = {}

employee["id"] = input("Enter employee ID: ")
employee["name"] = input("Enter employee name: ")
employee["basic_salary"] = float(input("Enter employee salary: "))

employee["hra"] = 0.20 * employee["basic_salary"]
employee["da"] = 0.10 * employee["basic_salary"]
employee["transport_allowance"] = 2000

employee["gross_salary"] = (
    employee["basic_salary"]
    + employee["hra"]
    + employee["da"]
    + employee["transport_allowance"]
)

employee["provident_fund"] = 0.12 * employee["gross_salary"]
employee["professional_tax"] = 200

employee["total_deduction"] = (
    employee["provident_fund"]
    + employee["professional_tax"]
)

employee["net_salary"] = (
    employee["gross_salary"]
    - employee["total_deduction"]
)

print("\n-------- EMPLOYEE SALARY SLIP --------")

print("Employee ID             :", employee["id"])
print("Employee Name           :", employee["name"])
print("Basic Salary            :", round(employee["basic_salary"], 2))
print("HRA (20%)               :", round(employee["hra"], 2))
print("DA (10%)                :", round(employee["da"], 2))
print("Transport Allowance     :", round(employee["transport_allowance"], 2))

print("-------------------------------------------")

print("Gross Salary            :", round(employee["gross_salary"], 2))
print("Provident Fund (12%)    :", round(employee["provident_fund"], 2))
print("Professional Tax        :", round(employee["professional_tax"], 2))
print("Total Deductions        :", round(employee["total_deduction"], 2))

print("-------------------------------------------")

print("Net Salary              :", round(employee["net_salary"], 2))


