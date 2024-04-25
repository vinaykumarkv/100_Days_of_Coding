import pandas

code_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in code_data_frame.iterrows()}

# user_list = [*user_input]
# result = [value for i in user_list for (key, value) in code_dict.items() if i == key]

# is_true = True
# while is_true:
#     user_input = input("please provide your input for conversion into phonetic code words: ").upper()
#     try:
#         result = [code_dict[letter] for letter in user_input]
#         print(result)
#         is_true = False
#
#     except KeyError:
#         print("Sorry. only letters in the alphabets please.")
#
#     else:
#         print(result)

def code_gen():
    user_input = input("please provide your input for conversion into phonetic code words: ").upper()
    try:
        result = [code_dict[letter] for letter in user_input]
        print(result)

    except KeyError:
        print("Sorry. only letters in the alphabets please.")
        code_gen()
    else:
        print(result)

code_gen()

