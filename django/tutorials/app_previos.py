from flask import Flask, jsonify, request


stores =[
    {
        "name":"office",
        "items":[ {"name":"paper"}, 
                {"name": "stapler"} ]
    },

    {
        "name":"home",
        "items":[ {"name":"spoon"}, 
                {"name": "pan"} ]
    }

]


app =Flask(__name__)

@app.route('/') 
def home():
    return "He He World"


#GET /store
@app.route('/store')
def get_stores():
    return jsonify({"stores":stores})

#GET /store/<string:name>
@app.route('/store/<string:store_name>') 
def get_store(store_name):
    for store in stores:
        if store["name"]==store_name:
            return jsonify(store)
    else: 
        return {"message": "Store not present"}
    
#GET /store/<string:store_name>/item {name:, price:}
@app.route('/store/<string:store_name>/<string:item_name>')
def get_item_in_store(store_name, item_name):
    for store in stores:
        if store["name"]==store_name:
            for item in store["items"]:
                if item["name"]==item_name:
                   return jsonify(item)
            else:
                return {"message":"Store: "+store_name +" found,but item: "+item_name +"  not found"}
     
    else: 
        return {"message": "Store not found"}


#POST /store data: {name}
@app.route('/store', methods=["POST"]) 
def create_Store():
    request_data=request.get_json()
    store={
        "name":request_data["name"]
    }
    stores.append(store)
    return jsonify(stores)


#POST /store/<string:store_name>/item {name:, price:}
@app.route('/store/<string:store_name>/item', methods=["POST"])
def create_item_in_store(store_name):
    request_data=request.get_json()
    for store in stores:
        if store["name"]==store_name:
            new_item={
                "name":request_data["name"]
                }
            store["items"].append(new_item)

            
            
            return jsonify(stores)  
    else:
        return jsonify({"name":"store not found"})
        



app.run(port=5000)
