# Hadoop map reduce


### Development Environment Setup

1 - Clone this repository<br />
2 - Download Cloudera’s QuickStart Docker Container <br />

By docker hub:
```
docker pull cloudera/quickstart:latest
```

or download manually [here](https://www.cloudera.com/downloads/quickstart_vms/5-13.html)

if you manually downloaded the container, import it
``` 
 docker import cloudera-quickstart-vm-5.13.0-0-beta-docker 
``` 
and 
```
docker image tag <HASH-HERE> cloudera-5-13 
```
3 - Running container <br />
``` 
$ docker run -p 8888:8888 -p 7180:7180 -p 8181:80 -v "$(pwd)/Projects/hadoop-map-reduce:/var/www/" \
  --name quickstart.cloudera \
  --hostname=quickstart.cloudera \
  -d --privileged=true \
  -t -i cloudera-5-13 \
  /usr/bin/docker-quickstart

$ docker attach quickstart.cloudera
```



## Create directory in hdfs and copy txt file

```
hadoop fs -mkdir -p /var/www
```
and

```
hadoop fs -put shakespeare.txt /var/www/
```
