def find_word_count(string):
        string_list = string.split()
        word_count = len(string_list)
        return word_count

def get_char_count(string):
    char_dict = {}
    lowercase_string = string.lower()
    for char in lowercase_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
	return dict["num"]

def sort_dict(dict):
	dict_list = []
	for key, value in dict.items():
		temp_dict = {"char": key, "num": value}
		dict_list.append(temp_dict)
	dict_list.sort(reverse=True, key=sort_on)
	return dict_list
