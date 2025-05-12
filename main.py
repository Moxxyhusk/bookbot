import sys
from stats import word_count, sort_chars


def main():
	
	if len(sys.argv) <= 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	print("============= Bookbot =============")
	print(f"Analysing book found at {sys.argv[1]}...")
	print("------------Word Count-------------")
	print(f"Found {word_count()} total words")
	print("----------Character Count----------")
	for char_dict in sort_chars():
		char = char_dict["char"]
		if char.isalpha():
			print(f"{char}: {char_dict['num']}")

	print("=============END====================")
	


main()


