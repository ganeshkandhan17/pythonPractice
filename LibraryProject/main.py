class Library:
    def __init__(self, books):
        self.books = books
        self.availableBooks = books.copy()
        self.borrowedBooks = []
        self.userBookMapping = {}

    def getAllBooks(self):
        return self.books

    def getAvailableBooks(self):
        return self.availableBooks

    def printAllBooks(self):
        books = self.getAllBooks()
        index = 1
        for book in books:
            print(f'{index}. {book}')
            index+=1
        print('\n')

    def printAvailableBooks(self):
        books = self.getAvailableBooks()
        index = 1
        for book in books:
            print(f'{index}. {book}')
            index+=1
        print('\n')

    def getAvailableBookByIndex(self, index):
        if len(self.availableBooks) < index:
            return 'book not available'
        else:
            return self.availableBooks[index-1]

    def borrowBook(self,index,name):
        if len(self.availableBooks)< index:
            return False
        else:
            selectedBook = self.availableBooks[index-1]
            self.availableBooks.remove(selectedBook)
            self.borrowedBooks.append(selectedBook)
            self.userBookMapping[selectedBook] = name
            return True

    def printUserBookMapping(self):
        for key,value in self.userBookMapping.items():
            print(f'{key} : {value}')  

    def returnBook(self,index):
        selectedBook = self.borrowedBooks[index-1]
        self.availableBooks.append(selectedBook)
        del self.userBookMapping[selectedBook] 
        print(f'You successfully returned the {selectedBook} book')         

if __name__ == '__main__':
    with open('D:\\Coding Practice\\PythonPractice\\LibraryProject\\bookList.txt') as f:
        content = f.read()
        bookList = content.split(', ')
        library = Library(bookList)

    while True:
        print(f'1. Display available books')
        print(f'2. Display all books')
        print(f'3. Display borrowed books')
        print(f'4. Borrow a book')
        print(f'5. Return a book')
        print(f'6. Display borrowed books')
        print(f'7. Show user book mapping')
        print(f'8. Quit')

        try: 
            userChoice = int(input('Enter your choice (1-7) : '))
        except Exception as e:
            print(f'\nError: Enter value from 1-7\n')
            continue

        if userChoice == 8:
            print(f'Thank you for reached out our library')
            break
        if userChoice == 1:
            library.printAvailableBooks()

        if userChoice == 2:
            library.printAllBooks()

        if userChoice == 3:
            pass

        if userChoice == 7:
            library.printUserBookMapping()

        if userChoice == 4:
            library.printAvailableBooks()
            try:
                userBookSelection = int(input('Choose the book : '))
            except Exception as e:
                print('Enter valid number')
                continue
            selectedBook = library.getAvailableBookByIndex(userBookSelection)
            if selectedBook == 'book not available':
                print('Enter valid number')
            else:
                print(f'You selected {selectedBook}')
                userName = input('Enter your name : ')
                result = library.borrowBook(userBookSelection, userName)
                if result == True:
                    print(f'You successfully borrowed the {selectedBook}')   

        if userChoice == 5:
            print('Which book you want to return')
            index = 1
            for book in library.borrowedBooks:
                print(f'{index}. {book}')
                index+=1
            print('\n')
            try:
                userChoice = int(input("Enter the book  number your are returning: "))
                if userChoice > len(library.borrowedBooks):
                    print('Enter valid number: ')
                    continue
            except Exception as e:
                print('Enter valid number: ')
                continue
            library.returnBook(userChoice)

        if userChoice == 6:
            index = 1
            for book in library.borrowedBooks:
                print(f'{index}. {book}')
                index+=1
            print('\n')
            
            


            
            
