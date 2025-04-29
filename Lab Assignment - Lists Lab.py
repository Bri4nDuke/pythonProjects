#Lab Assignment -  Lists Lab
#By: Brian Duke
#Date: 4/09/2025
#This program - simple library management system using Python lists. This system will allow the user to add books to the library, check out books, and display the library's inventory.

def add_book(library):
    isbn = input("Enter ISBN: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    library.append({'ISBN': isbn, 'title': title, 'author': author, 'available': True})
    print("Book Added Successfully!")
    
def checkout_book(library):
    isbn = input("Enter ISBN: ")
    
    for book in library:
        if book['ISBN'] == isbn:
            if book['available']:
                book['available'] = False
                print("Enjoy Your Book!")  
                return
            else:
                print("Book is Currently Unavailable")
                return
    print("Book Not Found")

def display_library(library):
    print("\nAvailable Books:")
    if not library:
        print("The Library is Empty")
        return
    availableBooks = [book for book in library if book["available"]]
    if not availableBooks:
        print("No Books Available")
        return
    for book in availableBooks:
        print(f"ISBN: {book['ISBN']}, Title: {book['title']}, Author: {book['author']}")
        
def main():
    library = []
    while True:
        
        print("\n--- Library Menu: ---")
        print("1. Add Book")
        print("2. Checkout Book")
        print("3. Display Books")
        print("4. Exit")
        print("---------------------")

        
        menu = input("\nEnter 1-4: ")
        
        if menu == '1':
            add_book(library)
        elif menu == '2':
            checkout_book(library)
        elif menu == '3':
            display_library(library)
        elif menu == '4':
            print("Have a Good Day!")
            break
        else:
            print("ERROR: PLEASE ONLY PUT 1-4")
            
if __name__ == "__main__":
    main()