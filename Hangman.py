#0 import module to recognize if a letter is a ascii (American Standard Code for Information Interchange)
from string import ascii_letters
import time
def main():

    
    def sorted_old_letters(old_letters_guessed):
        
        """ returns a sorted list of a list of letters passed as a parameter with "->" between them."""
        
        return " -> ".join(sorted(old_letters_guessed))

    def check_win(secret_word, old_letters_guessed):
        """checks if all letter in the first parameter appear in the 
           second one and returns a bulion accordingly."""
        res = 0
    
        for i in secret_word:
            if i not in old_letters_guessed:
                res += 1
            
        if  res > 0:
            return(False)
        else:
            return(True)
    
    def show_hidden_word(secret_word, old_letters_guessed):
        """loops through the first parameter, checks for each letter 
           if it appears in the second parameter 
           and returns the letter or a hidden symbol( _ )accordingly."""
        res = ""
        for i in secret_word:
            if i in old_letters_guessed:
                res += i
            else:
                res += " _ "
        
        return (res)
    
    def check_valid_input(letter_guessed):
        """ checks if the parameter is a valid ascii, singal-letter and returns a bulion accordingly."""
        #checks for to long input
        if len(letter_guessed) > 1:
            return(False)
        #checks if input in not a valid ascii letter      
        elif set(letter_guessed).difference(ascii_letters):
            return(False)
        #returns True if none of above acred    
        else: 
            return(True)
            
    def Check_if_guessed_before(letter_guessed, old_letters_guessed):
        """check if the first parameter appears in she second one."""
        if letter_guessed in old_letters_guessed:  
            return(True)
        else:
            return(False)    

    #f5 try_update_letter_guessed(updates the old_guessed_letters list or print the list in case of invalid input)(done)
    def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        """ adds the letter from the first parameter to the list in the second one if it is valid,
            returns "X" if not and the list of guessed letters if the letter was tried before"""

        if check_valid_input(letter_guessed) == False:
            return(False)
            #print("X")

        elif Check_if_guessed_before(letter_guessed, old_letters_guessed) == True:
            return("noo")
            #print(sorted_old_letters(old_letters_guessed))

        else:
            
            return(True)
            #old_letters_guessed += [letter_guessed]

    def choose_word(file_path, index):
        """takes from the player a path to a txt file and a number as index and returns the word in the index"""
        #creating a tuple to store the output and a list for the list of unique words.
        ret = tuple()
        listofwords = []

        #opening and reading the txt file.
        openfile = open(file_path, "r")
        rd = openfile.read()

        #creating a loop operator that filters out the multiple words.   
        for word in rd.split():
            if not word in listofwords:
                listofwords += [word] 

        #creating a operator that allows the selected number loop through the text in case its langer the it.
        if len(listofwords) < index:
            index = (index) % len(listofwords)  

        # filling the return tuple.
        return (listofwords[index-1].lower())

        openfile.close()

    
    def START_PAGE(MAX_TRIES):
        """ 1. Prints the Hangman ascii art
            3. Prints the maximum mistakes allowed in the game (defined in the variable MAX_TRIES)"""
        
        print ("""
        _    _                                         
        | |  | |                                        
        | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
        |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | |  | | (_| | | | | (_| | | | | | | (_| | | | |
        |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                            |___/ """)
        
        print ("Maximum tries allowed: ", MAX_TRIES)

    def hangman():
        """ main function:
            defines the variables, 
            interacts with the player, 
            runs the apportion functions
            and returns results"""

        # a int variable that determines the maximum amount of mistakes the player can make
        MAX_TRIES = 7
        #1 print the welcome message
        START_PAGE(MAX_TRIES)

        secret_word = choose_word(input(r"Please enter a valid path to the TXT file: "), int(input("Please enter a valid index number")))
        # a list variable to contane the guessed letters
        old_letters_guessed = []
        
        # a int variable that counts the number of failures
        num_of_tries = 1

        # a dictionary that curtains the different try modes in ascii art(done)
        HANGMAN_PHOTOS = {
                    1:"""
            x-------x 




                """, 2:"""
            x-------x
            |
            |
            |
            |
            |   """, 3:"""
            x-------x
            |       |
            |       0
            |
            |
            |   """, 4:"""
            x-------x
            |       |
            |       0
            |       |
            |
            |   """, 5:"""
            x-------x
            |       |
            |       0
            |      /|\\
            |
            |   """, 6:"""
            x-------x
            |       |
            |       0
            |      /|\\
            |      /
            |   """, 7:"""
            x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            |   """}

        #set's a defult boolien for the while loop
        win = False
        
        print("\nLet's go!\n")
        
        print(HANGMAN_PHOTOS[1])
        print(show_hidden_word(secret_word, old_letters_guessed))

        while num_of_tries < MAX_TRIES and win != True:
            #asks the player to guess a letter.
            letter_guessed = input("Guess a letter:  ").lower()
            # print(num_of_tries)
            # print(old_letters_guessed)
        

            if try_update_letter_guessed(letter_guessed, old_letters_guessed) == False:
                print ("X")

            elif try_update_letter_guessed(letter_guessed, old_letters_guessed) == "noo":
                print("noo, be creative...")
                print(sorted_old_letters(old_letters_guessed))

            elif try_update_letter_guessed(letter_guessed, old_letters_guessed) == True:
                old_letters_guessed += [letter_guessed]

                if letter_guessed in secret_word:
                    print(show_hidden_word(secret_word, old_letters_guessed))

                    if check_win(secret_word, old_letters_guessed):
                        print("You Won!\nYou had", num_of_tries, "misstakes, out of a maximum of", MAX_TRIES, "allowed") 
                        win = True
                else:
                    num_of_tries += 1
                    print(HANGMAN_PHOTOS[num_of_tries])
                    print(show_hidden_word(secret_word, old_letters_guessed))

            if num_of_tries >= 7:
                print("You lost")
            
    hangman() 

    #suggesting the player to play again 
    while "y" in input("Do you want to play again? ((Y)es or (N)o)"):
        hangman()
    else:
        print("It was a pleasure, by by...") 
        time.sleep(5)             
                
                           

if __name__ == "__main__":
    main()                                