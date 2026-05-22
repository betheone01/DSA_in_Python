# Count the Number of Digits in an Integer
import math
# Solution 1
def NoOfDigits(n):
    num =n
    count=0
    while(num>0):
        last_digit=num%10
        # print(last_digit)
        count+=1
        num=num//10
        
    
    return count

# Solution 2
def NoOfDigits1(n):
        count1=math.log10(n)
        return count1+1


def main():
    n=int(input("Enter the number"))
    
    count=NoOfDigits(n)
    print(count)
    count1=NoOfDigits1(n)
    print(int(count1))
    
    

if __name__=="__main__":
    
    main()