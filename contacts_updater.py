import os
import requests
import schedule
import time
import psycopg2

from db_connection import create_connection

from dotenv import load_dotenv

load_dotenv()


def update_contacts_from_nimble():
    """Function for updating contacts every day using schedule library"""

    url = "https://api.nimble.com/api/v1/contacts"
    headers = {"Authorization": os.getenv("API_KEY")}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        contacts = response.json()

        conn = create_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    for contact in contacts["resources"]:
                        first_name = contact.get("first name")
                        last_name = contact.get("last name")
                        email = contact.get("email").split(",")[0]
                        cursor.execute(
                            "INSERT INTO contacts(first_name, last_name, email) VALUES(%s, %s, %s)",
                            (first_name, last_name, email),
                        )
                    conn.commit()
            except psycopg2.Error as e:
                print("Error inserting contacts:", e)
                conn.rollback()
            finally:
                conn.close()

    except requests.exceptions.RequestException as e:
        print("Error fetching contacts from Nimble API:", e)


schedule.every().day.at("03:00").do(update_contacts_from_nimble)

while True:
    schedule.run_pending()
    time.sleep(1)
