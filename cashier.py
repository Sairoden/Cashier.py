class cashier:

    def __init__(self, a=0, r=0, recieve=0, change=0, temp=0):

        print("\n\n*****WELCOME TO THE RESTAURANT*****\n---- How may I help you?----\n")

        self.a = a
        self.r = r
        self.recieve = recieve
        self.change = change
        self.temp = temp

    def foods(self):

        print("*****RESTAURANT MENU*****")

        print("1.Ramen----->120", "\n2.Beef stew----->170", "\n3.Fried Chicken--->80", "\n4.Ice Cream---->50",
              "\n5.Cash Out", "\n6.Exit")

        while (1):

            c = int(input("Choose:\n"))

            if (c == 1):

                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 30 * d

            elif (c == 2):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 35 * d

            elif (c == 3):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 50 * d

            elif (c == 4):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 40 * d

            elif (c == 5):
                print("total:", self.r)
                if (self.r > 0):
                    recieve = int(input("Please enter payment:\n"))
                    print("Change:", recieve - self.r)
                    print("*****Thank You Come Again, I hope you enjoyed it!*****")
                    quit()
            elif (c == 6):
                quit()
            else:
                print("Invalid option")


def main():
    a = cashier()

    while (1):
        a.foods()


main()
