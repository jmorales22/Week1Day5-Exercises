# The user will input a word and the output will be a tally of each 
# letter in the word

word_choice = input('Please eneter a word: ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet_count = {}

for alpha in alphabet:
    if alpha in word_choice:
            num_letters = word_choice.count(alpha)
            alphabet_count[alpha]=num_letters
        
print(alphabet_count)

