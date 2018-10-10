from calculator import Calculator
import unittest
from time import sleep

class testAdd(unittest.TestCase):
	def setUp(self):
		print("start test")
		self.c = Calculator()

	def test_add_1(self):
		print("--- start test_add_1 ---")
		r_add_1 = self.c.add(3,5)
		self.assertEqual(r_add_1,8)
		print("--- end test_add_1 ---")
	def tearDown(self):
		print("end test")


if __name__ == '__main__':
	# unittest.main()
	unittest.main(verbosity=2)
	# suite = unittest.TestSuite()
	# suite.addTest(testAdd("test_add_1"))

	# runner = unittest.TextTestRunner()
	# runner.run(suite)

