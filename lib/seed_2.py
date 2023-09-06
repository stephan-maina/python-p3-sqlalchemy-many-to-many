#!/usr/bin/env python3

from models import Base, User, UserProfile, Author, Book, Genre, engine
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Seed data for one-to-one relationship
user_profile1 = UserProfile(bio="A bio for the user 1")
user1 = User(username="Stephan_Maina", profile=user_profile1)

user_profile2 = UserProfile(bio="A bio for the user 2")
user2 = User(username="Alice_Smith", profile=user_profile2)

session.add_all([user1, user2, user_profile1, user_profile2])
session.commit()

# Seed data for one-to-many relationship
author1 = Author(name="J.K. Rowling")
author2 = Author(name="George R.R. Martin")

book1 = Book(title="Harry Potter and the Sorcerer's Stone", author=author1)
book2 = Book(title="Harry Potter and the Chamber of Secrets", author=author1)
book3 = Book(title="A Game of Thrones", author=author2)
book4 = Book(title="A Clash of Kings", author=author2)

session.add_all([author1, author2, book1, book2, book3, book4])
session.commit()

# Seed data for many-to-many relationship
fantasy_genre = Genre(name="Fantasy")
mystery_genre = Genre(name="Mystery")
sci_fi_genre = Genre(name="Science Fiction")

book1.genres.extend([fantasy_genre, mystery_genre])
book2.genres.extend([fantasy_genre, mystery_genre])
book3.genres.append(fantasy_genre)
book4.genres.append(sci_fi_genre)

session.add_all([fantasy_genre, mystery_genre, sci_fi_genre])
session.commit()

# Query data
# Query and print all users with their profiles
users_with_profiles = session.query(User).all()
for user in users_with_profiles:
    print(f'User: {user.username}, Bio: {user.profile.bio}')

# Query and print all authors with their books
authors_with_books = session.query(Author).all()
for author in authors_with_books:
    print(f'Author: {author.name}')
    for book in author.books:
        print(f'Book Title: {book.title}')

# Query and print all books with their genres
books_with_genres = session.query(Book).all()
for book in books_with_genres:
    print(f'Book Title: {book.title}')
    for genre in book.genres:
        print(f'Genre: {genre.name}')

session.close()
)
