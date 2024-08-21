import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:  %(levelname)s:  %(message)s:')

project_name = "text-summarizer"
list_files = [      #used for CI/CD deploytment
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",        # this installs the folder as a local package in the virtual environment
    f"src/{project_name}/components/__init__.py",        
    f"src/{project_name}/utils/__init__.py",       
    f"src/{project_name}/utils/common.py",       
    f"src/{project_name}/logging/__init__.py",       
    f"src/{project_name}/config/configuration.py",       
    f"src/{project_name}/pipeline/__init__.py",       
    f"src/{project_name}/entity/__init__.py",       
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",      
    "setup.py"
    "research/trials.ipynb"
]

for file in list_files:
    file = Path(file)                           #convert the \ to / in the path
    filedir, filename = os.path.split(file)     #split the path into directory and filename

    if filedir != "":                           #if the directory is not empty
        os.makedirs(filedir, exist_ok=True)     #create the directory if it does not exist
        logging.info(f"Directory created: {filedir} for file: {filename}")

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):        #if the file does not exist
        with open(file, 'w') as f:              #create the file
            pass
            logging.info(f"File created: {file}")

    else:
        logging.info(f"File already exists: {filename}")
    