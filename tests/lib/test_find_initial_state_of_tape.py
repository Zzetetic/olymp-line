import unittest
from line.lib import find_initial_state_of_tape

class Test_case_1(unittest.TestCase):

	def test_1(self):
		initial_state_tape = [1, 4, 3, 2]
		end_state_tape = [1, 2, 3, 4]

		initial_state_tape_from_function = find_initial_state_of_tape(end_state_tape)
		
		self.assertEqual(initial_state_tape, initial_state_tape_from_function)
		
		

	def test_2(self):
		initial_state_tape = [1, 1, 1, 1]
		end_state_tape = [1, 1, 1, 1]

		initial_state_tape_from_function = find_initial_state_of_tape(end_state_tape)
		
		self.assertEqual(initial_state_tape, initial_state_tape_from_function)


	def test_3(self):
		initial_state_tape = [0, 0, 0, 0]
		end_state_tape = [0, 0, 0, 0]

		initial_state_tape_from_function = find_initial_state_of_tape(end_state_tape)
		
		self.assertEqual(initial_state_tape, initial_state_tape_from_function)


	def test_4(self):
		initial_state_tape = [5, 4, 3, 4]
		end_state_tape = [5, 4, 3, 4]

		initial_state_tape_from_function = find_initial_state_of_tape(end_state_tape)
		
		self.assertEqual(initial_state_tape, initial_state_tape_from_function)



if __name__ == '__main__':
    unittest.main() 
