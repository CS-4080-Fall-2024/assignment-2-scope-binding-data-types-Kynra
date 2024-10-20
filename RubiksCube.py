import random

class RubiksCube:
    def __init__(self):
        # Initializing the Rubik's Cube with each face having a uniform color
        self.state = {
            'F': [['W' for _ in range(3)] for _ in range(3)],  # Front face (white)
            'B': [['Y' for _ in range(3)] for _ in range(3)],  # Back face (yellow)
            'L': [['G' for _ in range(3)] for _ in range(3)],  # Left face (green)
            'R': [['B' for _ in range(3)] for _ in range(3)],  # Right face (blue)
            'U': [['O' for _ in range(3)] for _ in range(3)],  # Top face (orange)
            'D': [['R' for _ in range(3)] for _ in range(3)],  # Bottom face (red)
        }

    #display cube
    def display(self):
        for face, grid in self.state.items():
            print(f"{face} face:")
            for row in grid:
                print(row)
            print()

    def rotate_face_clockwise(self, face):
        # Rotate a face 90 degrees clockwise
        self.state[face] = [list(reversed(col)) for col in zip(*self.state[face])]
    
    def rotate_face_counterclockwise(self, face):
        # Rotate a face 90 degrees counterclockwise (3 clockwise rotations)
        for _ in range(3):
            self.rotate_face_clockwise(face)

    def rotate_row(self, row, direction):
         # Rotating a row
        if direction == 'right':
            temp = self.state['F'][row]
            self.state['F'][row] = self.state['L'][row]
            self.state['L'][row] = self.state['B'][row]
            self.state['B'][row] = self.state['R'][row]
            self.state['R'][row] = temp
        elif direction == 'left':
            temp = self.state['F'][row]
            self.state['F'][row] = self.state['R'][row]
            self.state['R'][row] = self.state['B'][row]
            self.state['B'][row] = self.state['L'][row]
            self.state['L'][row] = temp

        # If rotating the top (row 0) or bottom (row 2), we need to rotate the U or D faces as well
        if row == 0:
            self.rotate_face_clockwise('U') if direction == 'right' else self.rotate_face_counterclockwise('U')
        elif row == 2:
            self.rotate_face_clockwise('D') if direction == 'right' else self.rotate_face_counterclockwise('D')

#initialize cube
cube = RubiksCube()
cube.rotate_row(0, 'right')
cube.rotate_row(1, 'left')
cube.rotate_row(2, 'right')
cube.display()

