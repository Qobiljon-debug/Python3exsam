# class BookRepository:
#     def __init__(self):
#         self._storage = {}
#         self._next_id = 1

#     def create(self, data):
#         title = data.get("title", "").strip()
#         year = data.get("year", 0)
#         price = data.get("price", 0.0)

#         if not title:
#             raise ValueError("Book title cannot be empty.")
#         current_year = 2026
#         if not (1000 <= year <= current_year):
#             raise ValueError(f"Book year must be between 1000 and {current_year}.")
#         if price <= 0:
#             raise ValueError("Book price must be greater than 0.")

#         book_id = self._next_id
#         self._next_id += 1

#         book = {"id": book_id, "title": title, "year": year, "price": price}
#         self._storage[book_id] = book
#         return book

#     def update(self, book_id, data):
#         if book_id not in self._storage:
#             raise KeyError(f"Book with ID {book_id} not found.")
        
#         book = self._storage[book_id]
        
#         if "title" in data:
#             title = data["title"].strip()
#             if not title:
#                 raise ValueError("Book title cannot be empty.")
#             book["title"] = title
            
#         if "year" in data:
#             year = data["year"]
#             current_year = 2026
#             if not (1000 <= year <= current_year):
#                 raise ValueError(f"Book year must be between 1000 and {current_year}.")
#             book["year"] = year
            
#         if "price" in data:
#             price = data["price"]
#             if price <= 0:
#                 raise ValueError("Book price must be greater than 0.")
#             book["price"] = price
            
#         return book

#     def delete(self, book_id):
#         if book_id in self._storage:
#             del self._storage[book_id]
#             return True
#         return False

#     def get_by_id(self, book_id):
#         return self._storage.get(book_id, None)

#     def get_all(self):
#         return list(self._storage.values())


# class AuthorRepository:
#     def __init__(self):
#         self._storage = {}
#         self._next_id = 1

#     def create(self, data):
#         full_name = data.get("full_name", "").strip()
#         birth_year = data.get("birth_year", 0)
#         country = data.get("country", "").strip()

#         if not full_name:
#             raise ValueError("Author full name cannot be empty.")
#         current_year = 2026
#         if birth_year >= current_year:
#             raise ValueError("Author birth year must be less than the current year.")

#         author_id = self._next_id
#         self._next_id += 1

#         author = {"id": author_id, "full_name": full_name, "birth_year": birth_year, "country": country}
#         self._storage[author_id] = author
#         return author

#     def update(self, author_id, data):
#         if author_id not in self._storage:
#             raise KeyError(f"Author with ID {author_id} not found.")
        
#         author = self._storage[author_id]
        
#         if "full_name" in data:
#             full_name = data["full_name"].strip()
#             if not full_name:
#                 raise ValueError("Author full name cannot be empty.")
#             author["full_name"] = full_name
            
#         if "birth_year" in data:
#             birth_year = data["birth_year"]
#             if birth_year >= 2026:
#                 raise ValueError("Author birth year must be less than current year.")
#             author["birth_year"] = birth_year
            
#         if "country" in data:
#             author["country"] = data["country"]
            
#         return author

#     def delete(self, author_id):
#         if author_id in self._storage:
#             del self._storage[author_id]
#             return True
#         return False

#     def get_by_id(self, author_id):
#         return self._storage.get(author_id, None)

#     def get_all(self):
#         return list(self._storage.values())


# # Task 1
# book_repo = BookRepository()
# author_repo = AuthorRepository()

# book_repo.create({"title": "Python 101", "year": 2020, "price": 29.99})
# book_repo.create({"title": "Data Structures", "year": 2018, "price": 45.50})
# book_repo.create({"title": "Algorithms", "year": 2021, "price": 50.00})

# author_repo.create({"full_name": "Alice Smith", "birth_year": 1985, "country": "USA"})
# author_repo.create({"full_name": "Bob Jones", "birth_year": 1990, "country": "UK"})
# author_repo.create({"full_name": "Charlie Brown", "birth_year": 1975, "country": "Canada"})

# print("All Books:", book_repo.get_all())
# print("All Authors:", author_repo.get_all())

# book_repo.update(1, {"price": 35.00})
# author_repo.update(2, {"country": "Scotland"})

