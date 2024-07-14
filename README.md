# User Authentication Project

This project is a Django-based web application that allows users to register, log in, and view their profile. The application uses email and password authentication.

## Features

- User Registration
- User Login
- User Profile
- User Logout
- Error Handling and Messages

## Technologies Used

- Django
- HTML
- CSS
- JavaScript
- Bootstrap
  ---
  #ScreenShots
  ![image](https://github.com/user-attachments/assets/3e15cdec-798c-4e57-866b-f5301480ea99)
  ![image](https://github.com/user-attachments/assets/bac98a6b-4cb5-4a59-bfbc-687e5da0d16f)


  

## Installation

1. **Clone the repository:**
    ```sh
    (https://github.com/Oviyan007/ZenHook-Login.git)]
    ```

2. **Navigate to the project directory:**
    ```sh
    cd your-ZenHook-Login
    ```

3. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

8. **Open your web browser and go to:**
    ```
    http://127.0.0.1:8000
    ```

## Usage

### Registration

1. Navigate to the registration page.
2. Fill in the registration form with your username, email, and password.
3. Submit the form to create a new account.

### Login

1. Navigate to the login page.
2. Enter your registered email and password.
3. Submit the form to log in.

### Profile

- After logging in, you will be redirected to your profile page where you can see a welcome message with your username.

### Logout

- Click on the "Logout" button on the profile page to log out.

## File Structure

