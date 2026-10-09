class Book:

    def __init__(self,):
        self.name=""
        self.bookID=""
        self.AuthorID=""
        self. publisher=""
        self.year=""


    def add_book(self):
        self.name= input("Enter book Name:")
        self.bookID= input("Enter book ID:")
        self.AuthorID= input("Enter Author ID:")
        self.publisher= input("Enter Publisher:")
        self.year= input("Enter Year:")
        print()

    def display_book(self):
        print("Name:", self.name)
        print("ID:", self.bookID)
        print("Author:", self.AuthorID)
        print("Publisher:", self.publisher)
        print("year of publication:", self.year)
        print()

class Author:
    def __init__(self):
        self.name=""
        self.ID=""
        self.affiliation=""
        self.country=""
        self.phone=""
        self.email=""

    def add_author(self):
        self.name= input("Enter Author Name:")
        self.ID= input("Enter Author ID:")
        self.affiliation= input("Enter Affiliation:")
        self.country= input("Enter Country:")
        self.phone= input("Enter Phone Number:")
        self.email= input("Enter E-Mail:")
        print()

    def display_author(self):
        print("Name:", self.name)
        print("ID:", self.ID)
        print("Affiliation:", self.affiliation)
        print("Phone Number:", self.phone)
        print("E-Mail:", self.email)
        print()

class User:
    def __init__(self):
        self.name=""
        self.userID=""
        self.password=""
        self.address=""
        self.phone=""
        self.email=""

    def add_user(self):
        self.name= input("Enter User Name:")
        self.userID= input("Enter User ID:")
        self.password= input("Enter Password:")
        self.address= input("Enter Address:")
        self.phone= input("Enter Phone Number:")
        self.email= input("Enter E-Mail:")
        print()

    def display_user(self):
        print("Name:", self.name)
        print("ID:", self.userID)
        print("Phone Number:", self.phone)
        print("E-Mail:", self.email)
        print()



#Main code
bookList=[]
authorList=[]
UserList=[]
while True:
    print("1 to access books, 2 to access authors, 3 to access users.")
    w=int(input())

    # books
    if w==1:
        book = Book()
        print("1 to create book, 2 to display books")
        q=int(input())
        if q==1:
            print("how many books do you want to add?:")
            AB = int(input())
            for i in range(AB):
                book.add_book()
                bookList.append(book)
        elif q==2:
            print("displaying books:")
            book.display_book()
        else:
            print ("invalid input")

    # authors
    elif w==2:
        ath = Author()
        print("1 to create authors, 2 to display authors")
        q=int(input())
        if q==1:
            print("how many author to add?:")
            AA = int(input())
            for i in range(AA):
                ath.add_author()
                authorList.append(ath)

        elif q==2:
            print("displaying authors:")
            ath.display_author()

        else:
            print("invalid input")

    # users
    if w==3:
        usr = User()
        print("1 to create users, 2 to display users")
        q=int(input())
        if q==1:
            print("how many new user are there?: ")
            AU = int(input())
            for i in range(AU):
               usr.add_user()
               usr.display_user()
        elif q==2:
            print("displaying users:")
            usr.display_user()

        else:
            print("invalid input")








