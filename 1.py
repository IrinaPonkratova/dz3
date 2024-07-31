# Дан список повторяющихся элементов. Вернуть список с
# дублирующимися элементами. В результирующем списке не должно
# быть дубликатов.
COUNT = 1
data = [42, 73, 5, 42, 2, 3, 5, 7, 73, 42]
new_data = []
for i in set(data):
    if data.count(i) > COUNT:
        new_data.append(i)

print(f'список с повторяющимися элементами :\n{new_data}')