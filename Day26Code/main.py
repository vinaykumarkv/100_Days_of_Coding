import pandas

code_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in code_data_frame.iterrows()}
user_input = input("please provide your input for conversion into phonetic code words: ").upper()
# user_list = [*user_input]
# result = [value for i in user_list for (key, value) in code_dict.items() if i == key]
result = [code_dict[letter] for letter in user_input]
print(result)
