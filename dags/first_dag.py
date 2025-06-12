from airflow.sdk import dag, task, chain
from airflow.providers.standard.operators.python import PythonOperator
from pendulum import datetime
import requests
import csv
import os

default_args = {
    'retries':3
}

# DAG decorator
@dag(
    schedule="@daily",
    start_date=datetime(2025,6,10),
    description="Call Pokemon API",
    tags=['pokemon'],
    default_args=default_args
    # max_consecutive_failed_dag_runs=3
)
# Functions underneath DAG decorator

def first_dag():
    @task
    def task_a():
        print("Hello I'm task A")
    @task
    def task_b():
        print("Hello I'm task B")
    @task
    def task_c():
        print("Hello I'm task C")
    @task
    def task_d():
        print("Hello I'm task D")
    @task
    def task_e():
        print("Hello I'm task E")
    #Task Dependencies
    # a = task_a()
    # a >> task_b() >> task_c() #sequencing a to b to c
    # a >> task_d() >> task_e()
    # a >> [task_b(), task_c()] #parallel tasks in a list
    chain(task_a(), [task_b(), task_d()], [task_c(), task_e()])

first_dag()