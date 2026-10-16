class publication:
    def __init__(self, title: str, author: str): # This is the main parent class
        self.__title = title # We create 2 private attributes for publication class.
        self.__author = author


    def get_title(self):
        return self.__title
# These are getters and setters for both title and author where once checked and accessed returns the value.
    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author
# The author and title attribute along with its getter and setter will also be inherited by book and magazine.
    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}\nAuthor: {self.__author}\n") # This prints its info and I added \n so it looks better. This will also be inherited.

class Book(publication):
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author) # We use super() function to inherit common attributes between book and publication
        self.__number_pages = number_pages
        self.set_number_pages(number_pages)  # This is where we create setter method to get number_pages
        
    def get_number_pages(self): # A getter method to return self.__number_pages when used.
        return self.__number_pages

    def display_info(self): # We create a method that prints its info and pages by using super() function to get the earlier display_info traits.
        super().display_info() # This prints the details of the book object.
        if self.__number_pages <= 0: # This checks if the number of pages is less than or equal to 0 and prints a message if it is.
            print(f"Number of pages must be positive.")
            print(f"Number of pages: {abs(self.__number_pages)}\n")
        else: # If it is more than 0 then it prints the number of pages.
            print(f"Number of pages: {self.__number_pages}")
      
    def set_number_pages(self, number_pages): # We define the setter method
        self.__number_pages = number_pages # If it is more than zero it prints the number of pages.

class Magazine(publication):
    def __init__(self, title: str, author: str, issue_number: int): # We create its attributes using __init__
        super().__init__(title, author) # This inherits the instructions for the common attributes between title and author.
        self.__issue_number = 0 
        self.set_issue_number(issue_number) # This creates a setter for issue number.

    def get_issue_number(self): # This is a getter method for issue number that returns the value.
        return self.__issue_number

    def set_issue_number(self, issue_number): # This is a setter that checks if the magazine issue number is more or less than 0.
        if issue_number <= 0:
            print("Issue number must be positive.")
        else: # If issue number is below zero it prints that it must be postive.
            self.__issue_number = issue_number # If nothing wrong it goes on without printing.

    def display_info(self):
        super().display_info()
        print(f"Issue number:{self.__issue_number}") # Just like in book class we inherit display info and added issue number attribute.

# Example usage
publication2 = publication("Verity", "Colleen Hoover")
book2 = Book("Hunger Games", "Suzanne Collins", -200) # Just like in sample output this will check what happens if code is negative.
magazine2 = Magazine("New York Times", "Michael Jack", 12)

print("Publication 1 Info:")
publication2.display_info()
print("Book 1 Info:")
book2.display_info() # This part tests the code through 1 object of each class and prints their info.
print("Magazine 1 Info:")
magazine2.display_info()
