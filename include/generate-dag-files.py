import json
import os
import shutil
import fileinput


config_filepath = 'include/dag-config/'
dag_template_filename = 'include/dag-template.py'

for filename in os.listdir(config_filepath):
    f = open(config_filepath + filename)
    config = json.load(f)
    
    new_filename = 'dags/'+config['DagId']+'.py'
    shutil.copyfile(dag_template_filename, new_filename)
    

    for line in fileinput.input(new_filename, inplace=True):
        line = line.replace("dag_id", "'"+config['DagId']+"'")
        line = line.replace("scheduletoreplace", config['Schedule'])
        line = line.replace("querytoreplace", config['Query'])
        print(line, end="")
        