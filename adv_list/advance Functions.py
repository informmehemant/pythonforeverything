list_of_chars = list('Hellooooo')

sum_of_elements = sum([1,2,3,4,5])


element_sum = [sum(pair) for pair in zip([1,2,3],[4,5,6])]
sorted_by_second = sorted(['hi','you','man'], key = lambda el: el[1])

sorted_by_key = sorted([
    {'name':'Bina', 'age': 34},
    {'name':'Andy', 'age': 18},
    {'name':'Zoe', 'age': 55},
    {'name':'Bina', 'age': 32},
],key=lambda el: el['age'])

print(sorted_by_key)