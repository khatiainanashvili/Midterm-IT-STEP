# წიგნების მართვის კონსოლ აპლიკაცია 
# შექმენით კონსოლ აპლიკაცია C# / Python-ში, რომელიც მომხმარებლებს საშუალებას აძლევს მართონ წიგნების სია.  
# თითოეულ წიგნს აქვს სათაური, ავტორი და გამოცემის წელი. მომხმარებელს უნდა შეეძლოს წიგნის დამატება, წიგნების სიის ნახვა და წიგნის სათაურის მოძიება. 
# განახორციელეთ შემდეგი ფუნქციები ობიექტზე ორიენტირებული პროგრამირების პრინციპების გამოყენებით: 
 
# 1. Book კლასი: 
# • შექმენით წიგნის კლასი შემდეგი თვისებებით: 
# o სათაური o ავტორი o გამოცემის წელი 
# 2. BookManager კლასი: 
# •	შექმენით BookManager კლასი წიგნების სიის სამართავად. 
# •	კლასი უნდა შეიცავდეს მეთოდებს: o ახალი წიგნის დამატება  სიაში. o ყველა წიგნის სიის ჩვენება. o წიგნის ძებნა მისი სათაურის მიხედვით. 
 
# 3. User Interface: 
# • კონსოლზე დაფუძნებული მომხმარებლის ინტერფეისის შემუშავება, რომელიც მომხმარებლებს საშუალებას აძლევს: 
# o	დაამატოს ახალი წიგნი მისი სათაურის, ავტორისა და გამოცემის წლის შეყვანით. 
# o	იხილეთ ყველა წიგნის დეტალური ინფორმაციის ნახვა. o წიგნის ძებნა მისი სათაურის შეყვანის გზით. 
 
# 4. Validaon 
 
# • განახორციელეთ შეყვანის ვალიდაცია, რათა დარწმუნდეთ, რომ მომხმარებელი შეიყვანს ვალიდურ ინფორმაციას. 
 
# 5. მაგალითი: 
# მოიყვანეთ მაგალითი იმის სადემონსტრაციოდ, თუ როგორ მუშაობს აპლიკაცია წიგნების დამატების, სიის დათვალიერებისა და წიგნის ძიების პროცესში. 
# შენიშვნა: გამოიყენეთ ობიექტზე ორიენტირებული პროგრამირების ცნებები, როგორიცაა კლასები და ობიექტები თქვენი კოდის სტრუქტურირებისთვის. ყურადღება მიაქციეთ ინკაფსულაციას, მემკვიდრეობას და პოლიმორფიზმს, სადაც ეს შესაძლებელია. 

class Book:
    def __init__(self, title, author, year):    
        self.title = title 
        self.author = author 
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class BookManager:
    def __init__(self):
        self.books = [

            Book("1984", "George Orwell", 1949),
            Book("To Kill a Mockingbird", "Harper Lee", 1960),
            Book("The Great Getsby", "F. Skott Fitzgerard", 1925)
        ]

    def add_book(self, title, author, year):
        if not title.strip() or not author.strip() or not year.strip():
            print("Error: All fields (title, author, and year) must be filled.")
            return

        try:
            year = int(year)
            new_book = Book(title.strip(), author.strip(), year)
            self.books.append(new_book)
            print(f"Book '{title}' added successfully!")
        except ValueError:
            print("Error: Year must be a valid integer.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in the library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print("\nSearch results:")
            for book in results:
                print(book)
        else:
            print(f"No books found with title containing '{title}'.")


def main():
    manager = BookManager()

    while True:
        print("\nBook Library CLI")
        print("1. Add New Book")
        print("2. See All Books List")
        print("3. Search by Title")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author's name: ").strip()
            year = input("Enter year of publication: ").strip()
            manager.add_book(title, author, year)
        elif choice == "2":
            manager.list_books()
        elif choice == "3":
            title = input("Enter the title to search: ").strip()
            manager.search_by_title(title)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()


    