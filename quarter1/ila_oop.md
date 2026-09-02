 # ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
   Encapsulation bundles data and methods (behaviors) into a single class, leaving no access to an object's 
internal state using private access modifiers. In a sari-sari store system, a Product class can encapsulate properties 
like product_name, price, and quantity, making them private while providing getter and setter methods to access or modify them. 
For instance, a sell_product(amount) method can check if enough stock exists before removing from quantity, preventing invalid
direct edits like setting inventory to a negative number. This improves design security and keeps state management clean and controlled.

```
class Product:
    def __init__(self, name, price, stock):
        self.__name = name        # Private property
        self.__price = price      # Private property
        self.__stock = stock      # Private property

    def update_stock(self, amount):
        if self.__stock + amount >= 0:
            self.__stock += amount
        else:
            print("Error not enough stock!")
```

### 2. Abstraction
Abstraction hides complex background details and only shows the essential features required by the user. 
In the inventory system, a StoreManager or Inventory object can expose simple methods like checkout_item() or generate_sales_report() 
while hiding complex actions inside those methods. The main program loop simply calls inventory.add_product() 
without needing to know how somethings are handled behind the scenes. This reduces system complexity while leaving
space for the program to be easily maintained.

```
class Stock:
    def add_product(self, product)   Here user only sees available stock, as they don't need to see calculation mechanics and behind the scene.
        self.__product_list.append(product)

    def display_available_items(self): User only sees simple output formatting logic is hidden inside
```

### 3. Inheritance
Inheritance is named inheritance as it allows an existing class to get the properties and methods of a prior class. As an example class Product may have 
properties like name price and stock while specialized classes would have the same properties while adding some of their own.
This prevents code duplication and makes expanding the inventory system with new product categories fast and structured.

```
Parent Class:                   Subclass/Childclass
Product:                        SacheStrip:
(name, price, qty.) --------->    (name, price, qty, amount_per_strip.)

```

### 4. Polymorphism
  Polymorphism allows objects that is derived from other classes to be treated under a common parent class. They still respond to the same method call 
  in their own way. As an example in the sari sari store system, both standardproduct(example of class) and  perishableproduct can share a calculate_discount 
  method from class product. But PerishableProduct can ignore this method to automically apply a 30% discount if the item is close to its expiration date.
  In short it allows different classes to share same methods with their own way to deal with it. 

```
Example:
class Product:
  def calculate discount(self)
    l
    l
    V
class PerishableProduct(Product):
    def calculate discount(self):
       
        if self.is_near_expiry():
            return self.price * 0.70
        return self.price

```

### Reflection
Among the four pillars of Object-Oriented Programming, I think Encapsulation would be the most useful pillar in improving the sari-sari store inventory system. 
Looking at it a different way, stock quantities and prices are stored in many variables or scattered list that can easily be altered incorrectly by any part of the program.
Encapsulation ensures that vital business logic such as verifying that stock never drops below zero and prices remain positive.
Protecting these data fields from accidental modification makes the system significantly more reliable, secure, maintain, and easier to understand.
