# The user will input a sentence and the output will be a tally of each 
# word in the sentence

sentence_choice = input('Please eneter a sentence: ')

sentence_list = sentence_choice.split()

word_count = {}

for word in sentence_list:

    new_count = sentence_list.count(word)
    word_count[word]=new_count
        
print(word_count)