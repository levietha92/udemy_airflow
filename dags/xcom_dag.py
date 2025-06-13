from airflow.sdk import task,dag, Context

@dag
def xcom_dag():
    @task
    def task_a(**context: Context):
        val = 42
        context['task_instance'].xcom_push(key='my_key', value=val)

    @task
    def task_b(**context: Context):
        val = context['task_instance'].xcom_pull(task_ids='task_a',key='my_key')
        print(val)

    task_a() >> task_b()

xcom_dag()    
