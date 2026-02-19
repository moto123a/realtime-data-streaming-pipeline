from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def etl_task():
    print("Extracting streaming data from Kafka...")
    print("Transforming data for analytics...")
    print("Loading data into Redshift warehouse...")

default_args = {
    'owner': 'data_engineer',
    'start_date': datetime(2025, 1, 1)
}

dag = DAG(
    'realtime_streaming_etl',
    default_args=default_args,
    schedule_interval='@hourly',
    catchup=False
)

etl = PythonOperator(
    task_id='run_etl_pipeline',
    python_callable=etl_task,
    dag=dag
)

etl

