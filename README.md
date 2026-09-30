# Employee Salary Slip Calculator

A simple Python program that calculates an employee's salary details and generates a salary slip using a Python dictionary.

## Overview

This project takes basic employee information such as employee ID, employee name, and basic salary as input. It then calculates allowances, gross salary, deductions, and finally the employee's net salary.

The project demonstrates the use of Python dictionaries, user input, arithmetic calculations, and formatted output.

## Features

- Accepts employee ID and employee name
- Accepts basic salary from the user
- Calculates HRA at 20% of basic salary
- Calculates DA at 10% of basic salary
- Adds a fixed transport allowance of ₹2000
- Calculates gross salary
- Calculates provident fund at 12% of gross salary
- Applies professional tax of ₹200
- Calculates total deductions
- Calculates net salary
- Displays a formatted salary slip

## Salary Calculation

**HRA**
```text
HRA = 20% of Basic Salary
```

**DA**
```text
DA = 10% of Basic Salary
```

**Gross Salary**
```text
Gross Salary = Basic Salary + HRA + DA + Transport Allowance
```

**Provident Fund**
```text
Provident Fund = 12% of Gross Salary
```

**Total Deductions**
```text
Total Deductions = Provident Fund + Professional Tax
```

**Net Salary**
```text
Net Salary = Gross Salary - Total Deductions
```

## Technologies Used

- Python
- Python Dictionary
- User Input
- Arithmetic Operators
- `round()` function

## How to Run

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or another Python editor.
4. Run `main.py`.
5. Enter the employee details when prompted.
6. The program will display the calculated salary slip.

## Example

```text
Enter employee ID: E101
Enter employee name: Rahul
Enter employee salary: 30000

-------- EMPLOYEE SALARY SLIP --------
Employee ID             : E101
Employee Name           : Rahul
Basic Salary            : 30000.0
HRA (20%)               : 6000.0
DA (10%)                : 3000.0
Transport Allowance     : 2000.0
-------------------------------------------
Gross Salary            : 41000.0
Provident Fund (12%)    : 4920.0
Professional Tax        : 200
Total Deductions        : 5120.0
-------------------------------------------
Net Salary              : 35880.0
```

## Project Purpose

The purpose of this project is to practice Python programming concepts by creating a simple employee salary calculation system using a dictionary and basic mathematical operations.

## Author

**Arabdh joshi**
