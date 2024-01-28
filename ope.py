

def odd_numbers(num):
    if num < 0:
        print('Negative numbers isnt allow ')
    else:
        i = 1
        array_impares = []
        while i<=num:
            array_impares.append(i) if i % 2 != 0 else None
            i += 1
        return array_impares

num = int(input("Please, write a number: "))
print(num)
num_odd = odd_numbers(num)
print(f'These are the odd numbers: {num_odd}') if num_odd != None else print('Someting gone wrong') 
