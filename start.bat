pip install -r requirements.txt
set FLASK_APP = run.py

flask db init
flask db migrate
flask db upgrade