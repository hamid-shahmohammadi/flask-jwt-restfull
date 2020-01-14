from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList



app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity) # /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)