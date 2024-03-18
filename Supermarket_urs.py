from datetime import datetime
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root123",
    password="Password123#4",
    database="supermarket"
)
mycursor = mydb.cursor()

# Create bills table if it doesn't exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS bills (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        total_amount DECIMAL(10, 2),
        gst_amount DECIMAL(10, 2),
        final_amount DECIMAL(10, 2),
        date_time DATETIME
    )
""")

# Create bill_items table if it doesn't exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS bill_items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        bill_id INT,
        item VARCHAR(255),
        quantity INT,
        price DECIMAL(10, 2),
        FOREIGN KEY (bill_id) REFERENCES bills(id)
    )
""")

name = input("Enter your name:")

# List of items
lists = '''
Rice     rs 20/kg
Sugar    rs 40/kg
Salt     rs 20/kg
Oil      rs 120/lit
Paneer   rs 150/kg
Maggie   rs 60/kg
Horlicks rs 88/kg
Brush    rs 20/each
Colgate  rs 38/each
'''
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

# Rates for items
items = {
    'Rice': 20,
    'Sugar': 40,
    'Salt': 20,
    'Oil': 120,
    'Paneer': 150,
    'Maggie': 60,
    'Horlicks': 88,
    'Brush': 20,
    'Colgate': 38
}

option = int(input("for list of items press 1:"))

if option == 1:
    print(lists)

for i in range(len(items)):
    inp1 = int(input("if you want buy press 1 or 2 for exit:"))
    if inp1 == 2:
        break

    if inp1 == 1:
        item = input("Enter your items:")
        quantity = int(input("Enter quantity:"))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append(price)
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
        else:
            print("Sorry, the item you entered is not available.")

# Calculate GST and final amount
gst = (totalprice * 5) / 100
finalamount = gst + totalprice

print(finalamount)
inp = input("Can I bill the items? (yes or no): ")
if inp.lower() == 'yes':
    if finalamount != 0:
        # Insert data into MySQL table
        sql = "INSERT INTO bills (name, total_amount, gst_amount, final_amount, date_time) VALUES (%s, %s, %s, %s, %s)"
        val = (name, totalprice, gst, finalamount, datetime.now())
        mycursor.execute(sql, val)
        mydb.commit()

        # Fetch the last inserted bill ID
        bill_id = mycursor.lastrowid

        # Insert individual items into MySQL table
        for i in range(len(pricelist)):
            sql = "INSERT INTO bill_items (bill_id, item, quantity, price) VALUES (%s, %s, %s, %s)"
            val = (bill_id, ilist[i], qlist[i], plist[i])
            mycursor.execute(sql, val)
            mydb.commit()

        # Print the bill
        print(25 * "=", "Ours Supermarket", 25 * "=")
        print(28 * " ", "Urs Mart")
        print("Name:", name, 30 * " ", "Date:", datetime.now())
        print(75 * "-")
        print("Sno", 2 * " ", 'Items', 4 * " ", 'Quantity', 7 * " ", 'Price')
        for i in range(len(pricelist)):
            print(i + 1, 1 * " ", 5 * " ", ilist[i], 5 * " ", qlist[i], 7 * " ", plist[i])
        print(75 * "-")
        print(50 * " ", 'Total Amount:', 'Rs', totalprice)
        print("GST Amount", 50 * " ", 'Rs', gst)
        print(75 * "-")
        print(50 * " ", 'Final Amount:', 'Rs', finalamount)
        print(75 * "-")
        print(20 * " ", "<<<<Thanks for visiting>>>>")
        print(20 * " ", ".......Visit Again........")

# Close MySQL connection
mydb.close()
