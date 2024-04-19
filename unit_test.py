import unittest
from unittest.mock import MagicMock, patch
from user import fetch_data, created_data


#Ejercicio 7 prueba funcion add(a, b):
class MethodTest:
    def functionality(a,b):
        valors = sum([a, b])
        return valors

class TestStringMethods(unittest.TestCase):
    def test_correct(self):
        test = MethodTest.functionality(1,2)
        self.assertEqual(test, 3)
    
    def test_error(self):
        test = MethodTest.functionality(1,2)
        with self.assertRaises(AssertionError):
            self.assertEqual(test, 2)

#Ejercicio 8: test unittest.mock
class TestFetchData(unittest.TestCase):
    @patch('user.requests')
    def test_fetch_data_success_post(self, mock_requests):
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "Antonio",
            "age": 59,
            "has_children": 15,
            "gender": "Undefined",
            "full_name": "Antonio acevedo bolivar",
            "studies": "Any",
            "job": "searching",
            "id": 11
        }

        mock_requests.post.return_value = mock_response
        self.assertEqual(created_data()['name'], 'Antonio') 

    @patch('user.requests')
    def test_fetch_data_success_get(self, mock_requests):
        
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "Antonio",
            "age": 59,
            "has_children": 15,
            "gender": "Undefined",
            "full_name": "Antonio acevedo bolivar",
            "studies": "Any",
            "job": "searching",
            "id": 11
        }

        mock_requests.get.return_value = mock_response
        self.assertEqual(fetch_data(11)['name'], 'Antonio')
    
if __name__ == "__main__":
    unittest.main()