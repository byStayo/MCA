from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers import UserController, DealController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

user_controller = UserController(db)
deal_controller = DealController(db)

@app.route('/register', methods=['POST'])
def register():
    return user_controller.register()

@app.route('/login', methods=['POST'])
def login():
    return user_controller.login()

@app.route('/submit_deal', methods=['POST'])
def submit_deal():
    return deal_controller.submit()

@app.route('/approve_deal', methods=['POST'])
def approve_deal():
    return deal_controller.approve()

@app.route('/track_deal', methods=['GET'])
def track_deal():
    return deal_controller.track()

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
