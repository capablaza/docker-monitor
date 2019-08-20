import docker

def get_containers_names():
    client = docker.from_env()

    containers = client.containers.list(all)
    list_containers = dict()

    for con in containers:
        list_containers = con.name
    return list_containers

def get_log_container_name(container_name):
    client = docker.from_env()
    container = client.containers.get(container_name)
    list_logs = dict()
    list_logs = container.logs()

    return list_logs
