FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY ./app /app

# RUN pip install -r requirements.txt
RUN pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com -r requirements.txt

RUN git config --global http.sslVerify false

# workaround of linux server folder permission miss
RUN chmod -R 655 /app/static /app/templates