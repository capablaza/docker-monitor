


# Docker Monitor

Docker monitor is an easy api for get information from your containers

## Installation

If you want build the image manually then run the next command:

```shell
docker build -t docker-monitor-img .
```

In otherwise just you need run:

```shell
docker pull capablaza/docker-monitor
```

Then you need run this image to do this you need run the next command:

```shell
docker run -d -it --rm -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock --name docker-monitor capablaza/docker-monitor
```

## Usage

The api expose the follows endpoints:

GET ALL CONTAINER NAMES

```
http://[host]:5000/containers_names
```

GET LOG BY CONTAINER NAME

```
http://[host]:5000/logs/[container_name]
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact information
For contact you can send me an email at : c.apablaza.z@gmail.com


## License
[MIT](https://choosealicense.com/licenses/mit/)