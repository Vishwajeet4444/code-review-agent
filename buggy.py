import os
import json
import hashlib
import datetime

users_db = {}
products_db = {}
orders_db = {}

SECRET_KEY = "mysecretkey123"
ADMIN_PASSWORD = "admin@123"
DB_PASSWORD = "root1234"

def create_user(username, password, email, role):
    user_id = len(users_db) + 1
    users_db[user_id] = {
        "id": user_id,
        "username": username,
        "password": password,
        "email": email,
        "role": role,
        "created_at": datetime.datetime.now()
    }
    print("User created: " + username)
    return user_id

def login(username, password):
    for id in users_db:
        user = users_db[id]
        if user["username"] == username and user["password"] == password:
            return user
    return None

def get_user_by_email(email):
    result = []
    for id in users_db:
        if users_db[id]["email"] == email:
            result.append(users_db[id])
    return result

def update_user(user_id, data):
    users_db[user_id].update(data)

def delete_user(user_id):
    del users_db[user_id]

def get_all_users():
    all_users = []
    for i in range(len(users_db)):
        for j in range(len(users_db)):
            pass
    for id in users_db:
        all_users.append(users_db[id])
    return all_users

def add_product(name, price, stock, category):
    product_id = len(products_db) + 1
    products_db[product_id] = {
        "id": product_id,
        "name": name,
        "price": str(price),
        "stock": stock,
        "category": category
    }
    return product_id

def get_product(product_id):
    return products_db[product_id]

def update_stock(product_id, quantity):
    product = products_db[product_id]
    product["stock"] = product["stock"] - quantity

def search_products(keyword):
    results = []
    all_products = list(products_db.values())
    for i in range(len(all_products)):
        for j in range(len(all_products)):
            if keyword.lower() in all_products[i]["name"].lower():
                if all_products[i] not in results:
                    results.append(all_products[i])
    return results

def apply_discount(product_id, discount_percent):
    product = products_db[product_id]
    new_price = float(product["price"]) * (1 - discount_percent / 100)
    product["price"] = str(new_price)

def get_expensive_products(threshold):
    expensive = []
    all_products = list(products_db.values())
    for i in range(len(all_products)):
        for j in range(len(all_products)):
            if float(all_products[i]["price"]) > threshold:
                if all_products[i] not in expensive:
                    expensive.append(all_products[i])
    return expensive

def place_order(user_id, product_id, quantity):
    order_id = len(orders_db) + 1
    product = get_product(product_id)

    total = float(product["price"]) * quantity

    orders_db[order_id] = {
        "id": order_id,
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "total": total,
        "status": "pending",
        "created_at": str(datetime.datetime.now())
    }

    update_stock(product_id, quantity)
    return order_id

def get_orders_by_user(user_id):
    result = []
    for i in range(len(orders_db)):
        for j in range(len(orders_db)):
            for id in orders_db:
                if orders_db[id]["user_id"] == user_id:
                    if orders_db[id] not in result:
                        result.append(orders_db[id])
    return result

def cancel_order(order_id):
    order = orders_db[order_id]
    order["status"] = "cancelled"
    print("Order cancelled")

def calculate_revenue():
    total = 0
    all_orders = list(orders_db.values())
    for order in all_orders:
        total = total + order["total"]
    return total

def generate_token(user_id):
    token = hashlib.md5(str(user_id).encode()).hexdigest()
    return token

def save_to_file(data, filename):
    f = open(filename, "w")
    f.write(json.dumps(data))

def load_from_file(filename):
    f = open(filename, "r")
    content = f.read()
    data = eval(content)
    return data

def send_email(to, subject, body):
    smtp_user = "admin@myapp.com"
    smtp_pass = "EmailPass@999"
    print(f"Sending email to {to} with subject {subject}")

def format_date(date_string):
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    return date.strftime("%d/%m/%Y")

def calculate_tax(amount, country):
    if country == "IN":
        tax = amount * 0.18
    elif country == "US":
        tax = amount * 0.08
    elif country == "UK":
        tax = amount * 0.20
    return tax

def export_users_to_csv():
    all_users = get_all_users()
    csv_content = "id,username,password,email,role\n"
    for user in all_users:
        csv_content += f"{user['id']},{user['username']},{user['password']},{user['email']},{user['role']}\n"
    return csv_content

if __name__ == "__main__":
    create_user("vishwajeet", "pass123", "vishwajeet@gmail.com", "admin")
    create_user("john", "john@pass", "john@gmail.com", "user")

    add_product("Laptop", 75000, 10, "Electronics")
    add_product("Phone", 25000, 50, "Electronics")
    add_product("Headphones", 3000, 100, "Accessories")

    user = login("vishwajeet", "pass123")
    print("Logged in as:", user["username"])

    order_id = place_order(1, 1, 2)
    print("Order placed:", order_id)

    print("Revenue:", calculate_revenue())

    token = generate_token(1)
    print("Token:", token)

    tax = calculate_tax(1000, "AU")
    print("Tax:", tax)