from security import authenticate, identity
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import jwt_required, JWT



from security import authenticate, identity

app =Flask(__name__)
api=Api(app)

app.secret_key="sagar"
jwt = JWT(app, authenticate, identity) # /auth

items= [
    {"name":"dog"},
    {"name":"cat"},
    {"name":"fish"},     
]


class Item(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("price", 
                        type=float, 
                        required=True, 
                        help="Price Cannot be blank")
    parser.add_argument("name", 
                        type=str, 
                        required=True, 
                        help="Name Cannot be blank")                    
    

    @jwt_required()
    def get(self, name):
        item=list(filter(lambda x: x["name"]==name, items))
        return item,200 if item else 404

    def post(self, name):
        data=Item.parser.parse_args()

        if next(filter(lambda x: x["name"]==name, items),None) is not None:
            return {"message": "Item already present, cannot add it again"},400 
        item={"name":name, "price": data["price"]}
        
        items.append(item)
        return items, 201
     
    def delete(self, name):
        global items
    
        items = list(filter(lambda x: x["name"]!= name, items))
        if items:
            return {
                "items":items,
                "message":"Item with name: " +name+" deleted" }
        else:
            return {"message":"Item with name: " +name+" is not found."}

    def put(self, name):
        item = next(filter(lambda x: x["name"]== name, items), None)  
        
        data=Item.parser.parse_args()

        if item is None:
            item={"name":name, "price": data["price"]}
            items.append(item)
            return {
                "items":items,
                "message":"Item with name: " +name+" is now added."}
        else:
            item.update(data)
            return {
                "items":items,
                "message":"Item with name: " +name+" already exist, price updated"}


class ItemList(Resource):
    def get(self):
        return {"items":items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')




app.run(port=5000, debug=True)
