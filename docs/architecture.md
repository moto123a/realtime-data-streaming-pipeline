# Real-Time Data Streaming Pipeline Architecture

## Overview
This project implements a real-time streaming data pipeline for processing transactional order data using Apache Kafka and Spark Structured Streaming.

## Components

### 1. Kafka Producer
Generates real-time order events and publishes them into Kafka topic `orders-topic`.

### 2. Apache Kafka
Acts as a distributed messaging system to handle high-throughput real-time streaming data ingestion.

### 3. Spark Structured Streaming
Consumes Kafka topic events and performs streaming transformations on order-level transactional data.

### 4. Apache Airflow
Orchestrates ETL workflows for batch ingestion and scheduled transformation of processed streaming datasets.

### 5. Data Warehouse (AWS Redshift)
Stores transformed order-level datasets for business intelligence and analytics reporting.

## Data Flow

Kafka Producer → Kafka Topic → Spark Streaming Consumer → ETL via Airflow → AWS Redshift Warehouse

## Technologies Used

- Apache Kafka
- Apache Spark Structured Streaming
- Apache Airflow
- AWS Redshift
- Python
- SQL

## Use Case

Supports real-time analytics for order transactions enabling downstream reporting systems and enterprise dashboards.

