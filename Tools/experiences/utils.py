import re

"""
  numericalSort: sort in numerical order for data such as: filename, bla bla bla
"""
numbers = re.compile(r'(\d+)')
def numericalSort(value):
  parts = numbers.split(value)
  parts[1::2] = map(int, parts[1::2])
  return parts