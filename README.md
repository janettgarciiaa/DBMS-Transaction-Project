# DBMS Transaction Project

This project demonstrates how database transactions work using PostgreSQL and Python.  
The goal of the project is to show how changes across related tables can be handled safely while maintaining data integrity.

The database includes three tables:
- Product
- Depot
- Stock

Since these tables are connected through foreign keys, changes to one table often require updates to another. To handle this, transactions are used to ensure that all related operations either complete successfully or are rolled back if an error occurs.

## Technologies Used
- PostgreSQL
- Python 3
- psycopg2

## Project Files
- `create_schema.py`  
  Drops existing tables (if they exist), recreates the schema, and inserts sample data for testing and demonstration.

- `db_connect.py`  
  Handles the connection between the Python application and the PostgreSQL database.

- `transactions.py`  
  Contains the logic for Transactions 1–6. Each transaction is implemented using explicit `BEGIN` and `COMMIT` statements to demonstrate ACID properties.

- `menu.py`  
  Provides a simple command-line menu used to run each transaction during the presentation.

## Transactions Implemented
1. Delete product `p1` from Product and Stock  
2. Delete depot `d1` from Depot and Stock  
3. Rename product `p1` to `p10` in Product and Stock  
4. Rename depot `d1` to `d10`  
5. Insert a new product and corresponding stock  
6. Insert a new depot and corresponding stock  

All transactions are handled reactively in the application code to maintain referential integrity.

## How to Run the Project
```bash
python3 create_schema.py
python3 menu.py

## Project Presentation Video

You can watch our full DBMS Transactions Project presentation here:

**Google Drive Video Link:**  
https://drive.google.com/file/d/1EtmSajH8lKZjKbE-2wMoNgsOPcPIseM5/view
