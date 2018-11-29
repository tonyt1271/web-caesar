def alphabet_position(letter):
    """This function finds the numeric value of the letter"""
    import string
    global letter_list_lower        #making letter list upper available to both functions in this module
    letter_list_lower = []
    global letter_list_upper        #making letter list lower available to both functions in this module
    letter_list_upper = []

    for index in range(26):
        letter_list_lower.append(string.ascii_lowercase[index]) #turning the letter strings to list for use
        letter_list_upper.append(string.ascii_uppercase[index]) #of the index system because it is covenient
    if letter in letter_list_lower:                             #for this problem
        letter_num = letter_list_lower.index(letter)            #converting lower case letter to index value
        return letter_num
    elif letter in letter_list_upper:                           #converting upper case letter to index value
        letter_num = letter_list_upper.index(letter)
        return letter_num
    else:
        return letter                                           #if the character is not a letter return the
                                                                #character unchanged


def rotate_character(words,rot):
    """This function applies the rotation to the characters"""
    import string
    num_words_list = []
    new_words = []
    for letter in words:
        num_words_list.append(alphabet_position(letter))

        if letter in string.ascii_lowercase:
            rot_letter = letter_list_lower[(alphabet_position(letter)+rot)%26]
            new_words.append(rot_letter)

        elif letter in string.ascii_uppercase:
            rot_letter = letter_list_upper[(alphabet_position(letter)+rot)%26]

            new_words.append(rot_letter)

        else:
            new_words.append(letter)

    new_words = "".join(new_words)

    return new_words


def vigenere1(string_1,key_word):
    """The function takes uses the caesar function with a key word
    to apply a vigenere encryption to a string non letter characters
    are left unchanged. variables sent to the function are the string and
    the encryption keyword"""
    import caesar       #importing the caesar function
    import string       #importing the string module
    key_list = []
    for letter in key_word:                                 #iterating throuh key_word
        key_list.append(caesar.alphabet_position(letter))   #to create a list of numbers
    key_num = 0                                             #to be used for the rotation
    vig_string = []                                         #part of the encryption
    for character in string_1:
        if character.isalpha():                             #rotating rhought key values
            key_val = key_list[key_num%len(key_word)]       #applying to letters only

                                                                                #the ceasar.rotate_character() function
            vig_string.append(caesar.rotate_character(character, key_val))   #applies the encryption
            key_num += 1
        else:
            vig_string.append(character)    #if character was not a letter it remains
    a = "".join(vig_string)                 #unchanged
    print(a)
    return a

