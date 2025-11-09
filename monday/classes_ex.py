class Book:
    def __init__(self,title:str,author:str,ISBN ):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.is_available=False

    def __str__(self):
        return f"title: {self.title}, author: {self.author} ISBN: {self.ISBN} is_available: {self.is_available}"
    

class User:
    def __init__(self,name:str,id:str,borrowed_books:list[Book]):
        self.name=name
        self.id=id
        self.borrowed_books=borrowed_books

class Library:
    def __init__(self):
        self.list_books:list[Book]=[]
        self.list_users:list[User]=[]

    def add_book(self,book):
        self.list_books.append(book)

    def add_user(self,user):
        self.list_users.append(user)

    def return_book(self,user_id, book_isbn):
        for i in self.list_users:
            for j in self.list_books:
                pass
