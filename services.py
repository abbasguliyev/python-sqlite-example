from database import get_db_connection

def register_user(first_name, last_name, username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (first_name, last_name, username, password) VALUES (?,?,?,?)', 
                   (first_name, last_name, username, password))
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def get_all_cars():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()
    conn.close()
    return cars

def add_car(name, color, rental_price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO cars (name, color, rental_price) VALUES (?, ?, ?)',
        (name, color, rental_price)
    )
    conn.commit()
    conn.close()

def update_car(car_id, name, color, rental_price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE cars SET name = ?, color = ?, rental_price = ? WHERE id = ?',
        (name, color, rental_price, car_id)
    )
    conn.commit()
    conn.close()

def delete_car(car_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cars WHERE id = ?', (car_id,))
    conn.commit()
    conn.close()