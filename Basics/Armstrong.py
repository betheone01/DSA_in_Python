



def armstrong(n):
    
    num=n
    no_of_digits=len(str(num)) #3
    print(no_of_digits)
    total=0
    while(num>0):
        
        last_digit=num%10
        total+=last_digit**no_of_digits
        print(f"Total is {total}")
        num=num//10
        print(num)
        
    if(total==n):
        print(f"Total is {total}")
        return True 
    else:
        False

def main():
    n=int(input("Enter the number"))
    print("Armstrong" if armstrong(n) else "Not armstrong")    

if __name__=="__main__":
    
    main()