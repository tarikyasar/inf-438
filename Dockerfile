FROM alpine:3.14
COPY . /home/Twitter 
RUN apk add --no-cache python3 py3-pip
RUN apk add openjdk8 bash vim
RUN pip3 install requests kafka-python pyspark
RUN echo export PATH=/home/Twitter/kafka_2.13-3.0.0/bin:$PATH >> ~/.bashrc
RUN source ~/.bashrc
RUN bash
RUN /home/Twitter/kafka_2.13-3.0.0/bin/zookeeper-server-start.sh /home/Twitter/kafka_2.13-3.0.0/config/zookeeper.properties &
RUN /home/Twitter/kafka_2.13-3.0.0/bin/kafka-server-start.sh /home/Twitter/kafka_2.13-3.0.0/config/server.properties &
RUN /home/Twitter/kafka_2.13-3.0.0/bin/kafka-console-consumer.sh --topic veri-tabanlari --from-beginning --bootstrap-server localhost:9092 &

CMD ["/bin/bash"]
