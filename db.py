import sqlite3


def init_db():
    connection = sqlite3.connect('temp_and_press.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Temperatures
                  (date DATETIME, temp DOUB)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pressures
                  (date DATETIME, press DOUB)''')

    connection.commit()
    connection.close()


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('temp_and_press.db')
    except Exception as e:
        print(e)

    return conn


def add_temperature(conn, date, temp):
    sql = ''' INSERT INTO temperatures(date, temp)
              VALUES(?,?) '''
    curs = conn.cursor()
    curs.execute(sql, date, temp)
    conn.commit()


def add_pressure(conn, date, press):
    sql = ''' INSERT INTO pressures(date, press)
              VALUES(?,?) '''
    curs = conn.cursor()
    curs.execute(sql, date, press)
    conn.commit()


def select_temperature(conn, date):
    cur = conn.cursor()
    cur.execute("SELECT * FROM temperatures WHERE date>=?", (date,))
    return cur.fetchall()


def select_pressure(conn, date):
    cur = conn.cursor()
    cur.execute("SELECT * FROM pressures WHERE date>=?", (date,))
    return cur.fetchall()
