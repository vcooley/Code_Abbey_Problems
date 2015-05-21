__author__ = 'Vince'
"""
Create a structure such that only right and down moves are allowed.
Find number of paths from top left to bottom right corner.
Obstacles exist. I'm thinking create an array of shared edges
to iterate through. Where an obstacle exists, there is no edge between
itself and the point above or to the left of it.
It takes exactly (n-1) + (m-1) moves to reach the end
because you can't backtrack.

"""
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        self.hours = hours
        return super

milton = PartTimeEmployee("Matt")
print milton.full_time_wage(40)