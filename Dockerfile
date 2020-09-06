FROM python

ADD pip-requirements.txt /pip-requirements.txt
RUN pip install -r pip-requirements.txt

ADD pb/ /pb/
ADD server.py /server.py
ADD client.py /client.py
ADD start.sh /start.sh

EXPOSE 9080
ENTRYPOINT ["/start.sh"]
