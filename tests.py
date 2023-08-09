import unittest
from unittest.mock import Mock, patch
from flask import Flask
from api import search_handler


class TestSearchHandler(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.add_url_rule(
            "/search", "search_handler", search_handler, methods=["GET"]
        )
        self.client = self.app.test_client()

    @patch("db_connection.create_connection")
    def test_search_handler_with_results(self, mock_create_connection):
        mock_cursor = Mock()
        result = mock_cursor.fetchall.return_value = [
            [7, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [17, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [27, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [37, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [47, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [57, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [67, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [77, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [87, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [97, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [107, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [117, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [127, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [137, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [147, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [157, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [167, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [177, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [187, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [197, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
            [207, "artur.cmp@gmail.com", "Campo", "artur.cmp@gmail.com"],
        ]
        mock_create_connection.return_value.__enter__.return_value.cursor.return_value = (
            mock_cursor
        )

        response = self.client.get("/search?query=Campo")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, result)

    @patch("db_connection.create_connection")
    def test_search_handler_no_results(self, mock_create_connection):
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = []
        mock_create_connection.return_value.__enter__.return_value.cursor.return_value = (
            mock_cursor
        )

        response = self.client.get("/search?query=Jonny")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, [])


if __name__ == "__main__":
    unittest.main()
