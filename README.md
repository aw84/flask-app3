# First run
- Create `venv` for Flask app: `python3 -m venv /venv-flask`
- Activate: `source /venv-flask/bin/activate`
- Within activated venv install requirements: `pip install -r requirements.txt`
- Create a database with: `flask db upgrade`

# Tests
```bash
export PYTHONPATH=/code/flask-app3
pytest -vvv tests/
```
# Application run
Flask
```bash
export FLASK_ENV=development
flask run
```
Celery worker
```bash
celery -A app.celery.tasks worker -l info
```
Celery beat
```bash
celery -A app.celery.tasks beat -l info
```
