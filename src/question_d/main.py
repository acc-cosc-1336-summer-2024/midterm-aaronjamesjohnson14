#add import

from question_d import is_prime


def continue_option():
     
    print("Would You Like To Continue?" )
    print("1 - Yes")
    print("2 - No")

    continue_choice = int(input(""))

    if continue_choice == 1:
        menu_is_prime()
    
    elif continue_choice == 2: 
          exit()

def menu_is_prime():

    num = int(input("What Number Would You Like To Check Is Prime? "))

    result = is_prime(num)

    print (result)

    continue_option()


menu_is_prime()



