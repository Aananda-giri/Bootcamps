# Elastic Search Course for begineers
* [youtube video](https://www.youtube.com/watch?v=a4HBKEda_F8&t=3880s)

* [installing elastic search](https://www.elastic.co/search-labs/tutorials/install-elasticsearch)
* [github repo](https://github.com/ImadSaddik/ElasticSearch_Python_Course)
```
docker run -p 127.0.0.1:9200:9200 -d --name elasticsearch \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  -v "elasticsearch-data:/usr/share/elasticsearch/data" \
  docker.elastic.co/elasticsearch/elasticsearch:8.15.0
```

```
# install elastic search
uv pip install elasticsearch==8.15.0
```

```
# run the docker 
sudo docker start elasticsearch
```

name, price and description






Elastic search saga:
- They were initially open source (Apache 2.0)
- jan. 2021 changed to dual licensing: server side public, client side open source
- aws forked elastic search and called it open search under apache 2.0 license
- 2024 they changed to dual licensing: users can modify and distribute freely
- elastic search is still available in major cloud platforms


docker run -p 127.0.0.1:9200:9200 -d --name elasticsearch \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  -v "elasticsearch-data:/usr/share/elasticsearch/data" \
  docker.elastic.co/elasticsearch/elasticsearch:8.15.0
