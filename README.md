# Realtime Data Streaming With TCP Socket, NLP, Apache Spark, Kafka and Elasticsearch 

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [Technologies](#technologies)



## Introduction

This project serves as a comprehensive guide to building an pipeline using TCP/IP Socket, Apache Spark, Machine Learning, Kafka and Elasticsearch. It covers each stage from data acquisition, processing, sentiment analysis with SVM model, production to kafka topic and connection to elasticsearch.

## System Architecture
![System_architecture.png](assets%2FSystem_architecture.png)

The project is designed with the following components:

- **Data Source**: We use `yelp.com` dataset for our pipeline.
- **TCP/IP Socket**: Used to stream data over the network in chunks
- **Apache Spark**: For data processing with its master and worker nodes.
- **Confluent Kafka**: Our cluster on the cloud
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Kafka Connect**: For connecting to elasticsearch
- **Elasticsearch**: For indexing and querying


## Technologies

- Python
- Machine Learning
- TCP/IP
- Confluent Kafka
- Apache Spark
- Docker
- Elasticsearch

