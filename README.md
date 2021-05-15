# images-sorter

### Using Docker

In order to use this tool with Docker, go into the folder containing the different albums. Then, simply run:
```
docker run --rm -v $(pwd):/usr/src/app/albums -u $( id -u $USER ):$( id -g $USER) polchky/imagesorter
```
