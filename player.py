# FluidMusic
# player.py

# Description: This file is intended to include the class
# structures and function definitions for the main commands
# of the program

import pygame
import sys
import msvcrt

paused = True

pygame.mixer.init()

while True:
	char = msvcrt.getch()
	
	if(char == b'\x1b'): #escape key
		print("Exiting Player")
		exit(0)
		
	elif(char == b'l' or char == b'L'): #l or L
		song = input("Enter the path of the music file: ")
		if(pygame.mixer.music.get_busy() == True):
			pygame.mixer.music.stop() #stops song if playing
		pygame.mixer.music.load(song) #loads the song
		print("Now playing, " + song)
		pygame.mixer.music.play() #plays the song
		paused = False
		
	elif(char == b' '): #space bar
		#checks if playing or not
		if(paused):
			print("Unpausing song")
			pygame.mixer.music.unpause() #unpauses if playing
			paused = False
		else:
			print("Pausing song")
			pygame.mixer.music.pause() #resumes if paused
			paused = True
			
	elif(char == b's' or char == b'S'): #s or S
		print("Stopping song")
		pygame.mixer.music.stop()
		paused = True
	
	elif(char == b'p' or char == b'P'): #p or P
		print("Playing song")
		pygame.mixer.music.play()
		paused = False
		
	elif(char == b'r' or char == b'R'): #r or R
		print("Restarting song")
		pygame.mixer.music.rewind()
		paused = False
		
	elif(char == b'q' or char == b'Q'): #q or Q
		song = input("Enter the path of the music file to add to the queue: ")
		pygame.mixer.music.queue(song)
		print(song + " added to queue")
		
	elif(char == b']'): #]
		volume = pygame.mixer.music.get_volume()
		if(volume < 1):
			volume = volume + .05
		pygame.mixer.music.set_volume(volume)
	
	elif(char == b'['): #[
		volume = pygame.mixer.music.get_volume()
		if(volume > 0):
			volume = volume - .05
		pygame.mixer.music.set_volume(volume)