import flask
import pymongo
import time as t


app = flask.Flask(__name__)


@app.route("/")
def app_route():
    client = pymongo.MongoClient("my_docker_mongo", 27017)
    test_db = client.test_db
    times_collection = test_db.times_collection

    times_collection.insert_one({"time": t.time()})

    client.close()
    return "<h1>this is flask test page</h1>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
