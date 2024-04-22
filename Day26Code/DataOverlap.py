def file_to_list(filename):
    with open(filename, 'r') as file:
        # Create an empty list to store the lines
        num_list1 = []

        # Iterate over the lines of the file
        for line in file:
            # Remove the newline character at the end of the line
            line = line.strip()

            # Append the line to the list
            num_list1.append(int(line))
    return num_list1

# above function can also be done using readlines() after opening the files
# with open('File.txt') as file1
# list1 = file1.readlines()

num1 = file_to_list('File1.txt')
num2 = file_to_list('File2.txt')

result = [num for num in num1 if num in num2]

#result = [num1[num] for num in range(len(num1)) for n in range(len(num2)) if num1[num] == num2[n]]

# result = [num1[num] for num in range(len(num1)) for n in range(len(num2)) if num1[num] == num2[n]] in above line
# first for loop is for num1 to loop each item and 2nd for loop is to loop num 2, condition checks num1 iteration
# against all items of num2

print(result)
