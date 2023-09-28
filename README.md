# Project Setup

Before running the Django project, ensure you have set up the necessary environment variables and virtual environment.

### Step 1: Create `.env` file

Create a `.env` file and populate it with the required variables following the structure outlined in `.env.example`.

### Step 2: Create Virtual Environment

Create a virtual environment using the following command:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Run Django Project

Run the Django project with the following command:

```bash
python manage.py runserver
```

### Docker Compose

To run the project using Docker, follow these steps:

1. Build the Docker image:

```bash
docker-compose build
```

2. Run the Docker container:

```bash
docker-compose run --rm app
```

3. Start the Docker container:

```bash
docker-compose up
```

4. Access the Django app in the Docker container:

```bash
docker exec -it django_app sh
```

5. Run Django migrations in the Docker container:

```bash
python manage.py migrate
```

6. Restart the Docker container after migrations:

```bash
docker-compose up
```

---

Copy and paste the above content into your README.md file for clear instructions on setting up and running your Django project.
