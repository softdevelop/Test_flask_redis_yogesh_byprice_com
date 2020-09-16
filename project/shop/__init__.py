from flask import Flask
from flask_redis import FlaskRedis

from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config["REDIS_URL"] = 'redis://:@localhost:6379/my_db'

redis_client = FlaskRedis(app)


from shop.geoprice.views import geoprice
app.register_blueprint(geoprice)