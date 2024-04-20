#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# Open the file in read mode

with open('./Input/Names/invited_names.txt', 'r') as file:
    # Create an empty list to store the lines
    lines = []

    # Iterate over the lines of the file
    for line in file:
        # Remove the newline character at the end of the line
        line = line.strip()

        # Append the line to the list
        lines.append(line)
print(lines)

for names in lines:
    with open('./Input/Letters/starting_letter.txt', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('[name]', names)

    # Write the file out again
    with open(f'./Output/ReadyToSend/{names}.txt', 'a') as file:
        file.write(filedata)
