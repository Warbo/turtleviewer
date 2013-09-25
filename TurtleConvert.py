import time
import turtle
import pygame
import sys
pygame.init()

def flip_surface(to_flip):
	new_surface = pygame.Surface((to_flip.get_width(), to_flip.get_height()))
	to_flip_array = pygame.surfarray.pixels3d(to_flip)
	new_surface_array = pygame.surfarray.pixels3d(new_surface)
	for r, row in enumerate(to_flip_array):
		for c, element in enumerate(row):
			new_surface_array[r][c] = to_flip_array[-1*(r+1)][c]
	return new_surface_array

def get_neighbours(pixel):
	to_return = [(pixel[0] + 1, pixel[1]), \
		(pixel[0] - 1, pixel[1]), \
		(pixel[0], pixel[1] + 1), \
		(pixel[0], pixel[1] - 1)]
	return to_return

def get_moves(pixel_array):
	moves = []
	array_copy = pixel_array[:]
	current_pos = array_copy.pop()
	moves.append('#!/usr/bin/env python')
	moves.append('import time')
	moves.append('import turtle')
	moves.append('turtle.setup()')
	moves.append('turtle.up()')
	moves.append('turtle.goto('+str(current_pos[0])+','+str(current_pos[1])+')')
	moves.append('turtle.down()')
	while len(array_copy) > 0:
		#print str(len(array_copy))
		possibilities = get_neighbours(current_pos)
		found_neighbour = False
		for poss in possibilities:
			if poss in array_copy:
				moves.append('turtle.goto('+str(poss[0])+','+str(poss[1])+')')
				current_pos = poss
				array_copy.remove(poss)
				found_neighbour = True
		if not found_neighbour:
			moves.append('turtle.up()')
			current_pos = array_copy.pop()
			moves.append('turtle.goto('+str(current_pos[0])+','+str(current_pos[1])+')')
			moves.append('turtle.down()')
	moves.append('while True:')
	moves.append('	time.sleep(1)')
	return moves

surface = pygame.image.load(sys.argv[1])

surface_array = flip_surface(surface)

remaining_coords = []

for r, row in enumerate(surface_array):
	for c, element in enumerate(row):
		if int(element[0]) + int(element[1]) + int(element[2]) < 3*128:
			remaining_coords.append((r,c))
			element[0] = element[1] = element[2] = 0
		else:
			element[0] = element[1] = element[2] = 255

outfile = open(sys.argv[2], 'w')

commands = get_moves(remaining_coords)

for line in commands:
	outfile.write(line+'\n')
outfile.close()
