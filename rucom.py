import os
import sys
class Ru:
	def cls():
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
	