import json
import uuid
from flask import request, Blueprint
from flask_restful import Resource
from shop import redis_client, api

geoprice = Blueprint('geoprice', __name__)
 
@geoprice.route('/')
@geoprice.route('/home')
def home():
    return "Hello Yogesh@byprice.com_redis"

class ProductList(Resource):
    def get(self):
        old_products = redis_client.get("products")
        products = {}
        if old_products is not None:
            products = json.loads(redis_client.get("products"))
        return {'data': products} 

    def post(self):
        name = request.form.get('name')
        price = request.form.get('price')
        stock = request.form.get('stock')
        product_id = uuid.uuid1()
        
        old_products = redis_client.get("products")
        if old_products is None:
            products = {
                "products": {
                    str(product_id): {
                        'name': str(name),
                        'price': str(price),
                        'stock': str(stock),
                    }
                }
            }
            redis_client.set('products', json.dumps(products))
        else:
            json_products =  json.loads(old_products)
            list_products = json_products['products']
            next_product = {
                str(product_id): {
                    'name': str(name),
                    'price': str(price),
                    'stock': str(stock),
                }
            }
            json_products[str(product_id)] = {
                'name': str(name),
                'price': str(price),
                'stock': str(stock),
            }
            list_products.update(next_product)
            products = {
                "products": list_products, 
            }               
            redis_client.set('products', json.dumps(products))            
        return {'data': products}    

def get_product(key):
    old_products = redis_client.get("products")
    product = {}
    if old_products is not None:
        json_products =  json.loads(old_products)    
        for _key, _value in json_products['products'].items():  
            if key == _key:
                product = {
                    str(_key): _value
                }
                break
    return product 

class Product(Resource):     
        
    def get(self, key):
        product = get_product(key)
        return {'data': product}  

    def put(self, key):
        return {'message': 'Update successfully'}    

    def delete(self, key):
        return {'message': 'Delete successfully!'}      

api.add_resource(ProductList, '/products')
api.add_resource(Product, '/product/<string:key>')