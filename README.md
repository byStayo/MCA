The architecture of the system will be based on a Model-View-Controller (MVC) design pattern. The system will be developed using Python and the Flask web framework. The Google Sheets API will be used for integration with Google Sheets. The system will also use SQLAlchemy for database operations and Jinja2 for templating.

Here are the core classes, functions, and methods that will be necessary:

1. User class (models.py): This class will represent the user in the system. It will have methods for password hashing and verification.

2. Deal class (models.py): This class will represent a deal in the system. It will have methods for calculating commission.

3. UserController class (controllers.py): This class will handle user-related operations like registration, login, and profile management.

4. DealController class (controllers.py): This class will handle deal-related operations like submission, approval, and tracking.

5. GoogleSheetsService class (services.py): This class will handle the integration with Google Sheets.

6. main function (app.py): This function will be the entry point of the application. It will initialize the Flask app and the database, and register the routes.

Now, let's write the code for each file.

app.py
