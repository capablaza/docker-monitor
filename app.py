from flask import Flask
from docker_func import *
from docker.errors import APIError
from flask import jsonify

app = Flask(__name__)

@app.route("/containers_names", methods=['GET'])
def get_container_names():
    try:
        return jsonify(get_containers_names())
    except APIError as error:
        return {
            error.response.status_code :  error.response.reason
        }


@app.route("/logs/<container_name>", methods=['GET'])
def get_log_by_container_name(container_name):
    try:
        logContainer = get_log_container_name(container_name)        
        return logContainer
    except APIError as error:
        return {
            error.response.status_code :  error.response.reason
        }

@app.route("/image_names", methods=['GET'])
def get_images_names():
    try:
         return jsonify(get_images_name())
    except APIError as error:
        return {
            error.response.status_code :  error.response.reason
        }

if __name__ == '__main__':
    get_images_name()
    app.run(host='0.0.0.0')
