import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os
import dataPreprocessing    

dag_path = os.getcwd()

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1)
}



def check_csv_file():
    # Your code to check if the CSV file is present on the destination
    # You can use Python's built-in functions or libraries like os or pathlib
    
def perform_data_cleaning_and_outlier_handling():
    # Your code to perform data cleaning and outlier handling
    # You can use pandas or other data manipulation libraries
    df = pd.read_csv("RawData/Job_Placement_Data.csv")
    # Trimming of outliers
    df = df[ (df['cgpa'] < 8.80) & (df['cgpa'] > 5.11) ]
    # Capping on outliers
    upper_limit = df['cgpa'].mean() + 3*df['cgpa'].std()
    lower_limit = df['cgpa'].mean() – 3*df['cgpa'].std()
    df['cgpa'] = np.where(df['cgpa']>upper_limit,upper_limit,np.where(df['cgpa']<lower_limit,lower_limit,df['cgpa']))

def load_data_to_database():
    # Your code to load the cleaned data into a database
    # You can use libraries like SQLAlchemy or psycopg2 for database operations
    
with DAG('job_placement_dag', default_args=default_args, schedule_interval=None) as dag:
    check_csv_task = PythonOperator(
        task_id='check_csv_file',
        python_callable=check_csv_file
    )
    
    data_cleaning_task = PythonOperator(
        task_id='data_cleaning_and_outlier_handling',
        python_callable=perform_data_cleaning_and_outlier_handling
    )
    
    load_to_database_task = PythonOperator(
        task_id='load_data_to_database',
        python_callable=load_data_to_database
    )
    
    check_csv_task >> data_cleaning_task >> load_to_database_task

dag = DAG(
    'placementsDAG',
    default_args=default_args,
    description='A DAG for automating an ETL process of shortlisting candidates profile',
    schedule_interval=None,
    catchup=False
)

