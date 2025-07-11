import unittest
from flask import Flask, jsonify
from ..node import require_json  # adjust import if needed


class RequireJsonDecoratorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

        @self.app.route('/test', methods=['POST'])
        @require_json
        def test_route():
            return jsonify({"message": "Success"}), 200

        self.client = self.app.test_client()

    def test_rejects_non_json_request(self):
        response = self.client.post(
            '/test', data="not json", content_type='text/plain')
        self.assertEqual(response.status_code, 415)
        self.assertIn("Unsupported Media Type", response.get_json()["error"])

    def test_allows_json_request(self):
        response = self.client.post('/test', json={"key": "value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Success"})


if __name__ == '__main__':
    unittest.main()
