import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def climbDirectory (height):
    for i in range(height):
        os.chdir('..')