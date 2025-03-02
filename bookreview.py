import pymongo as pm

client = pm.MongoClient('mongodb://localhost:27017/')
db = client['Book_Review']
collection = db['books']

book_value = {'title': '', 'author': '', 'genre': [], 'review': []}
review_value = {'name': '', 'rating': 0, 'body': ''}

def insert_book():
    title = input("Enter the Title of the Book:").lower()
    existing_book = collection.find_one({'title': title})
    if existing_book:
        print(f"The book '{title}' already exists.")
        option = input(f"Do you want to give a new review for {title} book? (y/n): ")
        if option.lower() == 'y':
            review_value['name'] = input("Enter your name: ")
            review_value['rating'] = float(input("Enter the Rating of the Book: "))
            review_value['body'] = input("Enter your Review on the Book: ")
            collection.update_one({'title': title,}, {'$push': {'review': review_value.copy()}})
            print("Book Review is Given Successfully")
        else:
            print("Review not added.")
    else:
        book_value['title'] = title
        book_value['author'] = input("Enter the Author of the Book: ")
        i = 'Y'
        while i == 'Y' or i == 'y': 
            genre = input("Enter the genre of the Book: ")
            book_value['genre'].append(genre)
            choose = input("Do you want to insert more genres (y/n): ")
            if choose.lower() == 'n':
                i = 'N'
            elif choose.lower() == 'y':
                i = 'Y'
            else:
                print("Invalid Choice!")
            
        print("Your Review matters!")
        review_value['name'] = input("Enter your name: ")
        review_value['rating'] = float(input("Enter the Rating of the Book: "))
        review_value['body'] = input("Enter your Review on the Book: ")
        book_value['review'].append(review_value.copy())
        
        collection.insert_one(book_value)
        print("Book Review is Given Successfully")


def update_book(name):
    print(f"Hi {name} !")
    title=input("Enter the book Name:").lower()
    existing_book=collection.find_one({'title':title})
    if existing_book:
        existing_review=collection.find_one({'review.name': name})
        if existing_review:
               review_value['name']=input("Enter Your Name:")
               review_value['rating']=float(input("Enter Your Rating of the Book:"))
               review_value['body']=input("ENter the Review of the Book:")
               collection.update_one({'title': title,'review.name':name}, {'$set': {'review': review_value.copy()}})
               print("Updation Done Successfully!")
        else:
            print(f"Hi {name} your review is not be found")
            choose=input("Would you like to give a review on the Book(y/n):")
            if choose.lower() == 'y':
                insert_book()
    else:
        print(f"There is no review of the book")
        choose=input("Would You like to review the book(y/n):")
        if choose.lower()=='y':
            insert_book()
        else:
            print('exiting......')
    

def delete_book(name):
        title = input("Enter the book name to delete your review: ").lower()
        existing_review = collection.find_one({'title': title, 'review.name': name})
        if existing_review:
             collection.update_one({'title': title}, {'$pull': {'review': {'name': name}}})
             print("Book Review Deleted Successfully!")
        else:
             print(f"No review found for {name} on the book '{title}'.")


def view_book(title):
    title = title.lower()
    book = collection.find_one({'title': title})
    if book:
        print(f"\nTitle: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Genres: {', '.join(book['genre'])}")
        print("Reviews:")
        print(book['review'])

print("-- Book Reviews --")

exit = True
while exit:
    print("1. Give a Review on a Book\n2. Update Your Review\n3. View Reviews\n4. Delete Your Reviews\n5. Exit")
    choice = int(input("Enter Your Option (Enter the Number):"))
    if choice == 1:
        insert_book()
    elif choice == 2:
        name = input("Enter Your Name to Update your review:")
        update_book(name)
    elif choice == 3:
        title = input("Enter the book you're trying to find:")
        view_book(title)
    elif choice == 4:
        name = input("Enter Your Name:")
        delete_book(name)
    elif choice == 5:
        exit = False
    else:
        print(f"Invalid Choice {choice}")

print("Exiting Book Reviews.")
