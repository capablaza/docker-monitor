import docker
import json

def get_containers_names():
    client = docker.from_env()

    containers = client.containers.list(all)
    list_containers = []

    for con in containers:
        con_obj = {
            "name" : con.name ,
            "status" : con.status            
        }        
        list_containers.append(con_obj)        
    return list_containers

def get_log_container_name(container_name):
    client = docker.from_env()
    container = client.containers.get(container_name)
    list_logs = dict()
    list_logs = container.logs()
    return list_logs

def get_images_name():
    client = docker.from_env()
    images_from_system = client.images.list(all=True)
    list_images = []
    for image in images_from_system:
        img_con = {
            "name" : image.tags
        }
        list_images.append(img_con)    
    return list_images