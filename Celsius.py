name = input('please input your name: ')
print('Hi!', name)

x = 5
print(x)
print(x == 5)
print(x != 5)
print(x > 2)
print(x < 2)
print(x >= 2)
print(x <= 2)

rain = input('Is it rainy today?(Y/N) ')
if rain == 'Y':
    print('You go out with an umbrella.')
    print('You buy a bag of potato chip.')
    print('You watch films at home.')

age = input('How old are you?')
age = int(age)
if age >= 20:
    print('You can vote.')

c = input('please input Celsius degree: ')
c = float(c)
f = c * 9 / 5 + 32
print('Fahreheit degree is ', f)
