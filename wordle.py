from pprint import pprint
import words

SOLUTIONS_LIST = words.SOLUTIONS
GUESS_LIST = words.GUESSES


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


def get_good_guess_list(solutions, guesses):
    good_guesses = []
    good_guess_points = {}
    max_popular_letters = 5
    top_popular_letters_by_index = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
    }

    # populate the top_popular_letters_by_index dict using all possible solution words
    for i in range(max_popular_letters):
        for word in solutions:
            popular_letters = get_popular_letters_by_index(solutions, i)  # returns a dict with letter counts
            popular_letters_list = list(popular_letters.keys())
            top_popular_letters_by_index[i] = popular_letters_list[:max_popular_letters]

    # determine if a word should be considered a good guess
    for word in guesses:
        good_guess = True
        for i in range(len(word)):
            ch = word[i]

            # a word is not a good guess if its characters at each index aren't in top_popular_letters_by_index
            if word[i] not in top_popular_letters_by_index[i]:
                good_guess = False
                break

            # a word is not a good guess if it repeats any of its characters
            if word.count(ch) > 1:
                good_guess = False
                break

        if good_guess:
            good_guesses.append(word)

    # assign points to each guess based on letter indices
    for word in good_guesses:
        points = 0
        for i in range(len(word)):
            top_popular_letters = top_popular_letters_by_index[i]
            char = word[i]
            char_position = top_popular_letters.index(char)
            points += char_position
        good_guess_points[word] = points

    # the words with the least amount of points are considered the best guesses
    sorted_good_guess_points = dict(sorted(good_guess_points.items(), key=lambda item: item[1]))

    return list(sorted_good_guess_points.keys())


def main():
    good_guesses = get_good_guess_list(SOLUTIONS_LIST, GUESS_LIST)
    pprint('Good First Guesses:')
    pprint(good_guesses)

    letter_occurances = get_letter_occurances(SOLUTIONS_LIST)
    pprint('Letter Occurances:')
    pprint(letter_occurances, sort_dicts=False)

    letter_percentages = get_letter_percentages(letter_occurances)
    pprint('Letter Occurance Percentages:')
    pprint(letter_percentages, sort_dicts=False)

    popular_first_letters = get_popular_letters_by_index(SOLUTIONS_LIST, 0)
    most_popular_first_letter = list(popular_first_letters.keys())[0]
    pprint('Popular First Letters:')
    pprint(popular_first_letters, sort_dicts=False)

    popular_second_letters = get_popular_letters_by_index(SOLUTIONS_LIST, 1)
    most_popular_second_letter = list(popular_second_letters.keys())[0]
    pprint('Popular Second Letters:')
    pprint(popular_second_letters, sort_dicts=False)

    popular_third_letters = get_popular_letters_by_index(SOLUTIONS_LIST, 2)
    most_popular_third_letter = list(popular_third_letters.keys())[0]
    pprint('Popular Third Letters:')
    pprint(popular_third_letters, sort_dicts=False)

    popular_fourth_letters = get_popular_letters_by_index(SOLUTIONS_LIST, 3)
    most_popular_fourth_letter = list(popular_fourth_letters.keys())[0]
    pprint('Popular Fourth Letters:')
    pprint(popular_fourth_letters, sort_dicts=False)

    popular_fifth_letters = get_popular_letters_by_index(SOLUTIONS_LIST, 4)
    most_popular_fifth_letter = list(popular_fifth_letters.keys())[0]
    pprint('Popular Fifth Letters:')
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
