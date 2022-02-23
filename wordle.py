from pprint import pprint
import words

WORD_LIST = words.list


def get_letter_occurances(word_list):
    occurances = {}
    for word in word_list:
        for ch in word:
            if ch not in occurances:
                occurances[ch] = 0
            occurances[ch] += 1
    sorted_occurances = dict(sorted(occurances.items(), key=lambda item: item[1], reverse=True))
    return sorted_occurances


def get_letter_percentages(letter_occurances):
    count_list = list(letter_occurances.values())
    total_count = sum(count_list)
    percentages = {}

    for letter, count in letter_occurances.items():
        percentages[letter] = "{:.2%}".format(count / total_count)
    return percentages


def get_popular_letters_by_index(word_list, i):
    letter_counts = {}
    for word in word_list:
        letter = word[i]
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    sorted_letter_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_letter_counts



def main():
    letter_occurances = get_letter_occurances(WORD_LIST)
    pprint('Letter Occurances:')
    pprint(letter_occurances, sort_dicts=False)

    letter_percentages = get_letter_percentages(letter_occurances)
    pprint('Letter Occurance Percentages')
    pprint(letter_percentages, sort_dicts=False)

    popular_first_letters = get_popular_letters_by_index(WORD_LIST, 0)
    most_popular_first_letter = list(popular_first_letters.keys())[0]
    pprint('Popular First Letters')
    pprint(popular_first_letters, sort_dicts=False)

    popular_second_letters = get_popular_letters_by_index(WORD_LIST, 1)
    most_popular_second_letter = list(popular_second_letters.keys())[0]
    pprint('Popular Second Letters')
    pprint(popular_second_letters, sort_dicts=False)

    popular_third_letters = get_popular_letters_by_index(WORD_LIST, 2)
    most_popular_third_letter = list(popular_third_letters.keys())[0]
    pprint('Popular Third Letters')
    pprint(popular_third_letters, sort_dicts=False)

    popular_fourth_letters = get_popular_letters_by_index(WORD_LIST, 3)
    most_popular_fourth_letter = list(popular_fourth_letters.keys())[0]
    pprint('Popular Fourth Letters')
    pprint(popular_fourth_letters, sort_dicts=False)

    popular_fifth_letters = get_popular_letters_by_index(WORD_LIST, 4)
    most_popular_fifth_letter = list(popular_fifth_letters.keys())[0]
    pprint('Popular Fifth Letters')
    pprint(popular_fifth_letters, sort_dicts=False)

    pprint('Most Popular Letters by Index')
    pprint({
        0: most_popular_first_letter,
        1: most_popular_second_letter,
        2: most_popular_third_letter,
        3: most_popular_fourth_letter,
        4: most_popular_fifth_letter
    })


if __name__ == '__main__':
    main()
