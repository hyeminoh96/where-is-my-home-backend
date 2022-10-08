from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hello():
    return {"message": "Hello World"}


# FIXME : root url

@app.get("/buyer")
def read_buyers():
    return "all buyers"


@app.get("/buyer/{buyer_id}")
def read_buyer(buyer_id: int = None):
    return {"buyer_id": buyer_id}


@app.post("/buyer")
def create_buyers():
    return "create a buyer"


@app.put("/buyer/{buyer_id}")
def update_buyer(buyer_id: int = None):
    return {"update": {"buyer_id": buyer_id}}


@app.delete("/buyer/{buyer_id}")
def delete_buyer(buyer_id: int = None):
    return {"delete": {"buyer_id": buyer_id}}


@app.get("/seller")
def read_sellers():
    return "all sellers"


@app.get("/seller/{seller_id}")
def read_seller(seller_id: int = None):
    return {"seller_id": seller_id}


@app.post("/seller")
def create_seller():
    return "create a seller"


@app.put("/seller/{seller_id}")
def update_seller(seller_id: int = None):
    return {"update": {"seller_id": seller_id}}


@app.delete("/seller/{seller_id}")
def delete_seller(seller_id: int = None):
    return {"delete": {"seller_id": seller_id}}


@app.get("/property")
def read_properties():
    return "all properties"


@app.get("/property/{property_id}")
def read_property(property_id: int = None):
    return {"property_id": property_id}


@app.post("/property")
def create_property():
    return "create a property"


@app.put("/property/{property_id}")
def update_property(property_id: int = None):
    return {"update": {"property_id": property_id}}


@app.delete("/property/{property_id}")
def delete_property(property_id: int = None):
    return {"delete": {"property_id": property_id}}
