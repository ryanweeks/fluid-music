import sys
import pygame

def man():
	for c in command_list:
		print(c, str(command_list[c]))

print("Welome to Fluid Music")

command_list = {"man": man}

while True:
	command = input("Enter command (\"man\" for command list):")
	
	if command in command_list:
		command_list[command]()
	else:
		print("Command not found")