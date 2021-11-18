# num = int(input('Enter number: '))

# if num > 0: print(num ** 2)
# elif num < 0: print(num ** (1/3))

names = ['Zafar', 'Abdulhakim', 'Bobur', 'Zakir']
ages = [21, 15, 17, 20, 21]

# print(names[0])
# print(names[-1])

# names += ['Amalmalik']
# print(names[-1])

# # names.append('Elbek')
# # names.append(23)
# # names.append(True)
# print(names.pop(0))

# print(len(names))
# names.remove('Bobur')
# ages.remove(21)

# names.reverse()
# names = names[::-1]
# print(names[0:7:2])
# print(names[::-1])

print(names)

hrs = int(input('Enter hours: '))
mins = int(input('Enter minutes: '))
delta = int(input('Enter delta hours: '))

if hrs >= 0 and 0 <= mins <= 59:
    new_hrs = (hrs + delta) % 24
    if new_hrs <= 9: new_hrs = '0' + str(new_hrs)
    if mins <= 9 : mins = '0' + str(mins)
    print(f'{new_hrs}:{mins}')
else: print('Error')

# b =1 

# a = 9 if b > 2 else 10

# print(a)