from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from pendulum import datetime


@dag(
    dag_id='dag_file_1',
    start_date=datetime(2023, 7, 1),
    schedule='@daily',
    catchup=False,
)
def dag_from_config():
    BashOperator(
        task_id="say_hello",
        bash_command='echo $ENVVAR',
        env={"ENVVAR": 'Hello! :)'},
    )


dag_from_config()
