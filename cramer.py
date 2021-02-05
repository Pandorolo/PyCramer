# 3x3 Cramer Resolution
# Made by @Pandorolo

import os
import re

# Clear Screen
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

# Ask and slice down all equations
matcher = re.compile(r'([+-]?[0-9]+)')
eq = []

for x in range(3):
	input_eq = str(input(f'Insert the {x+1} equation: '))
	eq.append([int(re.findall(matcher, input_eq)[y]) for y in range(4)])

a, b, c, d = 0, 1, 2, 3

# First determinant
determinant = (eq[0][a]*eq[1][b]*eq[2][c]) + (eq[0][b]*eq[1][c]*eq[2][a]) + (eq[0][c]*eq[1][a]*eq[2][b]) + ((eq[0][c]*eq[1][b]*eq[2][a]) + (eq[2][b]*eq[1][c]*eq[0][a]) + (eq[2][c]*eq[1][a]*eq[0][b]))*-1

# Determinant of X
determinant_x = (eq[0][d]*eq[1][b]*eq[2][c]) + (eq[0][b]*eq[1][c]*eq[2][d]) + (eq[0][c]*eq[1][d]*eq[2][b]) - (eq[0][c]*eq[1][b]*eq[2][d]) - (eq[0][b]*eq[1][d]*eq[2][c]) - (eq[0][d]*eq[1][c]*eq[2][b])

# Determinant of Y
determinant_y = (eq[0][a]*eq[1][d]*eq[2][c]) + (eq[0][d]*eq[1][c]*eq[2][a]) + (eq[0][c]*eq[1][a]*eq[2][d]) - (eq[0][c]*eq[1][d]*eq[2][a]) - (eq[0][d]*eq[1][a]*eq[2][c]) - (eq[0][a]*eq[1][c]*eq[2][d])

# Determinant of Z
determinant_z = (eq[0][a]*eq[1][b]*eq[2][d]) + (eq[0][b]*eq[1][d]*eq[2][a]) + (eq[0][d]*eq[1][a]*eq[2][b]) - (eq[0][d]*eq[1][b]*eq[2][a]) - (eq[0][d]*eq[1][a]*eq[2][d]) - (eq[0][a]*eq[1][d]*eq[2][b])

# Results
print(f'\nThe main determinant is: {determinant}')
print(f'X: {determinant_x}/{determinant} or {determinant_x/determinant}')
print(f'Y: {determinant_y}/{determinant} or {determinant_y/determinant}')
print(f'Z: {determinant_z}/{determinant} or {determinant_z/determinant}')