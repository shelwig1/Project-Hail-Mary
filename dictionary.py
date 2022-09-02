#dictionary

"""
Do we need a bespoke data structure or will the built in work?

-string of cords, but the order doesn't matter - sets of chords
-meaning or meanings
Dictionary should suffice for this

"""

#save and load dictionary
import json
import os.path
from pprint import pprint

class dictionary:
	def __init__(self):
		self.dictionary = {}

		if os.path.isfile("dict_save.json"):
			with open("dict_save.json", "r") as f:
				self.dictionary = json.load(f)

				#exception handling for improper exiting
		else:
			f = open("dict_save.json", 'x')
			f.close()

	def save(self):
		with open('dict_save.json', 'w') as f:
			json.dump(self.dictionary, f)

	def add(self, chords, meaning):
		if chords not in self.dictionary:
			self.dictionary[chords] = meaning
		else:
			self.dictionary[chords].extend(meaning)

	def remove(self):
		#do i want to remove one possible meaning for this chord pair?
		#if we have multiple potential meanings, list them and ask for clarification
			#do we want to frag one in particular or all of them?
		pass

	def edit(self):
		pass

	#What sort of displays will I need?
	def displayword(self,chords):
		return self.dictionary[chords]

	def displaydict(self):
		pprint (self.dictionary)

	
