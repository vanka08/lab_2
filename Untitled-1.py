def get_unique_elements(input_list):
    """Возвращает список уникальных элементов из входного списка с использованием set."""

    return list(set(input_list))



# Примеры использования:

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = get_unique_elements(my_list)
print(unique_elements) # Вывод: [1, 2, 3, 4, 5] (порядок может отличаться)


my_list = ['apple', 'banana', 'apple', 'orange', 'banana']
unique_elements = get_unique_elements(my_list)
print(unique_elements) # Вывод: ['apple', 'banana', 'orange'] (порядок может отличаться)

my_list = [] # Пустой лист
unique_elements = get_unique_elements(my_list)
print(unique_elements) # Вывод: []



my_list = [1, 2, 3, 4, 5] # Уже уникальный лист
unique_elements = get_unique_elements(my_list)
print(unique_elements) # Вывод: [1, 2, 3, 4, 5] (порядок может отличаться)


