import unittest
import app 

class MyTest(unittest.TestCase):
	def test_my_function(self):
		self.assertEqual(app.my_function(1,1),2)
		self.assertEqual(app.my_function(2,3),5)
		self.assertEqual(app.my_function(4,5),9)
		self.assertEqual(app.my_function(8,9),17)

if __name__== '__main__':
	unittest.main() 
