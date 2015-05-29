__author__ = 'Vince'
"""
Create a structure such that only right and down moves are allowed.
Find number of paths from top left to bottom right corner.
Obstacles exist. I'm thinking create an array of shared edges
to iterate through. Where an obstacle exists, there is no edge between
itself and the point above or to the left of it.
For an array with edge lengths n and m, it takes exactly
(n-1) + (m-1) moves to reach the end because you can't backtrack.

"""

