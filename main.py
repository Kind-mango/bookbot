import sys
from stats import find_word_count
from stats import get_char_count
from stats import sort_dict

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	text = get_book_text(sys.argv[1])
	word_count = find_word_count(text)
	print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {word_count} total words")

	char_dict = get_char_count(text)
	dict_list = sort_dict(char_dict)
	print("--------- Character Count -------")
	for item in dict_list:
		if item["char"].isalpha():
			print(f"{item["char"]}: {item["num"]}")
		else:
			continue

if __name__ == "__main__":
    main()
