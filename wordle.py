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
    all_words = solutions + guesses
    good_guesses = {}
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
            top_popular_letters_by_index[i] = popular_letters_list

    # assign points to each guess based on letter indices
    for word in all_words:
        points = 0
        for i in range(len(word)):
            top_popular_letters = top_popular_letters_by_index[i]
            char = word[i]
            if char in top_popular_letters:
                char_position = top_popular_letters.index(char)
                points += char_position
            else:
                points += 26
        good_guesses[word] = points

    # the words with the least amount of points are considered the best guesses
    sorted_good_guesses = dict(sorted(good_guesses.items(), key=lambda item: item[1]))
    good_guesses_list = list(sorted_good_guesses.keys())


    pprint(sorted_good_guesses['saine'])
    pprint(sorted_good_guesses['saint'])
    pprint(sorted_good_guesses['crane'])
    pprint(sorted_good_guesses['salet'])

    return good_guesses_list[:20]

    # TODO: decomp this de-dup functionality
    # final_list = []
    # for word in good_guesses_list:
    #     has_double_letter = False
    #     for ch in word:
    #         if word.count(ch) > 1:
    #             has_double_letter = True
    #     if has_double_letter == False:
    #         final_list.append(word)
    # return final_list[:40]  # return top 40 good first guesses


def main():
    good_guesses = get_good_guess_list(SOLUTIONS_LIST, GUESS_LIST)
    pprint('Good First Guesses:')
    pprint(good_guesses)


if __name__ == '__main__':
    main()
