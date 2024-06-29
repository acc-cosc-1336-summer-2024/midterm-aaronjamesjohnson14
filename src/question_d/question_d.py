#write functions here, don't add input('') statements here!

def is_prime(num):

    if num <= 1:
        return False

    for i in range (2, int((num**.5)) + 1):
           
        if num % i == 0:
                
            return False
        
    return True
        

        
        


is_prime(13)