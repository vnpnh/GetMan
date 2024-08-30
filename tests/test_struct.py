from unittest import TestCase
import json

from getman import Struct


class TestStruct(TestCase):
    def setUp(self):
        self.simple_data = {'name': 'John', 'age': 30, 'city': 'New York'}
        self.nested_data = {
            'name': 'John',
            'address': {'street': '123 Main St', 'zip_code': '10001'}
        }
        self.simple_struct = Struct(**self.simple_data)
        self.nested_struct = Struct(**self.nested_data)

    def test_attribute_access(self):
        self.assertEqual(self.simple_struct.name, self.simple_data.get('name'))
        self.assertEqual(self.simple_struct.age, self.simple_data.get('age'))
        self.assertEqual(self.simple_struct.city, self.simple_data.get('city'))
        self.assertIsNone(self.simple_struct.country)

    def test_nested_struct_attribute_access(self):
        self.assertIsInstance(self.nested_struct.address, Struct)
        self.assertEqual(self.nested_struct.name, self.nested_data.get('name'))
        self.assertEqual(self.nested_struct.address.street, self.nested_data.get('address').get('street'))
        self.assertEqual(self.nested_struct.address.zip_code, self.nested_data.get('address').get('zip_code'))
        self.assertIsNone(self.nested_struct.address.city)

    def test_dynamic_attribute_assignment(self):
        self.simple_struct.new_attr = 'new_value'
        self.assertEqual(self.simple_struct.new_attr, 'new_value')

        self.simple_struct.name = 'Jane'
        self.assertEqual(self.simple_struct.name, 'Jane')

    def test_delete_attribute(self):
        self.assertEqual(self.simple_struct.city, self.simple_data.get('city'))
        del self.simple_struct.city
        self.assertIsNone(self.simple_struct.city)

    def test_to_json(self):
        expected_json = json.dumps(self.simple_data)
        actual_json = json.loads(self.simple_struct.to_json())
        expected_dict = json.loads(expected_json)
        self.assertEqual(actual_json, expected_dict)

    def test_invalid_key_access(self):
        self.assertIsNone(self.nested_struct.address.citys)

    def test_setitem_and_delitem(self):
        self.simple_struct['new_attr'] = 'new_value'
        self.assertEqual(self.simple_struct.new_attr, 'new_value')

        del self.simple_struct['new_attr']
        self.assertIsNone(self.simple_struct.new_attr)

