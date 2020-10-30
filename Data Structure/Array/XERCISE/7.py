# Write a Python program to find the list of words that are longer than n from a given list of words


def word_count(n,words):
    result_word = []
    txt = words.split(' ')
    for i in txt:
        if len(i) > n:
            result_word.append(i)

    return result_word


n = 3
words = 'ab ki bar modi sarkar' 
ans = word_count(n,words)
print(ans)
'''
Output:-
['modi', 'sarkar']
'''