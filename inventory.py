import mysql.connector

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '*****',
    'database': 'inventory',
}

get_inventory_declaration = {
    "name": "get_inventory",
    "description": "Retrieves the inventory list"
}

def setup_database():
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS inventory (
       part_id INT AUTO_INCREMENT PRIMARY KEY,
       part_name VARCHAR(255) NOT NULL,
       quantity INT NOT NULL,
       price INT NOT NULL
    )'''

    cursor.execute(sql)
    print("Table created successfully")

    conn.close()

def insert_sample_data():
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # Sample data
    parts = [
        ('TATA Windshield', 10, 1500),
        ('Mahindra Tire', 50, 750),
        ('Suzuki Brake Pad', 100, 300),
        ('Ford Display', 5, 2000),
        ('Suzuki Bumper', 5, 2000),
        ('Toyota Headlight', 15, 1200),
        ('Honda Side Mirror', 20, 800),
        ('Nissan Brake Caliper', 30, 500),

    ]

    cursor.executemany('INSERT INTO inventory (part_name, quantity, price) VALUES (%s, %s, %s)', parts)

    conn.commit()
    conn.close()

def get_inventory():
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    query = "SELECT * FROM inventory;"
    cursor.execute(query)

    rows = cursor.fetchall()

    inventory_list = [{"part_id": row[0], "part_name": row[1],
                       "quantity": row[2], "price": row[3]} for row in rows]

    conn.close()

    return inventory_list

setup_database()
insert_sample_data()
print(get_inventory())
