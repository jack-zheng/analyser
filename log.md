### run app against 5k port
docker run -d --name my5k -p 5000:80 myimage. 

export FLASK_APP=main.py
export FLASK_DEBUG=1

docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.1
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html