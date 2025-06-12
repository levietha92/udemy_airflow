# https://academy.astronomer.io/path/airflow-101/dag-101-1/1565802

from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import dag, task, chain
from pendulum import datetime

@dag(
    dag_id="check_dag",
    start_date=datetime(2025,1,1),
    schedule="0 0 * * *",
    description="DAG to check data"
)

def check_dag():
    @task.bash
    def create_file():
        return 'echo "Hi there!" >/tmp/dummy'
    
    @task.bash
    def check_file():
        return 'test -f /tmp/dummy'

    @task
    def read_file():
        print(open('/tmp/dummy', 'rb').read())

    create_file() >> check_file() >> read_file()

check_dag()
