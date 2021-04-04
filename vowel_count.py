def get_count(input_str):
    num_vowels = 0
    
    for vow in input_str:
        vow = vow.lower()
        if vow == '':
            return 0
        else:
            if vow == 'a' or vow == 'e' or vow == 'i' or vow == 'o' or vow == 'u':
                num_vowels += 1
            
    return num_vowels

get_string = input("Enter your string: ")

print(get_count(get_string))