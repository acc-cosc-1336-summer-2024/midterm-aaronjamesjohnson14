#write functions here, don't add input('') statements here!
def test_config():
    return True


def get_fahrenheit(celsius):

    while celsius <= 20:

        fahrenheit = (9/5* celsius) + 32

        print(celsius, "Degrees Celsius is ", fahrenheit, "Degrees Fahrenheit")

        celsius += 1

        return fahrenheit


    


