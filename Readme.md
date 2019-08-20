


# Docker Monitor

Docker monitor is an easy api for get information from your containers

## Installation

To start you need build the image, to do it this run the next command.

```bash
docker build -t docker-monitor-img .
```

Then you need run this image to do this you need run the next command:

```bash
docker run -d -it --rm -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock --name docker-api-con docker-api-logs
```

## Usage

The api expose the follows endpoints:

GET ALL CONTAINER NAMES

```
http://[host]:5000/containers_names
```

GET LOG BY CONTAINER NAME

```
http://[host]:5000/containers_names
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact information
For contact you can send me an email at : c.apablaza.z@gmail.com


## License
[MIT](https://choosealicense.com/licenses/mit/)