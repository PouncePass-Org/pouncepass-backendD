# PouncePass Backend

This repository contains the Django backend for PouncePass. The project utilizes SQLite3 for the database and is designed to work with a React frontend.

## Prerequisites

Ensure you have the following installed on your machine:

- Python (3.8 or newer is recommended)
- pip (Python's package installer)

## Setup

1. **Clone the repository, then navigate to it:**
    ```bash
    git clone https://github.com/your-username/pouncepass-backendD.git
    cd pouncepass-backendD
    ```

2. **Set up a virtual environment (optional but recommended. lets you have an environment specific to this project):**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the Django project:**
    - Update `pouncepass_backendD/settings.py` with your configuration if needed.
    - Ensure `DEBUG` is set to `True` for development, and `False` for production.
    - Update `ALLOWED_HOSTS` with the appropriate host(s) for your environment.

5. **Initialize the database:**
    ```bash
    python manage.py migrate
    ```

6. **Create an admin user:**
    ```bash
    python manage.py createsuperuser
    ```
    - Follow the prompts to create an admin user.

7. **Collect static files (if any):**
    ```bash
    python manage.py collectstatic --noinput
    ```

## Running the Backend

1. **Start the Django server:**
    ```bash
    python manage.py runserver
    ```

2. **Access the Django Admin Interface:**
    - Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with the admin user credentials you created earlier.

3. **Access the API:**
    - The API can be accessed at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Additional Information

- Default Admin Login Info (if needed):
    - Email: dev@dev.com
    - Phone number: 0000000000
    - Password: dev

## Troubleshooting

- Ensure all dependencies are correctly installed.
- Check the Django and database configurations in `pouncepass_backendD/settings.py`.

## IMPORTANT, please follow:

- ### Always use a feature branch, made from the development branch, when contributing. Follow best practices.
- ### Always test your code before submitting a pull request.
- ### Always make sure your code is well documented unless it is very self-explanatory.
- 
## License

[MIT License](LICENSE)
