# FluidMusic
# pygame_wrapper.py

# Description: This file is a function wrapper for
# the pygame library into the Song class

import pygame
import sys
import msvcrt

pygame.init()
pygame.mixer.init()
	
class Song:
	song_state = {0: "Stopped", 1: "Playing", 2: "Paused"}
	volume_step = 0.02 # 1/50 = 0.02 (MAX vol is 50, MIN is 0)
	
	#Initialization
	def __init__(self, path, name, artist, length, volume):
		self.path = path
		self.name = name
		self.artist = artist
		self.length = length
		self.status = 0
		self.loaded = False
		if(volume >= 0.0 and volume <= 1.0):
			pygame.mixer.music.set_volume(volume)
		else:
			print("Value for volume is invalid (0.0-1.0)")
		
	# Mutators
	def set_path(self, path):
		self.path = path
	def set_name(self, name):
		self.name = name
	def set_artist(self, artist):
		self.artist = artist
	def set_length(self, length):
		self.length = length
	def set_status(self, status):
		if(status >= 0 and status <= 2):
			self.status = status
		else:
			print("Value for status is invalid (0-2)")
	def set_loaded(self, loaded):
		self.loaded = loaded
	def set_position(self, position):
		if(position <= self.length and position >= 0):
			pygame.mixer.music.set_pos(position)
		else:
			print("Value for position is invalid (0-" + self.length + ")")
	def set_volume(self, volume):
		if(volume >= 0.0 and volume <= 1.0):
			pygame.mixer.music.set_volume(volume)
		else:
			print("Value for volume is invalid (0.0-1.0)")
			
	# Accessors
	def get_path(self):
		return self.path
	def get_name(self):
		return self.name
	def get_artist(self):
		return self.artist
	def get_length(self):
		return self.length
	def get_status(self):
		return self.status
	def get_loaded(self):
		return self.loaded
	def get_position(self):
		return pygame.mixer.music.get_pos()
	def get_volume(self):
		return pygame.mixer.music.get_volume()
		
	# Base wrappings	
	def load(self):
		try: 
			pygame.mixer.music.load(self.path)
			self.loaded = True
			self.status = 0
		except:
			print("Media could not be loaded: " + self.path)
			self.loaded = False
	def start(self):
		if(self.loaded):
			if(self.status == 0):
				pygame.mixer.music.play()
				self.status = 1	
			else:
				print("Media state (" + song_state[self.status] + ") is not suitable for starting")
		else:
			print("Media is not loaded")
	def restart(self):
		if(self.loaded):
			if(self.status != 0):
				pygame.mixer.music.rewind()
				self.status = 1 # TEST THIS to see if music starts when restarted from being paused/stopped
			else:
				print("Media state (" + song_state[self.status] + ") is not suitable for restarting")
		else:
			print("Media is not loaded")
	def pause(self):
		if(self.loaded):
			if(self.staus == 1):
				pygame.mixer.music.pause()
				self.status = 2
			else:
				print("Media state (" + song_state[self.status] + ") is not suitable for pausing")
		else:
			print("Media is not loaded")
	def unpause(self):
		if(self.loaded):
			if(self.status == 2):
				pygame.mixer.music.unpause()
				self.status = 1
			else:
				print("Media state (" + song_state[self.status] + ") is not suitable for resuming")
		else:
			print("Media is not loaded")
	def stop(self):
		if(self.loaded):
			if(self.status != 0):
				pygame.mixer.music.stop()
				self.status = 0
			else:
				print("Media state (" + song_state[self.status] + ") is not suitable for stopping")
		else:
			print("Media is not loaded")
		
	# Extra functionality
	def rewind(self, step, multiplier):
		if(self.loaded):
			position = self.get_position()
			position = position - (step * multiplier)
			if(position < 0):
				position = 0
			self.set_pos(position)
		else:
			print("Media is not loaded")
	def fast_foward(self, step, multiplier):
		if(self.loaded):
			position = self.get_position()
			position = position + (step * multiplier)
			if(position > length):
				position = length
			self.set_position(position)
		else:
			print("Media is not loaded")
	def increase_volume(self):
		volume = self.get_volume()
		volume = volume + volume_step
		if(volume > 1.0):
			volume = 1.0
		self.set_volume(volume)
	def descrease_volume(self):
		volume = self.get_volume()
		volume = volume - volume_step
		if(volume < 0.0):
			volume = 0.0
		self.set_volume(volume)
	def print_status(self):
		print("Media is currently " + song_state[self.status])

song = Song("./ZIPPER.mp3", "ZIPPER", "BROCKHAMPTON", 202000, 1.0)
		

'''
pygame.mixer.music.fadeout()
pygame.mixer.music.set_endevent()
pygame.mixer.music.get_endevent()
'''	