# StockStream: Continuous Stock Market Data Flow and Insights

StockStream is a comprehensive and efficient system that enables continuous stock market data flow, real-time data processing, and insightful analysis using various technologies such as Python, Kafka, AWS EC2, Athena, and Glue crawler. This project is designed to provide users with a robust and scalable platform to stay up-to-date with stock market trends, make informed investment decisions, and gain valuable business insights.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
  

## Introduction

The stock market is a dynamic and fast-paced environment where timely data access and analysis can make a significant difference in investment outcomes. StockStream addresses this need by automating the process of loading stock market data from a CSV file into a Kafka producer stream, facilitating real-time data processing and analysis. The platform is built on AWS infrastructure for high scalability, availability, and cost-effectiveness.

## Technologies Used

- Python: The core programming language used for data processing, automation, and script implementation.
- Kafka: A distributed streaming platform that enables real-time data ingestion and processing.
- AWS EC2: Elastic Compute Cloud provides scalable virtual server instances for hosting the Kafka cluster.
- Athena: Amazon Athena is a serverless query service used for querying data stored in Amazon S3 using standard SQL queries.
- Glue Crawler: AWS Glue Crawler automatically discovers and catalogs metadata about data sources, making it easier to work with data in AWS services.

## Features

- **Automated Data Ingestion:** A Python script is provided to automate the process of loading stock market data from a CSV file into the Kafka producer stream. This enables continuous and real-time data flow into the system.

- **Highly Scalable Kafka Cluster:** The Kafka cluster is deployed on an AWS EC2 instance to ensure high scalability and availability. The system is designed to achieve 99.9% uptime, making sure that the data stream is always available for consumption by the consumer script.

- **Real-time Data Processing:** With Kafka's streaming capabilities, incoming data is processed in real-time, allowing users to access the latest stock market information as it becomes available.

- **Athena-based Business Insights:** Leveraging AWS Athena, users can extract valuable business insights from the stored stock market data. By running SQL queries, users can gain valuable information to make informed investment decisions.

- **Cost-Effective Infrastructure:** The project's architecture is optimized to be cost-effective, utilizing AWS services efficiently to minimize operational expenses.
