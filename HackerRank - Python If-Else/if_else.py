if __name__ == '__main__':
    n = int(raw_input())
    
    if(n % 2 != 0):
        print "Weird"
        
    else:
        if(n >=2 and n <= 5 and n % 2 == 0):
            print "Not Weird"
        elif(n >= 6 and n <= 20 and n % 2 == 0):
            print "Weird"
        else:
            print "Not Weird"
            
    
        