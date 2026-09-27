class Library:
    def __init__(self):
        self.books=["english","maths","biology"]
    def borrowing(self,book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("borrowing imposssible")
    def returning(self,book):
        self.books.append(book)
    def total_available_books(self):
        print(self.books)
        
lib=Library()
lib.borrowing("python")
lib.returning("java")
lib.total_available_books()