# Семинар 1. Ввод-вывод, операторы ветвления.
# Задача №1. Решение в группах
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# n = int(input("Введите кол-во киллометров, которое Вы проезжаете за день: "))
# m = int(input("Введите общее расстояние: "))
# # n = 700
# # m = 750
# print((m + n - 1) // n)

# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

# countStudents1 = int(input("Введите кол-во учеников в 1-ом кабинете: "))
# countStudents2 = int(input("Введите кол-во учеников в 2-ом кабинете: "))
# countStudents3 = int(input("Введите кол-во учеников в 3-ом кабинете: "))
# part1 = (countStudents1 + 1) // 2
# part2 = (countStudents2 + 1) // 2
# part3 = (countStudents3 + 1) // 2
# print(part1 + part2 + part3)

# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input("Введите nomer ot golovy: "))
# j = int(input("Введите nomer vagona: "))
# if i == j:
#     print('ne uznat')
# else:
#     print(f'vsego vagonov: {i + j - 1}')

# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# n = int(input("Введите god: "))
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('YES')
# else: 
#     print('NO')

# def find_farthest_orbit(orbits):
#     list_of_elliptical_orbits = [i for i in orbits if i[0] != i[1]]
#     # print(list_of_elliptical_orbits)
#     list_of_areas = [i[0] * i[1] for i in list_of_elliptical_orbits]
#     # print(list_of_areas)
#     # max_area_index = list_of_areas.index(max(list_of_areas))
#     # print(max_area_index)
#     return list_of_elliptical_orbits[max_area_index[0]]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

def same_by(characteristic, objects):
    return sum(list(map(characteristic, objects))) == 0

values = [0, 2, 10, 6]
print(same_by(lambda x: x% 2, values))
if same_by(lambda x: x% 2, values):
    print('same')
else:
    print('dif')