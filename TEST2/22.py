class Bankaccount:
    def __init__(self,total_blns):
        self.total_blns=total_blns
    def deposit(self,amount):
        self.total_blns+=amount
        print("deposit_amt:",amount)
    def withdrawal(self,amount):
        if amount<=self.total_blns:
            self.total_blns-=amount
        else:
            print("withdrawal impossible")
    def blns_amt(self):
        print(self.total_blns)
acc=Bankaccount(1000)
acc.deposit(200)
acc.withdrawal(1600)
acc.blns_amt()

        