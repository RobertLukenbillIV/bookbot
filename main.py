def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    words = count_Words(file_contents)
    chars_dict = character_count_instance(words)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{len_words(words)} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(word_count_dic):
    word_count_dic =  list(word_count_dic)
    word_count_dic.sort(reverse=True, key=sort_on)
    for word in word_count_dic:
        print(f"The '{word}' character was found {word_count_dic[word]} times")

def character_count_instance(text):
    dic1 = {}
    for word in text:
        lower_case_word = word.lower()
        for character in lower_case_word:
            if (character in dic1) == False:
                dic1[character] = 1
            else:
                dic1[character] += 1
    return dic1

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_Words(text):
    words = text.split()
    return words

def len_words(words):
    return len(words)
main()