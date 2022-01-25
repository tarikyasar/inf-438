zookeeper-server-start.sh /home/Twitter/kafka_2.13-3.0.0/config/zookeeper.properties &
kafka-server-start.sh /home/Twitter/kafka_2.13-3.0.0/config/server.properties &
kafka-console-consumer.sh --topic veri-tabanlari --from-beginning --bootstrap-server localhost:9092 &
