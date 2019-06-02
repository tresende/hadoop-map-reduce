# Hadoop map reduce


## Environment config

Download docker ce and run:

> docker run -v "$(pwd)/hadoop-map-reduce:/var/www/" --name quickstart.cloudera \
  --hostname=quickstart.cloudera \
  -d --privileged=true \
  -t -i cloudera-5-13 \
  /usr/bin/docker-quickstart
