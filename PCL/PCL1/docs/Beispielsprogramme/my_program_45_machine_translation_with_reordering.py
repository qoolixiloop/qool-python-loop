#!/usr/bin/python

# program to do word-by-word translation based on a bilingual dictionary
# with reordering of a German VVPP verb
# by Martin Volk

# define a hash (= dictionary)
my_lexicon = {'Tante': 'aunt',
              'Polly': 'Polly',
              'sah': 'saw',
              'Mann': 'man',
              'mit': 'with',
              'Fernglas': 'telescope',
              'im': 'in the',
              'Garten': 'garden',
              'dem': 'the',
              'der': 'the',
              'den': 'the',
              'hat': 'has',
              'gesehen': 'seen',
              'beobachtet': 'watched'}

## test sentences with Part-of-Speech tags
test_sentence = 'Tante#NN Polly#NE sah#VVFIN den#ART Mann#NN mit#APPR' \
+' dem#ART Fernglas#NN'
test_sentence = 'Tante#NN Polly#NE hat#VAFIN den#ART Mann#NN mit#APPR' \
+ ' dem#ART Fernglas#NN gesehen#VVPP'
test_sentence = 'Tante#NN Polly#NE hat#VAFIN den#ART Mann#NN mit#APPR' \
+ ' dem#ART Fernglas#NN beobachtet#VVPP'
test_sentence = 'Tante#NN Polly#NE hat#VAFIN den#ART Mann#NN im#APPRART' \
+ ' Garten#NN mit#APPR dem#ART Fernglas#NN beobachtet#VVPP'

### for advanced students ###
# Example: 'Tante Polly wird den Mann mit dem Fernglas sehen koennen'
test_sentence = 'Tante#NN Polly#NE wird#VAFIN den#ART Mann#NN mit#APPR'\
 +' dem#ART Fernglas#NN sehen#VVINF koennen#VMINF'

# initialize a list to hold tuples of word + PoS tag
word_pos_tuple_list = []
print 'Input sentence:', test_sentence

# convert the sentence into a list
test_list = test_sentence.split()

# work through the list and create a new list where each pair of word + PoS tag is a tuple
for word_pos_pair in test_list:
    (word, pos) = word_pos_pair.split('#')
    word_pos_tuple_list.append((word, pos))

################ reorder the sentence ###################
## if the sentence contains a VAFIN and a VVPP, then place them in a sequence

## an index variable for the list
i = 0

## a variable to store the position of the VVPP in the sentence
vvpp_position = 0

## for each word + pos-tag pair do
for word_pos in word_pos_tuple_list:
    #	print my_tuple
    ## if the current PoS tag is a finite auxiliary verb
    ## then save the position
    if word_pos[1] == 'VAFIN':
        vafin_position = i
    ## else if the current PoS tag is a full verb in past participle
    ## then save the position and the tuple
    elif word_pos[1] == 'VVPP':
        vvpp_position = i
        vvpp_tuple = word_pos
    ## index for the position in the list
    i += 1

## if we found a full verb in past participle
if vvpp_position > 0:
    ## remove the VVPP tuple from its original position
    word_pos_tuple_list.pop(vvpp_position)
    ## insert the VVPP tuple after the VAFIN
    word_pos_tuple_list.insert(vafin_position + 1, vvpp_tuple)

################ end of reorder the sentence ###############
print 'Output sentence:',
# work through the list and translate each word
for word_pos in word_pos_tuple_list:
    word = word_pos[0]
    ## if the word is in the lexicon as key
    if word in my_lexicon:
        print my_lexicon[word],
    else:
        print '\n >>>', word, ' is unknown!!! :-('

print
print '---------------------'
