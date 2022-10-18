''' 
Задача: предложить улучшения кода для четырёх уже решённых задач из семинаров №№2 - 5 
# с помощью использования лямбд, filter, map, zip, enumerate, list comprehension
'''
# БЫЛО
# txt = 'Здесь есть абв, и даже много абв, абв, абв, абв. Ладно, остановимся'
# print(txt)

# txt_1 = 'А здесь уже нет абв, и даже много абв, абв, абв, абв. Ладно, остановимся'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# txt_1 = del_some_words(txt_1)
# print(txt_1)

#СТАЛО

# def del_w(origin_string: str, del_factor: str):
#     return " ".join(list(filter(lambda el: del_factor not in el, origin_string.lower().split())))


# test_string = "аБВ -влвы- сао б вба оабв абвввв"
# res = del_w(test_string, "абв")
# print(res)

#Task 2: ///////////////////////////////////////////////////////////

# БЫЛО

# from random import randint
# nums = []
# for i in range(10):
#     nums.append(randint (-10,10))
# print(nums)

# def numbers(nums):
#     count =0 
#     for element in nums:
#         count +=1
#     return count
# print('Колтчество элементов: ', numbers(nums))

# x = int(input('Введите позицию первого элемента: '))
# y = int(input('Введите позицию второго элемента: '))

# for i in range(len(nums)):
#     multi = nums[x -1]*nums[y - 1]
# print(f'Произведение элементов: {nums[x -1]} * {nums[y -1]} =', multi)

# СТАЛО

# def creat(n):
#     result = []
#     for i in range(-n, n + 1):
#         result.append(i)
#     return result


# def multi_new(a, b, n):
#     lst = [i for i in range(-n, n + 1)]
#     return lst[a - 1] * lst[b - 1]

# n = int(input("N: "))
# a = int(input("a: "))
# b = int(input("b: "))
# res_list = creat(n)
# print(f"a * b = {multi_new(a, b, n)}")

# Task 3: /////////////////////////////////////////////////////////

# БЫЛО

# from operator import index


# a = input('Введите любое число: ')
# sum = 0
# print(f'Вы ввели число {a}')

# for i in a:
#     if i != 0:
#         sum += int(i)
# print(f'Сумма чисел равна {sum} от введеного числа {a}')


# СТАЛО

# def sum_of_digits_new(num: str):
#     return sum([int(num[i]) for i in range(len(num)) if num[i].isdigit()])


# n = input()
# print(sum_of_digits_new(n))



# Task 4: ////////////////////////////////////////////////////////////////////////////////

# БЫЛО

# lst = [2, 3, 4, 5, 6]
# print(lst)
# result_lst = []
# for i in range((len(lst)+1)//2):
#     result_lst.append(lst[i]*lst[len(lst)-1-i])
# print(f'Произведение пар чисел списка равно: {result_lst}')

# СТАЛО

def multiply_of_pars_new(origin_lst: list):
    repeats = len(origin_lst) // 2 if len(origin_lst) % 2 == 0 else len(origin_lst) // 2 + 1
    return [origin_lst[i] * origin_lst[len(origin_lst) - (i + 1)] for i in range(repeats)]


test_1 = [2, 3, 4, 5, 6]
print(multiply_of_pars_new(test_1))
test_2 = [2, 3, 5, 6]
print(multiply_of_pars_new(test_2))