# Madhumal Motors Inventory System

This project is an inventory management system for motorcycles, built using Python, Gradio, and CSV for local file storage, or MySQL for database management.

## Features

1. **Add Motorcycle to Inventory**: Allows users to add new motorcycles to the inventory with details such as make, model, quantity, and price.
2. **Search Motorcycle Price**: Search the price of a motorcycle by its make and model.
3. **Create Invoice**: Create an invoice when a motorcycle is sold, deducting the quantity from the inventory and generating a total price.
4. **Inventory Report**: Generate a report of the current inventory, showing the make, model, and quantity of motorcycles available.
5. **Update Bike Information**: Modify the quantity or price of a motorcycle in the inventory.
6. **Delete Bike**: Delete a motorcycle from the inventory by its make and model.

## Technology Stack

- **Python**: The primary programming language used to implement the system.
- **Gradio**: A Python library used to build the user interface.
- **MySQL**: Database used for storing inventory and sales data.
- **CSV**: Used for storing inventory data in local files.

## Getting Started

### Requirements

- Python 3.x
- Gradio library
- MySQL server (for database version) or CSV for file-based version

Install necessary Python packages:

```bash
pip install gradio mysql-connector-python


### Running the Application

#### 1. **CSV Version (Standalone)**

- The application uses a CSV file `motorcycles.csv` to store inventory data.
- When the program is run, it initializes the CSV file if it doesn't already exist, and allows the user to add, search, and delete motorcycles from the inventory.

#### 2. **Database Version (MySQL)**

- If you choose to use MySQL, set up a MySQL database named `madhumal_motors` and create the tables `inventory` and `sales`.
- The application connects to this database to manage inventory and sales data.

### Usage

1. **Add Motorcycle to Inventory**:
    - Input details such as make, model, quantity, and price to add a new motorcycle to the inventory.
   
2. **Search Motorcycle Price**:
    - Search for a motorcycle by make and model to retrieve its price.
   
3. **Create Invoice**:
    - Select a motorcycle, enter the quantity sold, and generate an invoice that updates the inventory.
   
4. **Generate Inventory Report**:
    - View a summary of available motorcycles with make, model, and quantity.
   
5. **Update Bike Information**:
    - Modify the quantity and/or price of a motorcycle in the inventory.

6. **Delete Motorcycle**:
    - Remove a motorcycle from the inventory by specifying its make and model.

### Example Usage

Run the program in a terminal or IDE, and interact with the prompts to manage your motorcycle inventory.

### Gradio Interface

A web-based user interface is also available using Gradio. The UI allows you to perform the same actions through tabs:

- **Add Bike**: Adds new motorcycles to the inventory.
- **Search Price**: Searches and displays the price of a motorcycle.
- **Create Invoice**: Allows the creation of an invoice for sold motorcycles.
- **Inventory Report**: Generates a report of the current inventory.
- **Update Bike**: Updates the details of an existing motorcycle.
- **Delete Bike**: Deletes a motorcycle from the inventory.

To launch the Gradio interface, simply run the script:

```python
inventory_interface()
```

### File Structure

- `motorcycles.csv`: Stores inventory data for the CSV-based system.
- `main.py`: Contains the core logic for both CSV and MySQL-based implementations.
- `gradio_interface.py`: The Gradio-based UI setup for managing inventory.

### Google Colab 
https://colab.research.google.com/drive/1qwO0y6A-RRwq8fkU5Cze5sr-9mjc9eVV?usp=sharing

###GUI Video
https://drive.google.com/file/d/1KxxZR-Xvyyc7zPUOI1t98R0fkcPx82Vl/view?usp=drive_link
