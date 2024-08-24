# Comprehensive Library Management System

## Project Overview

The Comprehensive Library Management System (LMS) is a Python-based application designed to manage the operations of a library, including book inventory management, member management, transaction tracking, and financial management. The system is built using Object-Oriented Programming (OOP) principles and features data persistence through CSV files, as well as graphical reporting for insights into library activities.

## Features

- **Book Inventory Management:**

  - Add, view, search, and remove book records.
  - Store essential book details such as title, author, ISBN, publication date, and genre.

- **Member Management:**

  - Add and manage member records.
  - Store member details such as name, member ID, contact information, and join date.

- **Transaction Management:**

  - Issue books to members and track loan dates.
  - Record the return of books and calculate overdue fines.

- **Reporting and Analytics:**

  - Generate reports on book inventories, loan trends, and member activities.
  - Create graphical representations of data using `matplotlib` and `seaborn`.

- **Data Persistence:**
  - Store books and member records in CSV files for data persistence.
  - Load records from CSV files upon system startup.

## Requirements

- Python 3.x
- Libraries:
  - `matplotlib`
  - `seaborn`
  - `pandas`

To install the required libraries, run:

```bash
pip install matplotlib seaborn pandas
```
