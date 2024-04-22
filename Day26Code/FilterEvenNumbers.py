list_of_strings = input().split(',')

list_of_integers = [int(i) for i in list_of_strings]

result = [i for i in list_of_integers if i % 2 == 0]

print(result)
