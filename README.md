# dynamic-dags-tutorial
This repo contains an Astronomer project with multiple examples showing how to dynamically generate DAGs in Airflow. A guide discussing these concepts in depth will be published shortly.

## DAG Overview
This repo contains DAGs and supporting Python scripts that dynamically generate DAGs using multiple methods. They are described here, organized by folder.

#### dags

 - `dynamic-dags-connections.py` generates DAGs based on Airflow connections.
 - `dynamic-dags-loop.py` generates DAGs based on a simple range() loop.
 - `dynamic-dags-variable.py` generates DAGs based on an Airflow variables.
 - `dag_file_1.py` and `dag_file_2.py` are actual DAG files that were dynamically generated using scripts in the `include/` directory, described below.

#### include

 - `dag-config/` contains two Json configuration files with parameters used to dynamically generate Python files for `dag_file_1.py` and `dag_file_2.py`.
 - `dag-template.py` contains the starting DAG template from which other DAG files are dynamically generated.
 - `generate-dag-files.py` contains a script to dynamically generate a DAG file for each config file in `dag-config/` by making a copy of `dag-template.py` and replacing key parameters from the config file.

## Getting Started
The easiest way to run these example DAGs is to use the Astronomer CLI to get an Airflow instance up and running locally:

 1. [Install the Astronomer CLI](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart)
 2. Clone this repo somewhere locally and navigate to it in your terminal
 3. Initialize an Astronomer project by running `astro dev init`
 4. Start Airflow locally by running `astro dev start`
 5. Navigate to localhost:8080 in your browser and you should see the tutorial DAGs there
