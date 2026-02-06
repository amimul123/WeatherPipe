from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import sys

sys.path.append('/opt/airflow/api-request')
from insert_record import main

def test_1():
    print('test_1 task')

default_args ={
    'description' : 'Weather API pipeline',
    'start_date' : datetime(2026,2,5),
    'catchup': False,
}

dag = DAG(
    dag_id = 'weather-api-pipeline',
    default_args = default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    # task 1
    task1 = PythonOperator(
        task_id = 'api_data',
        python_callable = main
    )