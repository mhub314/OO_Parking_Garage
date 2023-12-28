class ParkingGarage():
    """
        The ParkingGarage class will have tickets, parking spaces, and current tickets

        Attributes for the class:
        - tickets: list
        - parkingSpaces: list
        - currentTicket: dictionary  
    """

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    #Write a method that decreases the amount of tickets by 1
    #decreases the amount of parkingSpaces by 1
    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        tickets = len(self.tickets)
        spaces = len(self.parkingSpaces)
        print(f"There are {tickets} tickets and {spaces} spaces available.")
        
    #White a method that displays an input that waits for an amount
    #from the user and stores it in a variable
    #If the payment variable is not empty (meaning the ticket is paid),
    #display a message to the user that they have 15 mins to leave
    #This should update the currentTicket dictionary key "paid" to True
    def payForParking(self):
        pay = input("Thanks for parking. Input '5' to pay $5.  " )
        pay = str(pay)
        if pay == '5':
            self.currentTicket = True
            print("You have 15 minutes to exit.")


    #if ticket is paid, display "Thank you, have a nice day"
    #If not, display a prompt for payment
    #Update parkingSpaces list to increase by 1
    #Update tickets list to increase by 1
    def leaveGarage(self):
        self.tickets.append('ticket_3')
        self.parkingSpaces.append('space_3')
        tickets = len(self.tickets)
        spaces = len(self.parkingSpaces)
        print(f"Thank you. Have a nice day. There are now {tickets} tickets and {spaces} spaces available.")
        

parking_dict = {'paid': True}
parking = ParkingGarage(['ticket_1', 'ticket_2', 'ticket_3'], ['space_1', 'space_2', 'space_3'], parking_dict)

def run():
    while True:
        response = input("Press 'x' to PARK or press 'y' to PAY AND EXIT: ")

        if response.lower() == 'x':
            parking.takeTicket()

        elif response.lower() == 'y':
            parking.payForParking()
            parking.leaveGarage()
            break

        else:
            print("That won't work. Try again.")

run()