# # Delete one of each
# book_repo.delete(3)
# author_repo.delete(3)

# try:
#     non_existing = book_repo.get_by_id(99)
#     if non_existing is None:
#         raise KeyError("Book not found.")
# except Exception as e:
#     print("Error caught:", e)

# print("All Books after updates/deletes:", book_repo.get_all())
# print("All Authors after updates/deletes:", author_repo.get_all())
# print("\n")



# class Publication:
#     def __init__(self, title, year):
#         self.title = title
#         self.year = year

#     def get_info(self):
#         return f"{self.title} ({self.year})"


# class Book(Publication):
#     def __init__(self, title, year, pages):
#         super().__init__(title, year)  # Call parent constructor
#         self.pages = pages

#     def get_info(self):
#         return f"Book: {super().get_info()}, {self.pages} pages"


# class Magazine(Publication):
#     def __init__(self, title, year, issue_number):
#         super().__init__(title, year)  # Call parent constructor
#         self.issue_number = issue_number

#     def get_info(self):
#         return f"Magazine: {super().get_info()}, issue #{self.issue_number}"


# #Task 2
# book = Book("Clean Code", 2008, 464)
# magazine = Magazine("Forbes", 2024, 7)

# print(book.get_info())
# print(magazine.get_info())

# print("Is book an instance of Publication?", isinstance(book, Publication))
# print("\n")




# class BankAccount:
#     def __init__(self, owner, initial_balance=0):
#         self.__owner = owner  
#         if initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative.")
#         self.__balance = initial_balance  

#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be greater than zero.")
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be greater than zero.")
#         if amount > self.__balance:
#             raise ValueError("Insufficient funds. Balance remains unchanged.")
#         self.__balance -= amount

#     def get_balance(self):
#         return self.__balance

#     def get_owner(self):
#         return self.__owner


# #Task 3
# account = BankAccount("Rustam", 100)
# account.deposit(50)
# print("Balance after deposit (150):", account.get_balance())

# try:
#     account.withdraw(200)
# except ValueError as e:
#     print("Caught expected error:", e)

# print("Balance after failed withdrawal (still 150):", account.get_balance())

# account.withdraw(30)
# print("Balance after valid withdrawal (120):", account.get_balance())

# account.balance = 1000000
# print("Secure private balance is still:", account.get_balance())
# print("\n")

# import math

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         return 0

#     def describe(self):
#         return f"{self.name}: area = {self.area():.2f}"


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__("Rectangle")
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__("Triangle")
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height




# class Square(Shape):
#     def __init__(self, side):
#         super().__init__("Square")
#         self.side = side

#     def area(self):
#         return self.side ** 2


# def total_area(shapes):
#     return sum(shape.area() for shape in shapes)


# #Task 4
# shapes_list = [Circle(3), Rectangle(4, 5), Triangle(6, 2), Square(5)]

# for shape in shapes_list:
#     print(shape.describe())

# print(f"Total area = {total_area(shapes_list):.2f}")
# print("\n")




# from abc import ABC, abstractmethod

# class Employee(ABC):
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     @abstractmethod
#     def calculate_salary(self):
#         pass

#     def show_info(self):
#         print(f"{self.get_name()}: salary = {self.calculate_salary()}")


# class FullTimeEmployee(Employee):
#     def __init__(self, name, monthly_salary):
#         super().__init__(name)
#         self.__monthly_salary = monthly_salary

#     def calculate_salary(self):
#         return self.__monthly_salary


# class PartTimeEmployee(Employee):
#     def __init__(self, name, hourly_rate, hours_worked):
#         super().__init__(name)
#         self.__hourly_rate = hourly_rate
#         self.__hours_worked = hours_worked

#     def calculate_salary(self):
#         return self.__hourly_rate * self.__hours_worked


# def total_payroll(employees):
#     return sum(emp.calculate_salary() for emp in employees)


# #Task 5
# try:
#     pass
# except TypeError:
#     print("Cannot instantiate abstract class Employee directly.")

# employees = [
#     FullTimeEmployee("Anna", 3000),
#     PartTimeEmployee("Bob", 20, 80)
# ]

# for emp in employees:
#     emp.show_info()

# print(f"Total payroll = {total_payroll(employees)}")