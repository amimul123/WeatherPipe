from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import sys
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

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
    dag_id = 'weather-api-dag_dbt',
    default_args = default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    # task 1
    task1 = PythonOperator(
        task_id = 'fetch_api_data',
        python_callable = main
    )

    task2 = DockerOperator(
        task_id = 'dbt_run_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command= 'run',
        working_dir='/usr/app',
        mounts=[
            Mount(
                source='/home/amimu/repos/weather-data-project/dbt/profiles.yml',
                target='/root/.dbt/profiles.yml',
                type='bind'
            ),
            Mount(
                source='/home/amimu/repos/weather-data-project/dbt/my_project',
                target='/usr/app',
                type='bind'
            ),
        ],
        network_mode='weather-data-project_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2