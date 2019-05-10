# Task 1 easy
# a = 1
# b = 2
# c = 1.23
# d = 'hello'
# e = False
# print(e)
# f = input('What is your name?')
# print(f)

# Task 2 easy
# number = int(input('Input number'))
# print(number + 2)

# Task 3 easy
# old = int(input('How old are you?'))
# if old >= 18:
#     print('Access is permit')
# else:
#     print('Sorry, using this resource is permited only 18+')

# Task 1 normal
# a = 1
# while a > 0 and a < 10:
#     a = int(input('Input the number bigger 0 and less 10'))
#     if a >= 10:
#         print('The number is very big. Valid range is 1 to 9. Try again.')
#     elif a <= 0:
#         print('The number is negative. Valid range is 1 to 9. Try again.')
#     else:
#         b = a ** 2
#         print(b)

# Task 2 normal
# a = int(input('Input value for var a'))
# b = int(input('Input value for var b'))
# a = a + b
# b = a - b
# a = a - b
# a, b = b, a
# print(a, b)

# Task 1 hard
anketa = {
    'name': input('Input your name'),
    'surname': input('Input your surname'),
    'weight': int(input('Input your weight')),
    'age': int(input('How old are you?'))
}
if anketa['age'] < 30 and 120 < anketa['weight'] < 50:
    print('You in good state!')
elif 40 > anketa['age'] >= 30 and (120 < anketa['weight'] or 50 > anketa['weight']):
    print('You need begin right life')
elif anketa['age'] >= 40 and (50 > anketa['weight'] or 120 > anketa['weight']):
    print('You need a medical examination')
else:
    print('Good bye!')