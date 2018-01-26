import sys
import pygame_wrapper

def man():
	for c in command_list:
		print(c)
		
def exit():
	sys.exit()
	
command_list = {"man": man, "exit": exit}

print("Welome to Fluid Music")

while True:
	command = input("Enter command (\"man\" for command list):")
	
	if command in command_list:
		command_list[command]()
	else:
		print("Command not found")