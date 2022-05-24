import unittest
from app import app
import requests

class ShopBridgeTest(unittest.TestCase):

    def setUp(self) :
         self.apiurl_list = "http://localhost:5000/api/products"
         self.apiurl_create = "http://localhost:5000/api/product/add"
         self.apiurl_update = "http://localhost:5000/api/product/update"
         self.apiurl_delete = "http://localhost:5000/api/product/delete"

         self.create_data = {
            "description": "Smart Phone",
            "name": "Redmi phone ",
            "price": 18000,
            "quantity": 100,
        }
         self.update_data = {
            "description": "Smart Phone 2",
            "name": "Redmi phone ",
            "price": 18500,
            "quantity": 100,
            "pid":13
        }

    # Test againts te status code 200 - Success http response
    def test_list(self):
        
        resp = requests.get(self.apiurl_list)
        status_code = resp.status_code
        self.assertEqual(status_code,200)

    def test_create_product(self):
        resp = requests.get(self.apiurl_create,json=self.create_data)
        status_code = resp.status_code
        self.assertEqual(status_code,200)

    def test_update_product(self):
        resp = requests.get(self.apiurl_update,json=self.update_data)
        status_code = resp.status_code
        self.assertEqual(status_code,200)    


if __name__== '__main__':
    unittest.main()
