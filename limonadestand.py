import random


class Store:


    def __init__(self):
        
        self.cash = 100
        self.lemons = 0
        self.lemons_price = random.randrange(1,6)
        self.sugar = 0
        self.sugar_price = random.randrange(1,6)
        self.ice = 0
        self.ice_price = random.randrange(1,6)
        self.numpitchers = 0
        self.numpitchers = 0
        self.total_cost = 0
        

    def makelemonade(self):
        print (' The price of lemons is :  ', self.lemons_price)
        print (' the price of ice is :  ', self.ice_price)
        print (' The price of sugar :  ', self.sugar_price) 
    
    def purchase(self):        
        self.lemons = int(input (' How many lemons do you want to Buy:  '))
        self.sugar = int(input(' How much sugar do you want to buy:  '))
        self.ice = int(input(' How much ice do you want to buy:  '))
        
    
    def cost(self):    
        self.lemons_cost = self.lemons * self.lemons_price
        self.sugar_cost = self.sugar * self.sugar_price
        self.ice_cost = self.ice * self.ice_price
        self.pitchers  = float((self.lemons_cost + self.sugar_cost + self.ice_cost) / 10
        self.cup_cost = (self.pitchers / 10)
        print (' Price per pitcher i: ', self.pitchers)
        print ('Price per cup is: ', self.cup_cost)

        return self.pitchers
        
    def balance(self):
        self.total_cost = self.lemons_cost + self.sugar_cost + self.ice_cost
        if self.total_cost > 100:
            print (' Remember Dont You have only 100 ')
            print (' Please try again ')
            stand = Store()
            return
            
        else:    
            print (' Your total Cost is :', self.total_cost)
            self.new_balance = self.cash - self.total_cost
            print (' Your Balance is :  ', self.new_balance)      
            return self.new_balance

    def choices(self):
        lemonade = self.makelemonade()
        purch = self.purchase()
        co = self.cost()
        ba = self.balance()

st = Store()
choices = st.choices()    
#print (choices) 
print (self.p)