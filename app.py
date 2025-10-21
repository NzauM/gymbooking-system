from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from models import db, Trainer


# add the sqlalchemy database configurtion to our app
# initialize our sqlalchemy instance with our app
# initialize our migrate instance with both our app and our DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gym.db'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def welcome():
    return "<h1>Flask App Running Smoothly.....</h1>"

@app.route('/create_trainer', methods=['POST'])
def create_trainer():
    # access trainer data that was sent from client through request
    trainer_data = request.json
    # print(trainer_data)
    # Add this new resource to your database, and ensure it’s saved. i.e create an instance of the trainer class, add it to the session and commit the session
    new_trainer = Trainer(name=trainer_data['name'], bio=trainer_data['bio'], specialization = trainer_data['specialization'], phone_number=trainer_data['phone_number'])
    db.session.add(new_trainer)
    db.session.commit()
    resp = make_response({'success':'Trainer Created'}, 201)
    return resp

# define a route to get a specific trainer by id
# localhost:5000/get_trainer_by_id/45 trainer_id = 45
@app.route('/get_trainer_by_id/<trainer_id>')
def get_trainer(trainer_id):
    # print(trainer_id)
    trainer = db.session.query(Trainer).get(trainer_id)
    resp = make_response(trainer.to_dict(), 200)
    return resp

@app.route('/trainers')
def get_trainers():
    trainers = db.session.query(Trainer).all()
    trainer_list = [trainer.to_dict() for trainer in trainers]
    resp = make_response({'trainers'})




