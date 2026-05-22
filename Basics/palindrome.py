

def palindrome(n):
    # if (n==0 or n==1 ):
    #     return True
    if(len(str(n)) == 1):
        return True
    num=n
    reverse=0
    while(num>0):
        last_digit=num%10
        reverse=(reverse*10)+last_digit
        print(reverse)
        num=num//10
    
    if reverse == n:
        return True
    else :
        return False
    



def main():
    n=int(input("Enter the number"))
    print("Palindrome" if palindrome(n) else "Not Palindrome")    

if __name__=="__main__":
    
    main()