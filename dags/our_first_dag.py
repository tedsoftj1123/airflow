from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='our_first_dag_v3',
    description='Our first dag',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2024, 6, 1),
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo hello world',
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo hello world 2',
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command='echo hello world 3',
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)