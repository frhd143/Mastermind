# Labration 2
# Skriven av Farhad Asadi, 29 september 2021


# Uppgift - Master Mind

# Krav på ett godkänd spel
# Du ska bryta ned din kod i flera funktioner. Det ska särskilt finnas!
# 1. en funktion, generate_code(), som genererar en slumpmässig fyrsiffrig 
#    kod med siffror 0-5, och returnerar koden i form av en lista med de fyra slumpade siffrorna
# 2. en funktion, right_position(guess, code), som tar in den gissade sifferkombinationen i form
#    av en lista, guess, och den riktiga kombinationen i en annan lista, code, och returnerar 
#    hur många siffror som är rätt på och på rätt plats .
# 3. en funktion, wrong_position(guess, code), som tar in den gissade sifferkombinationen i form 
#    av en lista, guess, och den riktiga kombinationen i en annan lista, code, och returnerar hur 
#    många siffror som är rätt men på fel plats.
 
# Dessa funktioner ska anropas i ditt program. Funktionerna ska läggas i en egen fil, som  som 
# döps till mastermind_funcs.py och som är fristående från huvudprogrammet med spelet. Allt innehåll
# i filen mastermind_funcs.py ska vara helt oberoende av användargränssnittet.

# Fråger!
# 1. Hur mycket tid trodde du att det skulle ta att lösa den här uppgiften?
# svar: Jag trodde att det skulle ta ungefär 3 timmar!
# 2. Hur mycket tid har du lagt ned på att lösa uppgiften?
# svar: Jag har lagt ned ungefär 7 timmar på att lösa uppgiften.


import random


# Funktionen skapar en fyrsiffrig kod med siffror 1-5
# Funktionen returnerar en kod i form av en lista med fyra siffror!
# T.ex. [1, 3, 4, 3]

def generate_code():
    list1 = []
    for i in range(1, 5):
        the_code = random.randrange(0, 5)
        list1.append(the_code)
    return list1


# Funktionen kollar hur många siffror som är rätt OCH på rätt plats
# Funktionen returnerar en siffra: T.ex. 3 (3 siffror är rätt och på rätt plats)
def right_position(guess, code):
    right_pos = 0
    for i in range(0, 4):
        if guess[i] == code[i]:
            right_pos += 1
    return right_pos


# Funktionen kollar hur många siffror som rätt MEN fel plats
# (!!En siffra i kod som är på RÄTT PLATS kommer inte räknas!!)
def wrong_position(guess, code):
    right_num = 0
    new_guess_list = []
    new_code_list = []
    for i in range(0, len(code)):
        if guess[i] != code[i]:             # Skippar första index
            new_guess_list.append(guess[i]) # Guess = [4, 1, 1, 1] = [4, 1, 1]
            new_code_list.append(code[i])   # Code = [1, 1, 5, 3] = [1, 5, 3]


    # Ex: vi måste få 3! inte 4!
    # new_guess_list = [5 ,5 ,1 ,1] = []
    # new_code_list = [1, 1 ,5, 3] = []
    for i in range(0, len(new_guess_list)):    
        if new_guess_list[i] in new_code_list:
            value = new_code_list.index(new_guess_list[i]) 
            new_code_list[value] = 8
            right_num += 1

    return right_num



