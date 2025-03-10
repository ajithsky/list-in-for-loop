def display_menu():
    print("\nLibrary menu:")
    print("1.Add a Book")
    print("2.Display Book")
    print("3.Update price of Book")
    print("4.Delete Book")
def add_book(library):
    book_id=input("Enter Book id:")
    book_name=input("Enter Book name:")
    book_author=input("Enter Name of Author:")
    book_price=float(input("Enter price of Book:"))
    book_publisher=input("Enter name of publisher:")
    library[book_id]={"Book name":book_name,"Author":book_author,"Book price":book_price,"Publisher":book_publisher}
    print("Book added successfully!")
def display_book(library):
    if not library:
        print("Book not Available")
        return
    print("Books in Library:")
    for book_id,details in library.items():
        print(f"Book ID: {book_id},book_name:{details['Book name']},book author:{details['Author']},book price:{details['Book price']},book publisher:{details['Publisher']}")
def update_price(library):
    book_id = input("Enter Book ID to update the price: ")
    if book_id in library:
        new_price = float(input("Enter the new price: "))
        library[book_id]["Book price"] = new_price
        print(f"Price updated successfully! New price is {new_price}")
    else:
        print("Book ID not found.")
def delete_book(library):
    delete_id=input("Enter the id to delete:")
    if delete_id in library:
        del library[delete_id]
        print("Book deleted Successfully")
    else:
        print("Book id not found")
def main():
    library={}
    while True:
      display_menu()
      choice=int(input("Enter your choice:"))

      if choice==1:
        add_book(library)
      elif choice==2:
        display_book(library)
      elif choice==3:
        update_price(library)
      elif choice==4:
        delete_book(library)
      elif choice==5:
        print("Exited successfully")
        break
      else:
        print("Invalid choice")

main()