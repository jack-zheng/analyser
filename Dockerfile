FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY ./app /app

RUN pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com -r requirements.txt

RUN git config --global http.sslVerify false