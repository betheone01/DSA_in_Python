
def extraction_and_print(n):
    num=n
    while(num>0):
        last_digit=num%10
        print(last_digit,sep=" " ,end=" ")
        num=num//10
        

def main():
    n=int(input("Enter the number"))
    
    extraction_and_print(n)
    
    

if __name__=="__main__":
    
    main()