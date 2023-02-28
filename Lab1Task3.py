year = int(input('Tell me the year: '))

if (year % 4) == 0:
    if (year % 100) == 0 and (year % 400) == 0:
        print('This is a високосный год')
    elif (year % 100) == 0 and (year % 400) != 0:
        print('This is not a високосный год')
    else:
        print('This is a високосный год')
else:
    print('This is not a високосный год')