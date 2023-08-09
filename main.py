import csv

from db_connection import create_connection

create_table_query = """
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100)
);
"""
with create_connection().cursor() as cursor:
    cursor.execute(create_table_query)
    create_connection().commit()

with open("Nimble_Contacts.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        first_name, last_name, email = row
        with create_connection().cursor() as cursor:
            cursor.execute(
                "INSERT INTO contacts ("
                "first_name, last_name, email"
                ") VALUES (%s, %s, %s)",
                (first_name, last_name, email),
            )
            create_connection().commit()
