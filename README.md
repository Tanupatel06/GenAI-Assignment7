 Assignment 7: Object-Oriented Programming (OOP) in Python

## 📌 Project Overview

This assignment focuses on understanding and implementing the fundamental concepts of Object-Oriented Programming (OOP) using Python.

The problem statement is based on an online electronics store that wants to organize product information, manage billing operations, and handle inventory using OOP concepts.

The assignment consists of seven tasks, starting with basic class and object creation and progressing towards a simple Inventory Management System.

## 🎯 Objectives
#
- Understand classes and objects in Python.
- Learn constructors and attributes.
- Implement encapsulation using private attributes.
- Understand inheritance and method overriding.
- Explore polymorphism and abstraction.
- Implement magic methods and operator overloading.
- Develop a simple inventory management system using OOP.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **IDE:** Visual Studio Code
- **Version Control:** Git and GitHub
- **Concepts:** Object-Oriented Programming

## 📂 Project Structure

```text
Assignment-7-OOP/
│
├── README.md
│
├── Task_1_Class_Object.py
├── Task_2_Encapsulation.py
├── Task_3_Inheritance.py
├── Task_4_Polymorphism.py
├── Task_5_Abstraction.py
├── Task_6_Magic_Methods.py
│
└── Task_7_Inventory_System.py
```

## 📚 Assignment Tasks

### Task 1: Basic Class & Object Creation

- Created a `Product` class.
- Defined attributes: `name`, `price`, and `category`.
- Implemented `get_info()` to display product details.
- Created two product objects.
- Added an optional `apply_discount(percent)` method to calculate discounted prices.

### Task 2: Constructor & Encapsulation

- Used the `__init__()` constructor.
- Made the price attribute private using `__price`.
- Implemented getter and setter methods.
- Added validation to update the price only when the new price is greater than zero.

### Task 3: Inheritance (Single-Level)

- Created an `ElectronicProduct` child class inheriting from `Product`.
- Added a `warranty_years` attribute.
- Used `super()` to call the parent class constructor.
- Overrode the `get_info()` method to include warranty information.

### Task 4: Polymorphism

- Created `Laptop` and `Mobile` classes inheriting from `Product`.
- Overrode the `get_info()` method in both classes.
- Used a loop to iterate through different objects.
- Demonstrated polymorphism through different outputs of the same method.

### Task 5: Abstraction

- Created an abstract base class named `Payment`.
- Defined an abstract method `process_payment(amount)`.
- Implemented two subclasses:
  - `CreditCardPayment`
  - `UPIPayment`
- Demonstrated abstraction using simple payment messages.

### Task 6: Magic Methods & Operator Overloading

- Implemented the `__str__()` magic method to display readable product information.
- Implemented the `__add__()` magic method.
- Overloaded the `+` operator to calculate the combined price of two product objects.

### Task 7: Mini Project – Simple Inventory System

Developed a simple inventory management system using two main classes.

**1. Inventory Class**

- Stores product objects in a list.
- `add_product()` adds products.
- `remove_product()` removes products by name.
- `get_total_value()` calculates the total inventory value.
- `show_all_products()` displays all product details.

**2. Store Class**

- Stores the store name.
- Maintains an Inventory object.
- `add_new_product()` takes user input and creates Product objects.
- `show_summary()` displays the total number of products and inventory value.

**Testing performed:**

- Created a Store object.
- Added three products.
- Displayed all

## 👩‍💻 Author

**Tanu Patel**  
Computer Science & Engineering (CSE) Student  

⭐ *Learning Python one concept at a time through practical implementation!*
