from aMain import AtmMain
from bmain import BankMain
while(True):
          print("="*60)
          print("\t\tWELCOME TO MY BANK APPLICATION")
          print("="*60)
          print("\t\t\t1. BANK Application")
          print("\t\t\t2. ATM Application")
          print("="*60)
          try:
                    ch=int(input("What You want to use:"))
                    if(ch==1):
                              BankMain()
                    elif(ch==2):
                              AtmMain()
                    else:
                              print("Sorry your choice is wrong.Please Try again")
          except ValueError:
                    print("="*60)
                    print("Dont't enter String/Special symbol/Alphanumeric for Withdraw")
