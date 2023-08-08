from flask import Flask, request, jsonify

from DBConnection import create_connection

app = Flask(__name__)


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
