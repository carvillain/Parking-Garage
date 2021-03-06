class parking():
    """
    Class creates a parking garage with functionality to enter, leave, and pay for tickets in accordance with
    garage standards
    """
    # {1 : [paid/unpaid, availability]}
    def __init__(self, tickets ={}, funds = 0):
        tickets = {1 : ['unpaid', 'available'],
        2 : ['unpaid', 'available'],
        3 : ['unpaid', 'available'],
        4 : ['unpaid', 'available'],
        5 : ['unpaid', 'available'],
        6 : ['unpaid', 'available'],
        7 : ['unpaid', 'available'],
        8 : ['unpaid', 'available'],
        9 : ['unpaid', 'available'],
        10 : ['unpaid', 'available'],
    }
        self.tickets = tickets
        self.funds = funds
    
    # Enter garage and take a ticket : Take a ticket out of pool : Mark a spot as occupied
    # Checks to see if garage is full/ returns available spots
    def enterGarage(self):
        check = 0
        avail_spots = []
        
        for x in self.tickets:
            if self.tickets[x][1] == 'available':
                self.tickets[x][1] = 'occupied'
                check = 1
                print(f'\nYour ticket is number {x}')
                break
        if check == 0:
            print("\nThere are no available spots")

        # Show how many spots are available
        for x in self.tickets.keys():
            if self.tickets[x][1] == 'available':
                avail_spots.append(x)
        print(f'\nAvailable Spots: {avail_spots}')

    
    # Opens up a spot : Check if paid : Opens a ticket
    # if not paid, transfers user to payment
    def leaveGarage(self):
        # Checks to see if input for ticket # can be converted to an integer
        tick = ''
        while type(tick) != int:
            try:
                tick = int(input("\nWhat is your ticket number? "))
            except:
                print("\nNot a valid ticket number")

        if self.tickets[tick][0] == 'unpaid':
            print("\nYou must pay to leave. Transferring you to payment options")
            self.payTicket()
        else:
            print("\nThank you for coming, have a great day!")
            self.tickets[tick][0] = 'unpaid'
            self.tickets[tick][1] = 'available'

    # Pay for ticket : Mark dict item as paid
    # Adds money to funds : Gives multiple payment options
    def payTicket(self):
        # Checks to see if input for ticket # can be converted to an integer
        tick = ''
        while type(tick) != int:
            try:
                tick = int(input("\nWhat is your ticket number? "))
            except:
                print("\nNot a valid ticket number")

        if self.tickets[tick][0] == 'unpaid' and self.tickets[tick][1] == 'occupied':
            paymethod = input("\nThat will be $5 for cash or $6 for credit. What method would you like to use today? ")

            if paymethod == 'cash':
                bills = input("\nPlease insert $5 (type $5): ")

                if bills == '$5':
                    print("\nThank you for paying. Please vacate within 15 minutes.")
                    self.tickets[tick][0] = 'paid'
                    self.funds += 5
                else:
                    print("\nYou have entered an incorrect amount, please try again.")

            else:
                card = input("\nPlease insert your credit card. (type 'insert') ")
                if card == 'insert':
                    print("\nPayment accepted, thank you. Please vacate within 15 minutes.")
                    self.tickets[tick][0] = 'paid'
                    self.funds += 6
                else:
                    print("\nERROR, please reinsert your card.")

        elif self.tickets[tick][1] != 'occupied':
            print("\nNot a valid ticket number")

        else:
            print("\nThank you for coming, your ticket is already paid for")

    # Returns total amount of money made for the day when program is quit using passcode
    def printFunds(self):
        password = input("\nPlease enter the passcode: ")
        if password == "0000":
            print(f'\nHere is how much money we made today: ${self.funds}')
        else:
            print("\nIncorrect passcode")


def run():

    random = parking()
    while True:
        response = input("\nWhat would you like to do? Enter/Leave/Pay: ")
    
        if response.lower() == 'enter':
            random.enterGarage()

        elif response.lower() == 'leave':
            random.leaveGarage()

        elif response.lower() == 'pay':
            random.payTicket()
        
        elif response.lower() == 'admin':
            random.printFunds()
            break
        
run()