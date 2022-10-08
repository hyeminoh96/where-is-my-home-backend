from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hello():
    return {"message": "Hello World"}


@app.get("/buyers")
def read_buyers():
    return "all buyers"


@app.get("/buyers/{buyer_id}")
def read_buyer(buyer_id: int = None):
    return {"buyer_id": buyer_id}


@app.get("/sellers")
def read_sellers():
    return "all sellers"


@app.get("/sellers/{seller_id}")
def read_seller(seller_id: int = None):
    return {"seller_id": seller_id}


@app.get("/properties")
def read_properties():
    return "all properties"


@app.get("/properties/{property_id}")
def read_property(property_id: int = None):
    return {"property_id": property_id}
