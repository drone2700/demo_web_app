from flask import Flask
from flask import render_template

app = Flask(__name__) # 1. Create the app


@app.route("/")      # 2. Map a URL
def home():        #  to a function
  return "Hello, Buyers Edge!"

@app.route("/bep")      # 2. Map a URL
def bep():        #  to a function
  return "OMG the hacker!"

@app.route("/product/<int:id>")
def product(id):
    return f"Product number {id}"



@app.route("/menu")
def menu():
    dishes = ["Tacos", "Pasta", "Salad"]
    return render_template("menu.html",
        title="Today's menu", dishes=dishes)


from flask import Flask, jsonify, request, abort


products = [
  {"id": 1, "name": "Rice", "price": 4.5},
  {"id": 2, "name": "Olive oil", "price": 12.0},
]


#############API FLASK##############
@app.get("/api/products")
def list_products():
  return jsonify(products)

@app.get("/api/products/<int:id>")
def get_product(id):
  for p in products:
    if p["id"] == id:
      return jsonify(p)
  abort(404)

@app.post("/api/products")
def create_product():
  data = request.get_json()
  new = {"id": len(products) + 1, **data}
  products.append(new)
  return jsonify(new), 201


if __name__ == "__main__":
  app.run(debug=True)  # 3. Start it

