#write functions here, don't add input('') statements here!



def get_miles_per_hour(kilometers, minutes):

    miles = kilometers * .621371
    hours = minutes / 60

    miles_per_hour = miles / hours
    
    print (miles_per_hour, "Miles Per Hour")

    return miles_per_hour




