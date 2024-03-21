#1/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init_with_args(self):
        base_model = BaseModel(id='123', created_at='2022-01-01T12:00:00.000')
        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at, datetime.datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(base_model.updated_at, datetime.datetime(2022, 1, 1, 12, 0, 0))

    def test_init_without_args(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)

    def test_to_dict(self):
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
