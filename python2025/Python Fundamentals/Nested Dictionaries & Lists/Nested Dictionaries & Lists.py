x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

def iterateDictionary(some_list):
    for item in some_list:
        output = []
        for key, value in item.items():
            output.append(f"{key} - {value}")
        print(", ".join(output))

#test
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        if key_name in item:
            print(item[key_name])

#test
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

