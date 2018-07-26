# Analyser
this is the second version of analyser, new design & new project structure

### Command list
docker run -d --name my5k -p 5000:80 myimage # start flask website 


export FLASK_APP=main.py # config for flask debug
export FLASK_DEBUG=1


docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.1
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

## TODO List
* flask integrate with es search sample
 + trigger python API, new record created on es search
* impl of record to es search
* about the data backup, using real device instead fo es docker
 + or a command to migrate data everytime new docker
* finish docker compose
