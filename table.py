"""ask user a number and print the multiplication table
1.ask user to input any number and assign it with variable uint1
2.assign the variable n and assign it with value 1
3. run while loop till n  is lesser than 11
4.print (ui*n)
5. increment the value of n by 1 each time
"""
ui=input("enter any number")
ui=int(ui)
n=1#(here n is a multplier)
while n<11:
    print(n*ui)
    n=n+1#(incrementing the divider in every loop)