# Problem Set 4B
# Name: Thomas Ren
# Collaborators: None
# Time Spent: About 3 hours

import string

### HELPER CODE ###
import numpy as np


def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    # >>> is_word(load_words('words.txt'), 'bat')
    # True
    # >>> is_word(load_words('words.txt'), 'asdf')
    # False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

# if __name__ == '__main__':
#     word_list = load_words('words.txt')
#     print(is_word(word_list, 'dance'))

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
WORD_LIST = load_words(WORDLIST_FILENAME)

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = list(text.split(' '))

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return str(self.message_text)

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dict = {'a':string.ascii_lowercase[-shift], 'b':string.ascii_lowercase[-shift+1],'c':string.ascii_lowercase[-shift+2],
                'd': string.ascii_lowercase[-shift+3],'e':string.ascii_lowercase[-shift+4],'f':string.ascii_lowercase[-shift+5],
                'g': string.ascii_lowercase[-shift+6],'h':string.ascii_lowercase[-shift+7],'i':string.ascii_lowercase[-shift+8],
                'j': string.ascii_lowercase[-shift+9],'k':string.ascii_lowercase[-shift+10],'l':string.ascii_lowercase[-shift+11],
                'm': string.ascii_lowercase[-shift+12],'n':string.ascii_lowercase[-shift+13],'o':string.ascii_lowercase[-shift+14],
                'p': string.ascii_lowercase[-shift+15],'q':string.ascii_lowercase[-shift+16],'r':string.ascii_lowercase[-shift+17],
                's': string.ascii_lowercase[-shift+18],'t':string.ascii_lowercase[-shift+19],'u':string.ascii_lowercase[-shift+20],
                'v': string.ascii_lowercase[-shift+21],'w':string.ascii_lowercase[-shift+22],'x':string.ascii_lowercase[-shift+23],
                'y': string.ascii_lowercase[-shift+24],'z':string.ascii_lowercase[-shift+25],'A':string.ascii_uppercase[-shift],
                'B':string.ascii_uppercase[1-shift],'C':string.ascii_uppercase[2-shift],'D':string.ascii_uppercase[3-shift],
                'E': string.ascii_uppercase[4-shift],'F':string.ascii_uppercase[5-shift],'G':string.ascii_uppercase[6-shift],
                'H': string.ascii_uppercase[7-shift],'I':string.ascii_uppercase[8-shift],'J':string.ascii_uppercase[9-shift],
                'K': string.ascii_uppercase[10-shift], 'L': string.ascii_uppercase[11-shift],'M': string.ascii_uppercase[12-shift],
                'N': string.ascii_uppercase[13-shift], 'O': string.ascii_uppercase[14-shift],'P': string.ascii_uppercase[15-shift],
                'Q': string.ascii_uppercase[16-shift], 'R': string.ascii_uppercase[17-shift],
                'S': string.ascii_uppercase[18-shift],
                'T': string.ascii_uppercase[19-shift], 'U': string.ascii_uppercase[20-shift],
                'V': string.ascii_uppercase[21-shift],
                'W': string.ascii_uppercase[22-shift], 'X': string.ascii_uppercase[23-shift],
                'Y': string.ascii_uppercase[24-shift],'Z': string.ascii_uppercase[25-shift],
                }
        return dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_list = []
        dict = self.build_shift_dict(shift)
        for letter in self.message_text:
            if letter.isalpha():
                shifted_list.append(dict.get(letter, 0))
            else:
                shifted_list.append(letter)

        shifted_str = ''.join(shifted_list)
        return shifted_str


# if __name__ == '__main__':
#     a = Message('abcd efg')
#     encrypted_a = Message(a.apply_shift(2))
#     decrypted_a = encrypted_a.apply_shift(26-2)
#     print(encrypted_a.get_message_text())
#     print(decrypted_a)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = Message(self.message_text).build_shift_dict(self.shift)
        self.message_text_encrypted = Message(self.message_text).apply_shift(26-self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        return self.shift

# if __name__ == '__main__':
#     plaintext = PlaintextMessage('hello', 2)
#     print('Expected Output: jgnnq')
#     # print('Actual Output:', plaintext.get_message_text_encrypted())
#     print(plaintext.get_message_text_encrypted())


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        NUM_WORDS = []
        text = self.message_text
        # text_list = self.valid_words
        # word_list = load_words('words.txt')
        for shift in range(26):
            shifted_text = Message(text).apply_shift(shift)
            shifted_text_list = list(shifted_text.split(' '))
            temp = []
            for word in shifted_text_list:
                temp.append(is_word(WORD_LIST, word))
            NUM_WORDS.append(sum(temp))

        best_shift = np.argmax(NUM_WORDS)
        decrypted_message = Message(self.message_text).apply_shift(best_shift)


        return (26-best_shift, decrypted_message)

if __name__ == '__main__':

    story = get_story_string()
    encrypted_story = CiphertextMessage(story)
    decrypted_story = encrypted_story.decrypt_message()
    print(decrypted_story)
    ######################################################################################
    #Here is the decrypted story


    # 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack.
    # He has been registered for classes at MIT twice before, but has reportedly never passed aclass.
    # It has been the tradition of the residents of East Campus to become Jack Florey for a few nights
    # each year to educate incoming students in the ways, means, and ethics of hacking.'

    #####################################################################################

    # #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())
    #
    # #Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story

    # test_text = 'abc def cat g.'
    # test_text = Message(test_text)
    # encrypted_text = test_text.apply_shift(3)
    # print(encrypted_text)
    # encrypted_text = CiphertextMessage(encrypted_text)
    # decrypted_list = encrypted_text.decrypt_message()
    # print(decrypted_list)
