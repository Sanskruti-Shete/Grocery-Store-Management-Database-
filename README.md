# Grocery-Store-Management-Database-
Grocery Store Management Database (py and csv)

# Grocery Store Management System

A simple Python-based grocery store management system with CSV file storage for tracking customers, products, and employees.

## Features

- Add, view, and delete customer records
- Add, view, and delete product details  
- Add, view, and delete employee information
- Create and manage grocery lists

## Files

The system uses three CSV files and one text file:
- `Customer.csv`: Stores customer name, ID, phone number, and address
- `Product.csv`: Stores product name, ID, cost, and stock level
- `Employee.csv`: Stores employee name, ID, age, position, and salary
- `Grocery List.txt`: Stores user-created grocery lists

## Usage

1. Run the program (`python 123.py`)
2. Select options from the main menu by entering the corresponding number
3. Follow the prompts to add, view or delete records

## Menu Options

1. Add Customer details
2. Add Product details
3. Add Employee details
4. Create Grocery List
5. Display all customer details
6. Display all product details
7. Display all employee details
8. Delete customer details
9. Delete Product details
10. Delete Employee details
11. Exit

## Requirements

- Python 3.x
- CSV module (built into Python standard library)

## Notes

- When deleting records, you need to enter the exact ID of the record you want to delete
- To stop adding items to a grocery list, enter '*'

## Future Improvements

Potential enhancements for future versions:
- Input validation
- Error handling for file operations
- Search functionality
- Data backup and restore options
- User authentication
