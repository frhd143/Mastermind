
from mastermind_funcs import *


# konverterar int (t.ex. 1234) to a list (t.ex. [1, 2, 3, 4])
def convert_int_to_list(theInt):
    list1 = [int(i) for i in str(theInt)]
    return list1


# Kontrollerar om längden är okej! (Längden på koden måste vara 4)
def check_length(code):
    if len(code) == 4:
        return True
    else:
        return False



# Man har 10 försök på sig att gissa koden!
def Ten_attempts(code):
    x = 10 
    while x > 0:
        input_value = input("Guess the code: ")
        var_check_length = check_length(input_value)
        # Längen på koden måste vara okej! 
        if var_check_length == True:
            the_guessed_code = convert_int_to_list(input_value)
            # Kollar om användaren gissat rätt!
            if the_guessed_code == code:
                print("Great job!")
                x = 0
                return # Avsluta programmet om användaren gissat rätt!
            else:
                var_right_position = right_position(the_guessed_code, code)
                var_wrong_position = wrong_position(the_guessed_code, code)
                print("Right guess and right position(Balck or Red): ", var_right_position)
                print("Right guess but wrong position(White): ", var_wrong_position)
                x = x - 1
                print("You have", x, "attempts left!")
        # Om längden är inte okej!
        else:
            print("The code must contain 4 digits! Try again!")
            x = x - 1
            print("You have", x, "attempts left!")
            
    # If you don't guess the code after 10 attempts!
    print(" You lost!, The code is: ", code)



the_real_code = generate_code()
Ten_attempts(the_real_code)

