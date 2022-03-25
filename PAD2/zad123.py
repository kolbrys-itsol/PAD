# zad 1
fun1 = lambda x: x + 15
fun2 = lambda x, y: x * y

print('Zadanie 1')
print('fun1')
print(fun1(5))
print('fun2')
print(fun2(5, 5))

# zad 2
dicts = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
         {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
fun3 = sorted(dicts, key=lambda val: val['model'])
print('Zadanie 2 (sortujemy po modelu)')
print(fun3)

# zad 3
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fun4 = lambda vals: [(val ** 2, val ** 3) for val in vals]
print('Zadanie 3')
print(fun4(values))
