import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


# Correct way to get environment variable
mysql_password = os.getenv('MYSQL_ROOT_PASSWORD')


# Ensure the variable is set
if not mysql_password:
    raise ValueError("MYSQL_ROOT_PASSWORD environment variable is not set.")


# Replace [PASSWORD] with the root password for your mysql container
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{getenv(MYSQL_ROOT_PASSWORD)}@myqsl1:3306/flask-db'


# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{mysql_password}@mysql1:3306/flask-db'


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email, ' Name: ', self.first_name, ' ', self.last_name, '\n'])


@app.route('/')
def hello():
  data1 = Users.query.all()
  return render_template('home.html', data1=data1)

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
