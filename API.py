from flask import Flask, jsonify
import psycopg2

from DBConnection import create_connection

app = Flask(__name__)


@app.route("/contacts", methods=["GET"])
def get_contacts():
    connect = create_connection()
    if connect:
        try:
            with connect.cursor() as cursor:
                cursor.execute("SELECT * FROM contacts;")
                rows = cursor.fetchall()

            contacts = [
                {
                    "id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                }
                for row in rows
            ]

            connect.close()

            return jsonify(contacts)

        except psycopg2.Error as e:
            print("Error executing query:", e)
            connect.close()

    return jsonify([])


if __name__ == "__main__":
    app.run(debug=True)
