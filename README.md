# Project Manager Flask

This is a simple Flask application for managing projects. It provides CRUD (Create, Read, Update, Delete) operations for
projects.

### Prerequisites

You need to have the following software installed on your system:

- Python 3.9+
- flask

### Installing Dependencies

In your project directory, install the required Python packages using pip and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Migrations

```
flask db upgrade
```

## Running the Application

To run the Flask application, execute the run.py script:

```python
python app.py
```

The application will start and be accessible at http://127.0.0.1:5000/ in your web browser.

## API Endpoints

- Create Project: POST /project
- Read Project: GET /project/<id>
- Read Projects: GET /project
- Update Project: PUT /project/<id>
- Delete Project: DELETE /project/<id>

## Database

The application uses an PostgreSQL database for simplicity. You can configure your own database system in the config.py
file.

## Set up your Environment variable

```
touch .env
```

Find the .sample_env from the structure. Copy the contents and paste it in .env file. Replace the dummy values with your
actual account credentials.