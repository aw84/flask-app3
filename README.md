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
```bash
export FLASK_ENV=development
flask run
```
