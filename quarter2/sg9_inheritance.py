class publication:
    def __init__(self, title: str, author: str): # This is the main parent class
        self.title = title
        self.author = author

    def get_title(self):
        return self.title
    def get_author(self):
        self.author = author    
        return self.author
    def set_title(self, title: str):
        self.title = title
    def set_author(self, author: str):
        self.author = author
    def display_info(self): # I used \n so it prints both title and author on different lines and so it matches sample output
        print(f"Title: {self.title}, \nAuthor: {self.author}\n")

class Book(publication):
    def __init__(self, number_pages: int, title: str, author: str): # I used inheritance/super() function because both book and publivation has title and author.
        super().__init__(title, author)
        self.number_pages = number_pages

    def get_number_pages(self):
        return self.number_pages
    def set_number_pages(self, number_pages: int):
        self.number_pages = number_pages

class Magazine(publication):
    def __init__(self, issue_number: int, title: str, author: str): # Just like the book case it both has title and author.
        super().__init__(title, author)
        self.issue_number = issue_number

    def get_issue_number(self):
        return self.issue_number
    def set_issue_number(self, issue_number: int):
        self.issue_number = issue_number

publication1 = publication("1984", "George Orwell") # example case where I used all clases.
publication2 = publication("Verity", "Colleen Hoover")
book2 = Book(200, "Hunger Games", "Suzanne Collins")
book1 = Book(123, "How to Win a World Cup", "Chris Evan") 
magazine1 = Magazine(45, "National Geographic", "Jack Russell")
magazine2 = Magazine(12, "New York Times", "Michael Jack")

print("Publication 1 Info:")
publication1.display_info() # Using the display_info method to print everything
print("Publication 2 Info:")
publication2.display_info()
print("Book 1 Info:")
book1.display_info()
print("Book 2 Info:")
book2.display_info()
print("Magazine 1 Info:")
magazine1.display_info()
print("Magazine 2 Info:")
magazine2.display_info()
