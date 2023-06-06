# User Authentication System with MongoDB

This is a user authentication system implemented using Django and MongoDB as the database. The project provides functionalities for user registration, login, logout, and session management.

## Prerequisites

Before running the project, make sure you have the following requirements:

- Python 3.x installed on your system
- Django framework installed
- MongoDB installed and running

## Installation

1. Clone the project repository from GitHub:

   ```
   git clone https://github.com/aminbista6666/mongo-login.git
   ```

2. Install the required Python packages. In the project directory, run:

   ```
   pip install -r requirements.txt
   ```

3. Configure the MongoDB connection settings. Open the `mongodb.py` file and update the `settings.MONGO_DB['connection_uri']` variable with the appropriate MongoDB connection URI.

## Usage

To start the Django development server and run the project, follow these steps:

1. Navigate to the project directory:

   ```
   cd user-authentication-system-mongodb
   ```

2. Start the development server:

   ```
   python manage.py runserver
   ```

3. Open your web browser and access the application at `http://localhost:8000`.

## Functionality

The user authentication system provides the following functionality:

- **Register**: Users can create an account by providing their email, password, and confirm password.
- **Login**: Registered users can log in using their email and password.
- **Logout**: Logged-in users can log out of their account.
- **Session Management**: The system manages user sessions and stores them in MongoDB. Sessions have an expiration time of 5 minutes.

## Project Structure

The project files are organized as follows:

- `helper.py`: Contains helper functions for creating user objects and authenticating users.
- `middleware.py`: Defines custom middleware classes for session management and authentication.
- `mixins.py`: Includes mixins for access control and permission handling.
- `mongodb.py`: Provides functions to connect to the MongoDB database and access user and session collections.
- `password.py`: Contains functions for password hashing using the Argon2 algorithm.
- `validators.py`: Defines JSON schemas for validating user and session objects in MongoDB.
- `views.py`: Implements the views for user registration, login, logout, and protected content.
- `protected/`: Contains templates and views for protected content accessible only to logged-in users.
- `users/`: Includes templates and views for user authentication and account management.

## Contributing

Contributions to the project are welcome. If you encounter any issues or have suggestions for improvements, please create a new issue on the GitHub repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
