import psycopg2
import gradio as gr
from datetime import datetime
import mysql.connector

# Database connection setup
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        database="madhumal_motors",
        user="root",
        password=""
    )

# 1. Add motorcycle to inventory
def add_bike(make, model, quantity, price):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO inventory (make, model, quantity, price) VALUES (%s, %s, %s, %s)",
                (make, model, quantity, price))
    conn.commit()
    conn.close()
    return f"Added {quantity} units of {make} {model} at {price} each."

# 2. Search for bike price by make and model
def search_price(make, model):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT price FROM inventory WHERE make = %s AND model = %s", (make, model))
    price = cur.fetchone()
    conn.close()
    if price:
        return f"The price of {make} {model} is {price[0]}"
    else:
        return "Bike not found in the inventory."

# 3. Create invoice
def create_invoice(customer_name, make, model, quantity):
    conn = connect_db()
    cur = conn.cursor()

    # Check availability
    cur.execute("SELECT price, quantity FROM inventory WHERE make = %s AND model = %s", (make, model))
    result = cur.fetchone()
    if not result:
        conn.close()
        return "Bike not found."

    price, available_quantity = result
    if available_quantity < quantity:
        conn.close()
        return "Not enough quantity available."

    # Update inventory
    new_quantity = available_quantity - quantity
    cur.execute("UPDATE inventory SET quantity = %s WHERE make = %s AND model = %s",
                (new_quantity, make, model))

    # Insert into sales
    total_price = price * quantity
    cur.execute(
        "INSERT INTO sales (customer_name, bike_make, bike_model, quantity_sold, total_price) VALUES (%s, %s, %s, %s, %s)",
        (customer_name, make, model, quantity, total_price))
    conn.commit()
    conn.close()
    return f"Invoice created. {quantity} {make} {model} sold to {customer_name} for {total_price}."

# 4. Display inventory report
def inventory_report():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT make, model, quantity FROM inventory")
    inventory = cur.fetchall()
    conn.close()
    report = "\n".join([f"{make} {model}: {quantity} available" for make, model, quantity in inventory])
    return report if report else "No bikes in the inventory."

# 5. Update bike information
def update_bike(make, model, quantity, price):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE inventory SET quantity = %s, price = %s WHERE make = %s AND model = %s",
                (quantity, price, make, model))
    conn.commit()
    conn.close()
    return f"Updated {make} {model} with {quantity} units at {price} each."

# 6. Delete bike from inventory
def delete_bike(make, model):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM inventory WHERE make = %s AND model = %s", (make, model))
    conn.commit()
    conn.close()
    return f"Deleted {make} {model} from the inventory."

# Gradio UI Setup
def inventory_interface():
    with gr.Blocks() as app:
        gr.Markdown("## Madhumal Motors Inventory System")

        # Add Bike Tab
        with gr.Tab("Add Bike"):
            make = gr.Textbox(label="Make")
            model = gr.Textbox(label="Model")
            quantity = gr.Number(label="Quantity")
            price = gr.Number(label="Price")
            add_btn = gr.Button("Add Bike")
            output_add = gr.Textbox(label="Output")
            add_btn.click(add_bike, [make, model, quantity, price], output_add)

        # Search Price Tab
        with gr.Tab("Search Price"):
            search_make = gr.Textbox(label="Make")
            search_model = gr.Textbox(label="Model")
            search_btn = gr.Button("Search Price")
            output_search = gr.Textbox(label="Output")
            search_btn.click(search_price, [search_make, search_model], output_search)

        # Create Invoice Tab
        with gr.Tab("Create Invoice"):
            customer_name = gr.Textbox(label="Customer Name")
            inv_make = gr.Textbox(label="Make")
            inv_model = gr.Textbox(label="Model")
            inv_quantity = gr.Number(label="Quantity")
            inv_btn = gr.Button("Create Invoice")
            output_inv = gr.Textbox(label="Output")
            inv_btn.click(create_invoice, [customer_name, inv_make, inv_model, inv_quantity], output_inv)

        # Inventory Report Tab
        with gr.Tab("Inventory Report"):
            report_btn = gr.Button("Generate Report")
            output_report = gr.Textbox(label="Inventory Report", lines=10)
            report_btn.click(inventory_report, None, output_report)

        # Update Bike Tab
        with gr.Tab("Update Bike"):
            up_make = gr.Textbox(label="Make")
            up_model = gr.Textbox(label="Model")
            up_quantity = gr.Number(label="Quantity")
            up_price = gr.Number(label="Price")
            update_btn = gr.Button("Update Bike")
            output_update = gr.Textbox(label="Output")
            update_btn.click(update_bike, [up_make, up_model, up_quantity, up_price], output_update)

        # Delete Bike Tab
        with gr.Tab("Delete Bike"):
            del_make = gr.Textbox(label="Make")
            del_model = gr.Textbox(label="Model")
            delete_btn = gr.Button("Delete Bike")
            output_delete = gr.Textbox(label="Output")
            delete_btn.click(delete_bike, [del_make, del_model], output_delete)

    app.launch(share=True)

# Start the Gradio interface
inventory_interface()
