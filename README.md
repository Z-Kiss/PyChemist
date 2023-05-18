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

      PostgreSQL
      How to install: https://www.postgresql.org/download/

### **Getting Started**

Before you start, you need to create a Virtual Environment
    - From the PyChemist directory run: "python -m venv venv"
  
Then you need to activate it
    - Enter the command "source venv/bin/activate" if you're on a Unix-based system
    or "venv\Scripts\activate.bat" if you're on a Windows system.
  
Then you need to install the requirements
    -  Enter the command "pip install -r requirements.txt"
 
For the application to be able to work you need to create a database
   - After installed the Postgresql you need to log in
   - Open a Terminal and enter the command "psql -U postgres"
   You need to use the password that you gave at the installation
   - After you logged in you need to enter the command "create database pychemist"

At this state of the application
you need to migrate the database relations that we defined in the model.py
    - From the PyChemist directory enter this commands
    - python manage.py makemigrations
    - python manage.py migrate

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
      
##### _**Register Recipe**_    
      
    - After the fifth ingredient if there is a Recipe with the same ingredient,
      if it is, it will connect the Recipe to the potion. Otherwise if there is no Recipe
      that contains the same ingredients, the Recipe shown and you can name it.
      
##### _**Original Potions**_

    - If there was Recipe that had the same Ingredients as the Potion, then the potion Original field became False.
      Otherwise it will became True showing that Potion was the first created by those Ingredients
      
    
### **Future plans**
    
  - Deepen "Game" logic
        - Ingredients will have cost
        - Random Ingredient spawn by "Trader"
        - You can Sell Potions
  - Add scoring system, to feel the accomplishment
  - Better design
  - Optimalize
  - Make code cleaner
   
