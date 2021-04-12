import unittest
import click

from line.main import MyAppTest
from line.lib import find_initial_state_of_tape



class Test_case_1(unittest.TestCase):

	def test_1(self):
		with MyAppTest() as app:
			data = {'inital_tape' : [1, 2, 3, 4, 5]}
			app.render(data, "istate.jinja2")			
			if click.confirm('Test pass?', default=True):			
				self.assertTrue(True)
			else:
				self.assertTrue(False)
		

if __name__ == '__main__':
    unittest.main() 
