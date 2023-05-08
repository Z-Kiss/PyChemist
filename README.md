# **PyChemist**

It's a simple game where you can Brew Potions with Ingredients.

## **Toughts on the project**

The idea of the project came from one of the teamwork project that we did in CodeCool FullStack Developer course.
My goal was with this project to learn more about Python and Django Framework.

### **Built With**

    - Python
    - Django

### **Prerequisites**

  Python
  How to install: https://www.python.org/downloads/


### **Getting Started**

Before you start, you need to create a Virtual Environment
  - From the PyChemist directory run: "python venv venv"
  
Then you need to activate it
  - Enter the command "source venv/bin/activate" if you're on a Unix-based system
    or "venv\Scripts\activate.bat" if you're on a Windows system.
  
Then you need to install the requirements
 -  Enter the command "pip install -r requirements.txt"
 
 After you are done, you can start the application
  - Enter the command "python manage.py runserver"
 

### **Implemented Features**


#### _**Login/Register/Logout**_

    - You can do basic User interactions

##### _**Add Potion**_

    - You can Add a Potion by giveing a name, that after you can start Brewing 

##### _**Checkout your Potions**_

    - You can see all the potions that you are created 
      and from here you can start Brewing until it's done

##### _**Brew Potions**_

    - You can add Ingredients to the Potion until reaching 5 of it.
      When you reach 5 ingredient your potion is done.
      
    
### **Future plans**

  - Implememnt Feature about Recipes:
    After adding the fifth ingredient, the app will check
    if there is any Recipe with the same ingredients(order not count atm)
    If there is none, your potion will be a Original one and you can name the Recipe
  - Add Ingridients
  - Add scoring system, to feel the accomplishment :D
  - Better design
   
