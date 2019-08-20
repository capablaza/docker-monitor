from flask import Flask
from docker_func import *
from docker.errors import APIError

app = Flask(__name__)

@app.route("/containers_names", methods=['GET'])
def getContainerNames():
    try:
        return get_containers_names()
    except APIError as error:
        return {
            error.response.status_code :  error.response.reason
        }


@app.route("/logs/<container_name>", methods=['GET'])
def getLogByContainerName(container_name):
    try:
        logContainer = get_log_container_name(container_name)
        print(str(logContainer))
        return logContainer
    except APIError as error:
        return {
            error.response.status_code :  error.response.reason
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0')
