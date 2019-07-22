#!/bin/bash

zk=$1

echo "#################### installing jq ######################"
sudo apt -y install jq

echo "export password=clusterKafka@123" >> ~/.bashrc
echo "export clusterNameA=clusterKafka" >> ~/.bashrc

source ~/.bashrc

echo "export clusterName=$(curl -u admin:$password -sS -G "https://$clusterNameA.azurehdinsight.net/api/v1/clusters" | jq -r '.items[].Clusters.cluster_name')" >> ~/.bashrc

source ~/.bashrc

echo "export KAFKAZKHOSTS=`curl -sS -u admin:$password -G http://headnodehost:8080/api/v1/clusters/$clusterName/services/ZOOKEEPER/components/ZOOKEEPER_SERVER | jq -r '["\(.host_components[].HostRoles.host_name):2181"] | join(",")' | cut -d',' -f1,2`" >> ~/.bashrc

echo "export KAFKABROKERS=`curl -sS -u admin:$password -G http://headnodehost:8080/api/v1/clusters/$clusterName/services/KAFKA/components/KAFKA_BROKER | jq -r '["\(.host_components[].HostRoles.host_name):9092"] | join(",")' | cut -d',' -f1,2`" >> ~/.bashrc

source ~/.bashrc

echo "Kafka hosts are: "$KAFKAZKHOSTS
echo "Kafka brokers are: "$KAFKABROKERS

echo "###################### Topic Creation ####################"

/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 3 --partitions 8 --topic twitterData --zookeeper $zk:2181

echo "###################### List all topics #########################"

/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --list --zookeeper $zk:2181
 
