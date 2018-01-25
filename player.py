import sys
import pygame

print("Welome to Fluid Music")

command_list = {"help": help}

while True:
	command = raw_input("Enter command (\"help\" for command list):")
	
	if command in command_list:
		command_list[command]()
	else:
		print("Command not found")