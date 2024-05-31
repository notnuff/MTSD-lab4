import unittest
from app import app

class FlaskRoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_solve_post(self):
        data = {'cell-0-0': '5', 'cell-0-1': '3', 'cell-1-0': '6', 'cell-1-3': '1', 'cell-1-4': '9', 'cell-1-5': '5'}
        response = self.app.post('/solve', data=data)
        self.assertEqual(response.status_code, 200)

    def test_custom_get(self):
        response = self.app.get('/custom')
        self.assertEqual(response.status_code, 200)

    def test_custom_post(self):
        data = {'cell-0-0': '5', 'cell-0-1': '3', 'cell-1-0': '6', 'cell-1-3': '1', 'cell-1-4': '9', 'cell-1-5': '5'}
        response = self.app.post('/custom', data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
