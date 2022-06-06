FROM python:3.8-slim
WORKDIR /Data_BI
COPY . /Data_BI
RUN pip install -r requirements.txt
RUN chmod +x script.sh
CMD ["./script.sh"]