import os

import requests
import schedule
from schedule import repeat, every
from db_connection import create_connection

from dotenv import load_dotenv

load_dotenv()


@repeat(every().day)
def update_contacts_from_nimble():
    """Function for updating contacts every day
    using schedule library"""

    url = "https://api.nimble.com/api/v1/contacts"
    headers = os.getenv("HEADERS")

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        contacts = response.json()
        for contact in contacts["resources"]:
            first_name = contact.get("first name")
            last_name = contact.get("last name")
            email = contact.get("email").split(",")[0]
            with create_connection().cursor() as cursor:
                cursor.execute(
                    "INSERT INTO contacts(first_name, last_name, email) VALUES( % s, %s, %s)",
                    (first_name, last_name, email),
                )
                create_connection().commit()


if __name__ == "__main__":
    schedule.run_pending()
