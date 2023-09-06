#!/usr/bin/env python3

from models import Base, User, UserProfile, Author, Book, Genre, engine
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Seed data for one-to-one relationship
user_profile = UserProfile(bio="A bio for the user")
user = User(username="Stephan_Maina", profile=user_profile)
session.add(user)
session.add(user_profile)  # You need to add user_profile as well
session.commit()

# Seed data for one-to-many relationship
author = Author(name="J.K. Rowling")
book1 = Book(title="Harry Potter and the Sorcerer's Stone", author=author)
book2 = Book(title="Harry Potter and the Chamber of Secrets", author=author)
session.add(author)
session.add(book1)  # Add book1 to the session
session.add(book2)  # Add book2 to the session
session.commit()

# Seed data for many-to-many relationship
fantasy_genre = Genre(name="Fantasy")
mystery_genre = Genre(name="Mystery")
book1.genres.extend([fantasy_genre, mystery_genre])
book2.genres.append(fantasy_genre)
session.add(fantasy_genre)  # Add genres to the session
session.add(mystery_genre)  # Add genres to the session
session.commit()

session.close()

