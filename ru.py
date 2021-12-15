import os
import sys
import re
import rucom

ru_json = {"cls": rucom.Ru.cls, "file": __file__}
ru_class = {"ru": ru_json}

varibles_json = {}
current_line=1
def yorumla(code):
		space_count = code.count(" ")
		line_count = code.count("\n")
		if line_count == 0:
			line_count+=1

		for i in range(line_count):
			line=code.splitlines()[i]
			current_line=i
			for x in range(len(line.split())):
				try:
					if line.split()[x] in ru_class:
						if line.split()[x+1] in ru_class[line.split()[x]]:
							if callable(ru_class[code.split()[x]][code.split()[x+1]]) is True:
								eval("ru_class[code.split()[x]][code.split()[x+1]]"+"()")
							elif type(ru_class[code.split()[x]][code.split()[x+1]]) is str or int or float:
								print(ru_class[code.split()[x]][code.split()[x+1]])
						else:
							print(f"Arg Error: arg ({line.split()[x+1]}) not found line:{i+1}")
					elif line[0] == "#":
						pass
					elif line[0:2] == "//":
						pass
			
					else:
						#print(line.split().index(line.split()[x]))
						if not line.split().index(line.split()[x]) == 0:
							pass
						else:
							print(f"Error: {line.split()[x]} Not Found line: {i+1}")
				except IndexError:
					print(f"Arg Error: Empty arg in '{code.splitlines()[i]}' line:{i+1}")

try:
	if sys.argv[1] == "console":
		while True:
			a=input(">>")
			yorumla(a)
	elif sys.argv[1] == "-h" or "--help" or "help":
		print("""
Run <file>    Run file
console       Ru console
""")
	elif sys.argv[1] == "run":
		try:
			file=open(sys.argv[2], "r", encoding="utf8").read()
			yorumla(file)
		except IndexError:
			print(f"run required argument <file>")
	else:
		print("Argument Not Found -h for help")
except IndexError:
	print(f"Use: {__file__} -h for help")
