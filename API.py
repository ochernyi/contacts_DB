from flask import Flask, jsonify, request
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


def search_contacts(query):
    """Function for fulltext searching contacts"""

    with create_connection().cursor() as cursor:
        cursor.execute(
            "SELECT * FROM contacts WHERE to_tsvector("
            "'simple', first_name || ' ' || last_name || ' ' || email) @@ plainto_tsquery('simple', %s)",
            (query,),
        )
        results = cursor.fetchall()
        return results


@app.route("/search", methods=["GET"])
def search_handler():
    query = request.args.get("query", "")
    results = search_contacts(query)

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
