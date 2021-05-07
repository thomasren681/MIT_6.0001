# Problem Set 2
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    boolean = True
    for letter in secret_word:
        if letter not in letters_guessed:
            boolean = False

    return boolean


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_wordlist = []
    for idx,letter in enumerate(secret_word):
        if letter in letters_guessed:
            guessed_wordlist.append(letter)
        else:
            guessed_wordlist.append('_')

    str = "".join(guessed_wordlist)
    return str



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_of_all_lowercase = list(string.ascii_lowercase)
    for letter in letters_guessed:
        list_of_all_lowercase.remove(letter)

    str = "".join(list_of_all_lowercase)

    return str


def get_unique_letters(secret_word):
    """
    :param secret_word: a string
    :return: a list of characters which contains each unique character in the string
    """
    wordlist = list(secret_word)
    for letter in wordlist.copy():
        if letter == '_':
            continue
        elif wordlist.count(letter)>1:
            wordlist.remove(letter)

    return wordlist



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guesses_left = 6#initail guess times
    warnings_left = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    num_of_unique_letters = len(get_unique_letters(secret_word))
    #methods to calculate the total score

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long" % len(secret_word))
    print('-'*20)
    while (guesses_left>0 and warnings_left>=0):
        print('You have %d warnings left.' % warnings_left)
        print('You have %d guesses left.' % (guesses_left))
        available_letters = get_available_letters(letters_guessed)
        print('Availble letters: ', get_available_letters(letters_guessed))
        print('The letters you have been guessed are: ', letters_guessed)
        letter = str.lower(input('Please guess a letter:'))
        if not str.isalpha(letter):
            warnings_left -= 1
            print('Oops! That is not a valid letter. You have %d warnings left: ' % warnings_left, get_guessed_word(secret_word,letters_guessed))
        elif letter not in available_letters:
            warnings_left -= 1
            print('Oops! You\'ve already guesses that letter. You now have %d warnings:' % warnings_left)
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(letter)
        if letters_guessed[-1] in secret_word:
            print('Good guess: ', get_guessed_word(secret_word,letters_guessed))
        else:
            if letters_guessed[-1] not in vowels:
                print('Oops! That letter is not in my word: ', get_guessed_word(secret_word,letters_guessed))
                guesses_left -= 1
            else:
                print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 2

        print('-'*20)#dashes to seperate each guess

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print('Your total score for this game is:', guesses_left*num_of_unique_letters)
            break

    #run out of guesses or warnings
    if not is_word_guessed(secret_word,letters_guessed):
        print('Sorry, you ran out of guesses or warnings. The word was ', secret_word)




    return secret_word



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word) != len(other_word):
        return False
    else:
        boolean = True
        for idx,letter in enumerate(my_word):
            if letter == '_':
                if other_word[idx] in my_word:
                    return False
                else:
                    continue
            else:
                if letter == other_word[idx]:
                    boolean *= 1
                else:
                    boolean *= 0

        return bool(boolean)




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    match_wordlist = []
    for word in wordlist:
        if match_with_gaps(my_word,word) and len(word) == len(my_word):
            match_wordlist.append(word)
    if len(match_wordlist) != 0:
        return match_wordlist
    else:
        match_wordlist.append('No Matches Found')
        return match_wordlist[0]



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_left = 6  # initail guess times
    warnings_left = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    num_of_unique_letters = len(get_unique_letters(secret_word))
    # methods to calculate the total score

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long" % len(secret_word))
    print('-' * 20)
    while (guesses_left > 0 and warnings_left >= 0):
        print('You have %d warnings left.' % warnings_left)
        print('You have %d guesses left.' % (guesses_left))
        available_letters = get_available_letters(letters_guessed)
        print('Availble letters: ', get_available_letters(letters_guessed))
        print('The letters you have been guessed are: ', letters_guessed)
        letter = str.lower(input('Please guess a letter:'))
        if not str.isalpha(letter):
            if letter == '*':
                print('Possible word matches are:')
                print(show_possible_matches(get_guessed_word(secret_word,letters_guessed)))
            else:
                warnings_left -= 1
                print('Oops! That is not a valid letter. You have %d warnings left: ' % warnings_left,
                    get_guessed_word(secret_word, letters_guessed))
        elif letter not in available_letters:
            warnings_left -= 1
            print('Oops! You\'ve already guesses that letter. You now have %d warnings:' % warnings_left)
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(letter)
        if letters_guessed[-1] in secret_word:
            print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
        else:
            if letters_guessed[-1] not in vowels:
                print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 1
            else:
                print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 2

        print('-' * 20)  # dashes to seperate each guess

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print('Your total score for this game is:', guesses_left * num_of_unique_letters)
            break

    # run out of guesses or warnings
    if not is_word_guessed(secret_word, letters_guessed):
        print('Sorry, you ran out of guesses or warnings. The word was ', secret_word)

    return secret_word



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    secret_word = 'apple'
    hangman_with_hints(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)


