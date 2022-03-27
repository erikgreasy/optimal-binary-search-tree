def loadWords():
    dict_words = {}
    arr_words = []
    all_words_arr = []
    sum_pocetnost = 0

    with open('dictionary.txt') as file:
        lines = file.readlines()
        for line in lines:
            temp = line.split(' ')

            word = temp[1].strip()  # get rid of newline char
            number = int(temp[0])

            all_words_arr.append(word)
            dict_words[word] = number

            # COUNT TOTAL POCETNOST FOR LATER CALCULATIONS
            sum_pocetnost += number

            # if dont want number that has less than 50k occurencies
            if number < 50000:
                continue

            arr_words.append(word)

    lex_arr_words = sorted(arr_words)
    lex_all_words = sorted(all_words_arr)

    p = getP(lex_arr_words, dict_words, sum_pocetnost)
    q = getQ(lex_arr_words, lex_all_words, dict_words, sum_pocetnost)

    lex_arr_words.insert(0, '')

    return (p, q, lex_arr_words)


def getP(words, dict_words, sum_pocetnost):
    p = [0]

    for word in words:
        p.append(dict_words[word] / sum_pocetnost)

    return p


def getQ(words, all_words, dict_words, sum_pocetnost):
    q = [0]

    # COUNT Q-s
    for i in range(0, len(words)-1):
        word1 = words[i]
        word2 = words[i+1]

        q_item = countQ(all_words, dict_words, sum_pocetnost, word1, word2)
        q.append(q_item)

    q_sum = 0

    for j in range(all_words.index(words[-1])+1, all_words.index(all_words[-1])):
        q_sum += dict_words[all_words[j]]

    q_sum += dict_words[all_words[-1]]
    q_item = q_sum / sum_pocetnost
    q.append(q_item)

    return q


def countQ(all_words, dict, sum_pocetnost, word1, word2):
    """Count q value for given two words (q_i where i = index of word1)"""
    q_sum = 0

    for j in range(all_words.index(word1)+1, all_words.index(word2)):
        q_sum += dict[all_words[j]]

    return q_sum / sum_pocetnost
