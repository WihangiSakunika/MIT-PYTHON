# Madhumal Motors Inventory System

This project is an inventory management system for a motorcycle store built with **MySQL** as the database and **Gradio** for the user interface. It allows you to manage motorcycles in inventory, create invoices, search for prices, update bike information, and generate inventory reports.

## Features

- **Add Bike to Inventory**: Add new bikes to the inventory by specifying the make, model, quantity, and price.
- **Search Price**: Search for the price of a motorcycle by its make and model.
- **Create Invoice**: Generate invoices for customers, adjusting inventory quantities as bikes are sold.
- **Inventory Report**: View the current stock of bikes in the inventory.
- **Update Bike Information**: Modify the quantity or price of a bike already in the inventory.
- **Delete Bike from Inventory**: Remove a bike from the inventory.

## Prerequisites

Make sure the following are installed before running the application:

- **Python 3.x**
- **MySQL** (for the database)
- **Gradio** (for the user interface)
- **mysql-connector-python** (for MySQL database connection)

### Install Dependencies

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate

# Install required Python libraries
pip install mysql-connector-python gradio
```

## Database Setup

1. **Install MySQL** if you haven't already. You can download it from [here](https://dev.mysql.com/downloads/installer/).

2. **Create Database and Tables**:

   After installing MySQL, log in to the MySQL server and run the following SQL commands to set up the database and tables:

   ```sql
   -- Create the database
   CREATE DATABASE madhumal_motors;

   -- Switch to the new database
   USE madhumal_motors;

   -- Create the inventory table
   CREATE TABLE inventory (
       make VARCHAR(50),
       model VARCHAR(50),
       quantity INT,
       price DECIMAL(10, 2)
   );

   -- Create the sales table
   CREATE TABLE sales (
       customer_name VARCHAR(100),
       bike_make VARCHAR(50),
       bike_model VARCHAR(50),
       quantity_sold INT,
       total_price DECIMAL(10, 2)
   );
   ```

3. **Configure the Connection**:

   In the Python code, the `connect_db()` function connects to the MySQL database. Make sure that your credentials are correct (username, password, database, host).

   ```python
   def connect_db():
       return mysql.connector.connect(
           host="localhost",
           database="madhumal_motors",
           user="root",  # Change if necessary
           password=""    # Add your password if needed
       )
   ```

## Running the Application

1. **Start the Application**:

   After setting up your environment and database, run the Python script to start the Gradio interface:

   ```bash
   python main.py
   ```

   This will start a local web application at `http://127.0.0.1:7860/` (or another URL that will be printed in the terminal).

2. **Interact with the Application**:

   The Gradio app will provide tabs for each feature:
   
   - **Add Bike**: Add new motorcycles to the inventory.
   - **Search Price**: Find the price of a bike based on its make and model.
   - **Create Invoice**: Create an invoice for a customer, adjusting stock levels automatically.
   - **Inventory Report**: View the available stock of bikes.
   - **Update Bike**: Modify the quantity or price of a bike.
   - **Delete Bike**: Remove a bike from the inventory.

## Troubleshooting

- **Database Connection Issues**: Verify that MySQL is running, and check your credentials (username, password, host) in the `connect_db()` function.
- **Missing Tables**: Ensure the database and tables are created as per the SQL instructions above.
