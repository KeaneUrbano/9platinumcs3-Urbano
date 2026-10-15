class publication:
    def __init__(self, title: str, author: str): # This is the main parent class
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\n")

class Book(publication):
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author)
        self.number_pages = abs(number_pages)
    def display_info_book(self): # I used \n so it prints both title and author on different lines and so it matches sample output
        print(f"Title: {self.title}, \nAuthor:{self.author}\nNumber of Pages: {self.number_pages}\n")

class Magazine(publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.issue_number = abs(issue_number)
    def display_info_magazine(self): # I used \n so it prints both title and author on different lines and so it matches sample output
        print(f"Title: {self.title}, \nAuthor: {self.author}\nIssue Number: {self.issue_number}\n")


publication2 = publication("Verity", "Colleen Hoover")
book2 = Book("Hunger Games", "Suzanne Collins", -200) # I used negative number to show that the function works.
magazine2 = Magazine("New York Times", "Michael Jack", 12)

print("Publication 1 Info:")
publication2.display_info()
print("Book 1 Info:")
book2.display_info_book()
print("Magazine 1 Info:")
magazine2.display_info_magazine()

# I used abs function so the pages are always returned as positive numbers.
