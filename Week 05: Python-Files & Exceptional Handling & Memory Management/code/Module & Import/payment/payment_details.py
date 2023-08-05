
import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from course import course_details

def payment():
    print("This i my payment function")

course_details.course()