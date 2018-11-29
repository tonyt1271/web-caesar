from helpers import alphabet_position, rotate_character


def encrypt(the_string, rot):
    return rotate_character(the_string, rot)

def main():
    """Main function for caesar"""
    from sys import argv
    #print("This is what the user typed on the command line:", argv)
    the_string = ""
    while the_string == '':
        the_string = input("Type the message to be encoded: \n")

    #rot = 'not an integer'
    try:
        rot = int(argv[1])
    except:
        rot = 'not and integer'
    while type(rot) != int:
        try:
            rot = int(input("Rotate by:\n"))

        except:
            print('The vlaue must be an integer')

    print(rotate_character(the_string, rot))


if __name__ == "__main__":
    main()



