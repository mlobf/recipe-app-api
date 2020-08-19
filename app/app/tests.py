from django.test import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test that two numbers added together"""
        self.assertEqual(add(3,8), 11)


    def test_subtract_numbers(self):
        """This test will subtract two numbers"""
        self.assertEqual(subtract(5,11),6)

