from flask import Flask
import logic, config

app = Flask(__name__)
app.config['PORT'] = config.PORT
app.config['HOST'] = config.HOST

# POST Method 
@app.route("/challenge", methods=["POST"])
def createData():
   return logic.createData()

# DELETE Method
@app.route("/deleteitems", methods=["DELETE"])
def deleteItems():
    return logic.deleteItems()

if __name__ == "__main__":
    print("Server running in port %s"%(app.config['PORT']))
    app.run(host=app.config['HOST'], port=app.config['PORT'])