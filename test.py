# rules = []
# value1 = 1
# value2 = 2
# print(f'{{"match": {{"{value1}": "{value2}"}}}}')
myquery = {'bool': {'filter': []}}
description = 'test'
data = 'value'
test = f"{{'match': {{'{description}': '{data}'}}}},"
myquery['bool']['filter'].append(test)
myquery['bool']['filter'].append(test)
print(myquery['bool']['filter'])