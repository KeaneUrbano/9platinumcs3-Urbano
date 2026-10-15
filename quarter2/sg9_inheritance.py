class publication:
    def __init__(self, title: str, author: str): # This is the main parent class
        self.title = title
        self.author = author

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def set_title(self, title: str):
        self.title = title
    def set_author(self, author: str):
        self.author = author
    def display_info_publication(self): # I used \n so it prints both title and author on different lines and so it matches sample output
        print(f"Title: {self.title}, \nAuthor: {self.author}\n")

class Book(publication):
    def __init__(self, number_pages: int, title: str, author: str): # I used inheritance/super() function because both book and publivation has title and author.
        super().__init__(title, author)
        self.number_pages = number_pages

    def get_number_pages(self):
        return self.number_pages
    def set_number_pages(self, number_pages: int):
        self.number_pages = number_pages
    def display_info_book(self): # I used \n so it prints both title and author on different lines and so it matches sample output
        print(f"Title: {self.title}, \nAuthor:{self.author}\n Number of Pages:{self.number_pages}\n")

class Magazine(publication):
    def __init__(self, issue_number: int, title: str, author: str): # Just like the book case it both has title and author.
        super().__init__(title, author)
        self.issue_number = issue_number

    def get_issue_number(self):
        return self.issue_number
    def set_issue_number(self, issue_number: int):
        self.issue_number = issue_number
    def display_info_magazine(self): # I used \n so it prints both title and author on different lines and so it matches sample output
        print(f"Title: {self.title}, \nAuthor: {self.author}\n Issue Number:{self.issue_number}\n")

a = str(input("Enter title of publication 1: "))
b = str(input("Enter author of publication 1: "))

c = str(input(f"\nEnter title of Book 1: "))
d = int(input("Enter number of pages for Book 1: "))

if d <= 0:
    print(f"\nNumber of pages must be a positive integer.")
    d = int(input("Enter number of pages for Book 1:"))
    if d <= 0:
        while d <= 0:
            print(f"\nNumber of pages must be a positive integer.")
            d = int(input("Enter number of pages for Book 1: "))

e = str(input(f"\nEnter author of Book 1: "))

f = str(input(f"\nEnter title of Magazine 1: "))
g = int(input("Enter issue number for Magazine 1: "))
if g <= 0:
    print(f"\nIssue number must be a positive integer.")
    g = int(input(f"Enter issue number for Magazine 1: "))
    if g <= 0:
        while g <= 0:
            print(f"\nIssue number must be a positive integer.")
            g = int(input(f"Enter issue number for Magazine 1: \n"))

h = str(input("Enter author of Magazine 1: "))

publication1 = publication(a, b) # example case where I used all classes. But some are input by user to see it in action.
publication2 = publication("Verity", "Colleen Hoover")
book2 = Book(200, "Hunger Games", "Suzanne Collins")
book1 = Book(d, c, e)
magazine1 = Magazine(g, f, h)
magazine2 = Magazine(12, "New York Times", "Michael Jack")

print("Publication 1 Info:")
publication1.display_info_publication() # Using the display_info method to print everything
print("Publication 2 Info:")
publication2.display_info_publication()
print("Book 1 Info:")
book1.display_info_book()
print("Book 2 Info:")
book2.display_info_book()
print("Magazine 1 Info:")
magazine1.display_info_magazine()
print("Magazine 2 Info:")
magazine2.display_info_magazine()


