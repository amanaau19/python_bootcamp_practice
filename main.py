# 1. Напишите lambda функцию которая принимает число и возвращает его возведенным в степень двойки
# 2. Напишите lambda функцию которая принимает строку и возвращает её в верхнем регистре.
# 3. Напишите lambda функцию которая принимает строку и возвращает её в нижнем регистре.
# 4. Напишите lambda функцию которая принимает список или tuple и возвращает последний элемент.
# 5. Дан список: [1,2,3,4,5,6,834,123, 99,32, 644 ] с помощью спискового включения - сформируйте новый
# список только из чётных элементов.

power_of_2 = lambda x: x**2
print(power_of_2(7))

word_upper = lambda word: word.upper()
print(word_upper("hello"))

word_lower = lambda word: word.lower()
print(word_lower("WORLD"))

nums = [1, 3, 5, 7, 9, 11]
last_element = lambda list: list[-1]
print(last_element(nums))

nums_2 = [1,2,3,4,5,6,834,123,99,32,644]
even_nums = list(filter(lambda num: num % 2 == 0, nums_2))
print(even_nums)
