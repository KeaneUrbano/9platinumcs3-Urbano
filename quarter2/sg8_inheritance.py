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
        self.number_pages = abs(number_pages)

    def get_number_pages(self):
        if self.number_pages <= 0:
            self.number_pages = abs(self.number_pages)
        return self.number_pages
    def set_number_pages(self, number_pages: int):
        if number_pages <= 0:
            number_pages = abs(number_pages)
        self.number_pages = number_pages
    def display_info_book(self): # I used \n so it prints both title and author on different lines and so it matches sample output
        print(f"Title: {self.title}, \nAuthor:{self.author}\nNumber of Pages: {self.number_pages}\n")

class Magazine(publication):
    def __init__(self, issue_number: int, title: str, author: str): # Just like the book case it both has title and author.
        super().__init__(title, author)
        self.issue_number = abs(issue_number)

    def get_issue_number(self):
        if self.issue_number <= 0:
            self.issue_number = abs(self.issue_number)
        return self.issue_number
    def set_issue_number(self, issue_number: int):
        if issue_number <= 0:
            issue_number = abs(issue_number)
        self.issue_number = issue_number
    def display_info_magazine(self): # I used \n so it prints both title and author on different lines and so it matches sample output
        print(f"Title: {self.title}, \nAuthor: {self.author}\nIssue Number: {self.issue_number}\n")


publication2 = publication("Verity", "Colleen Hoover")
book2 = Book(-200, "Hunger Games", "Suzanne Collins") # I used negative number to show that the function works.
magazine2 = Magazine(12, "New York Times", "Michael Jack")

print("Publication 1 Info:")
publication2.display_info_publication()
print("Book 1 Info:")
book2.display_info_book()
print("Magazine 1 Info:")
magazine2.display_info_magazine()

# I used abs function so the pages are always returned as positive numbers.
