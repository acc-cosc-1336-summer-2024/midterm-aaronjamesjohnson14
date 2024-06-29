#add import

from question_b import get_miles_per_hour


def menu_for_get_miles_per_hour():

    kilometers = int(input("Kilometers: "))
    minutes = int(input("Minutes: "))

    if kilometers < 0 or minutes < 0:
        print ("Invalid Arguments")
        exit()

    get_miles_per_hour(kilometers, minutes)


menu_for_get_miles_per_hour()
