import json

from tests.BaseCase import BaseCase

class TestUserLogin(BaseCase):

    def test_successful_login(self):
        # Given
        email = "paurakh011@gmail.com"
        password = "mycoolpassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        product_payload = {
            "name": "Superduperproduct",
            "price": 50012.23,
            "quantity": 5000
        }
        # When
        response = self.app.post('/api/products',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(product_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)