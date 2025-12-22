class Library:
    
    def __init__(self, name, location): #initializes library name, location, and book list.
        self.name = name
        self.location = location 
        self.books = []

    # Instance method
    def add_book(self, title, author):  
        self.books.append({"title": title, "author": author}) #Adds a book and updates total books.
       
        return f"Adding '{title}' to {self.name} library."

    # Instance method
    def display_info(self): #Shows library details.
        return f"{self.name} library at {self.location} "

# Create library objects
lib1 = Library("old Library", "Main Street")
lib2 = Library("new Library", "Park Avenue")

# Add books and display info
print(lib1.add_book("Amma diaryloni konni pageelu", "ravi"))
print(lib2.add_book("We never meant to be", "Palle vaasu"))
print(lib1.display_info())
print(lib2.display_info())

