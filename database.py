import sqlite3

def connect_db():
    conn = sqlite3.connect("inventory.db")
    return conn
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER,
        price REAL
    )
    """)

    conn.commit()
    conn.close()
def add_product(name, quantity, price):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?,?,?)",(name, quantity, price))
    
    conn.commit()
    conn.close()

def view_product():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    
    conn.close()
    return products
def update_name(product_id, new_name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET name = ? WHERE id = ?",
        (new_name, product_id)
    )

    conn.commit()
    conn.close()
def update_quantity(product_id, new_quantity):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET quantity = ? WHERE id = ?",
        (new_quantity, product_id)
    )

    conn.commit()
    conn.close()
def update_price(product_id, new_price):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (new_price, product_id)
    )

    conn.commit()
    conn.close()
def update_all(product_id, name, quantity, price):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE products
        SET name = ?, quantity = ?, price = ?
        WHERE id = ?
        """,
        (name, quantity, price, product_id)
    )

    conn.commit()
    conn.close()
def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    conn.commit()
    conn.close()
def get_low_stock(threshold=10):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE quantity <= ?",
        (threshold,)
    )

    low_stock_items = cursor.fetchall()
    conn.close()
    return low_stock_items