import sys

def get_book_text(path):
	with open(path) as f:
		file_content = f.read()
		return file_content


def word_count(): 
	words = get_book_text(sys.argv[1]).split()
	total_words = len(words)
	return total_words

def char_count():
	lower = get_book_text(sys.argv[1]).lower()
	count_char = {}
	for i in set(lower):
		count_char[i] = lower.count(i)
			
	return count_char

def sort_chars():
    char_dict = char_count()  
    chars_list = []
    
    for char, count in char_dict.items():
        chars_list.append({"char": char, "num": count})
    
    chars_list.sort(key=lambda x: x["num"], reverse=True)
    
    return chars_list
