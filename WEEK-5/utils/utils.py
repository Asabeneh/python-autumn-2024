import re 
import pprint
import os 
import random 

from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, punctuation, octdigits
from random import choice

alpha_numberic = ascii_letters + digits

def generate_hexa_color ():
    hexa_color = '#'
    for _ in range(6):
        letter = choice(hexdigits)
        hexa_color += letter
    return hexa_color 

