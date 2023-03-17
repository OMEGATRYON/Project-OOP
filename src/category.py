class category: 
    def __init__(self, ledger):
         self.ledger = []
         self.amount = 0
         self.description = ""

    def withdraw(self, monies, description):
        if monies > self.amount:
            print("you broke bro")
        elif monies <= self.amount:
            print(self.amount)
        self.ledger.append({'Amount': (transaction), 'Description': description})
        print(self.ledger)
    def deposit(self):
        pass
    def get_balance(self):
        pass
    def transfer(self):
        pass
    def check_funds(self):
        pass