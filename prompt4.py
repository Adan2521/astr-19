import sys

class Turtle:

	def describe(self):
		print("My Favotire animal is a turtle.")
		print(f"Length of arms in cm = {self.len_of_arms}")
		print(f"Length of the legs in cm = {self.len_of_legs}")
		print(f"Number of eyes = {self.num_eyes}")
		print(f"Does it have a tail = {self.tail}")
		print(f"Is it a furry? = {self.furry}")

	def __init__(self,len_of_arms, len_of_legs, num_eyes, tail, furry):
		self.len_of_arms = len_of_arms
		self.len_of_legs = len_of_legs
		self.num_eyes = num_eyes
		self.tail = tail
		self.furry = furry
if __name__ == "__main__":
	turtle = Turtle(5.0, 7.5, 2, True, False)
	turtle.describe()


