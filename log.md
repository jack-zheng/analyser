### run app against 5k port
docker run -d --name my5k -p 5000:80 myimage. 

export FLASK_APP=main.py
export FLASK_DEBUG=1