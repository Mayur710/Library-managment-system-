class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books for you: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-book database has been updated. You can take your book now")
        else:
            print(f"{self.lendDict[book]} is using this book right now")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    mauyr = Library(["Poor dad Rich dad", "Harry potter all series", "Learning python in hard way",
                     "Principles of a genius", "The theory of everything"], "Verma")

    while(True):
        print(f"Welcome to the {mauyr.name} library. Enter your choice to continue")
        print("1) Display books")
        print("2) Lend a book")
        print("3) Add a book")
        print("4) Return a book")
        user_choice = int(input("Write number given in front of choices to proceed further \n >>"))

        if user_choice == 1:
            mauyr.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: \n >>")
            user = input("Enter your name also \n >>")
            mauyr.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: \n >>")
            mauyr.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return \n >>")
            mauyr.returnBook(book)

        else:
            print("Not a valid option")

        print("Press 'q' to quit and 'c' to continue ")
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input(">>")
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue

