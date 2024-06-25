from datetime import timedelta, datetime

from airflow.decorators import dag, task

default_args = {
    'owner': 'tedsoftj1123',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}


@dag(dag_id='tag_with_taskflow',
     default_args=default_args,
     start_date=datetime(2021, 1, 1),
     schedule_interval='@daily')
def hello_world():
    @task()
    def get_name() -> str:
        return 'Ted'

    @task()
    def get_age() -> int:
        return 18

    @task()
    def greet(name: str, age: int):
        print(f'Hello {name}, you are {age} years old.')

    name = get_name()
    age = get_age()
    greet(name, age)


greet_dag = hello_world()
