import unittest
from app import app

class ShopBridgeTest(unittest.TestCase):

    # def setUp(self) :
    #     pass

    # Test againts te status code 200 - Success http response
    def test_index(self):
        tester = app.test_client(self)
        resp = tester.get("/index")
        status_code = resp.status_code
        self.assertEqual(status_code,200)

if __name__== '__main__':
    unittest.main()
