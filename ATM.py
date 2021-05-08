class ATM(object):

    def _init_(self,cardnumber,cvv):
        self.cardname=cardname
        self.cardnumber=cardnumber
        self.expirydate=expirydate
        self.cvv=cvv

    def cashwithdrawal(self,cardnumber,cvv):
        print("Cash withdrawal successful for "+cardnumber )

    def balanceenquiry(self,cardnumber,cvv):
        print("bank balance for"+cardnumber)


def main():
    cardnumber=input("ENTER YOUR CARDNUMBER")       
    cvv=input("ENTER YOUR CVV") 
    
    user1=ATM(cardnumber,cvv)
    print("CHOOSE AN ACTIVITY")
    print("1.CASH WITHDRAWAL   2.BALANCE ENQUIRY")
    choice=int(input("ENTER ACTIVITY NUMBER"))
    if choice==1:
        user1.cashwithdrawal(cardnumber,cvv)
    elif choice==2:
         user1.balanceequiry(cardnumber,cvv)

    else:
        print("PLEASE ENTER A VALID INPUT")


if __name__ == "__main__":
     main()    