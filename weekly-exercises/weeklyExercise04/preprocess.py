# ————————————————————————————————-------
#   Name: Zhiyuan Lu
#   ID: 1579050
#   CMPUT 274, Fall 2018
#
#   Weekly Exercise #4: Text Preprocessor
# ---------------------------------------
import string
import sys


def convert_to_lower():
    """ convert all the input words to lowercase words.

    :return:
        lowercase_words_list: return a list which contains all
                              the lowercase words.
    """
    lower_words_list = []
    # iterate each words in user-input list, convert these words to lowercase
    for char in input_list:
        lower_char = char.lower()
        lower_words_list.append(lower_char)
    return lower_words_list


def rm_punctuation(lower_words):
    """

    :param lower_words: a list which has converted each words to lowercase words from user_input_list
    :return:
            words_list: return a list which separates all the words to letters,
                        and removes all the punctuation in the list
    """
    # separate each words to letters
    words_list = list(" ".join(x for x in lower_words))
    # iterate each symbols in string.punctuation
    # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # if a symbol appears in words_list, remove this symbol
    for i in string.punctuation:
        while i in words_list:
            words_list.remove(i)

    return words_list


def rm_number(words_list):
    """

    :param words_list: a list which has separated each words to letters
                       converted to lowercase and remove all the punctuations

    :return:
            noNum_word_list: a list of words which removes all the numbers
                            (unless a token contains only numbers, keep this token)
    """
    noNum_word_list = []
    # join each letters to words, save the words in new_words_list
    new_words_list = "".join(words_list).split()
    # Iterate each words in new_words_list
    # if a string in this list contains only numbers,
    # append it directly to noNum_word_list
    for ele in new_words_list:
        if ele.isdigit():
            noNum_word_list.append(ele)
        # If a string in this list contains not only digits,
        # remove all these digits
        else:
            i = 0
            new_str = ""
            while i < len(ele):
                # If the token in the string(ele) is NOT digit,
                # save the element in new_str
                if not ele[i].isdigit():
                    new_str += ele[i]
                i += 1
            noNum_word_list.append(new_str)
    return noNum_word_list


def rm_stopwords(no_stopwords_list):
    """

    :param no_stopwords_list: a list which removes all the symbols and numbers
    :return:
            no_stopwords_list: a list which removes all the stopwords
    """
    # iterate stopwords in stop_words_list
    # if a stopwords is found in this list
    # remove the stopwords
    for stop_word in stop_words_list:
        while stop_word in no_stopwords_list:
            no_stopwords_list.remove(stop_word)
    return no_stopwords_list


def remain_words(remain_words_list):
    """

    :param remain_words_list: a list which removes all the punctuations,
                             numbers in the token, and stopwords
    :return: the word which has not been completely removed
    """
    processed_words = " ".join(remain_words_list)
    return processed_words


def main():
    global input_list
    # if the user does not enter the mode
    if len(sys.argv) == 1:
        input_list = input().split()
        lower_text = convert_to_lower()
        remove_punc = rm_punctuation(lower_text)
        remove_number = rm_number(remove_punc)
        remove_stopwords = rm_stopwords(remove_number)
        process_words = remain_words(remove_stopwords)
        print(process_words)
    # if the user enters the mode
    else:
        # Does not process the function rm_number()
        if sys.argv[1] == "keep-digits":
            input_list = input().split()
            lower_text = convert_to_lower()
            remove_punc = rm_punctuation(lower_text)
            remove_stopwords = rm_stopwords("".join(remove_punc).split())
            process_words = remain_words(remove_stopwords)
            print(process_words)
        # Does not process the function rm_stopwords()
        elif sys.argv[1] == "keep-stops":
            input_list = input().split()
            lower_text = convert_to_lower()
            remove_punc = rm_punctuation(lower_text)
            remove_number = rm_number(remove_punc)
            process_words = remain_words(remove_number)
            print(process_words)
        # Does not process the function rm_punctuation()
        elif sys.argv[1] == "keep-symbols":
            input_list = input().split()
            lower_text = convert_to_lower()
            remove_number = rm_number(list(" ".join(x for x in lower_text)))
            remove_stopwords = rm_stopwords(remove_number)
            process_words = remain_words(remove_stopwords)
            print(process_words)
        # If the user does not input an valid mode, an error message would prompt
        else:
            print("Invalid mode")
            print("please enter ***python3 preprocess.py <mode>***")
            print("<mode> should be <keep-digits> or <keep-stops> or <keep-symbols>")
            sys.exit(1)


if __name__ == "__main__":
    input_list = []
    stop_words_list = []
    stop_words_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
                       "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her",
                       "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs",
                       "themselves", "what", "which", "who", "whom", "this", "that", "these", "those",
                       "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                       "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
                       "or", "because", "as", "until", "while", "of", "at", "by", "for", "with",
                       "about", "against", "between", "into", "through", "during", "before", "after",
                       "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
                       "under", "again", "further", "then", "once", "here", "there", "when", "where",
                       "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
                       "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                       "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    main()
