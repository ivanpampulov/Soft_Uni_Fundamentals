import re

variables = input()
pattern = r'\b_([A-Za-z0-9]+)\b'

matches = re.findall(pattern, variables)

print(','.join(matches))