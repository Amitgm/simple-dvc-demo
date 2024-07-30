create env
conda create -n wineq python=3.7 -y

Install dvc version 2.10.2,
Check which dvc is used (the one in venv),
Check fsspec version number (== 2023.1.0),
Force reinstall to downgrade fsspec to 2022.11.0,
Check fsspec version number again (== 2022.11.0), and
Force initialize dvc since there is an existing .dvc folder in the project directory.

activate env
conda activate wineq

install requirements
pip install -r requirements.txt

get the dataset

git init 

dvc init

dvc add data_given/winequalityN.csv

git add .

git commit -m  "first commit"

git remote add origin https://github.com/Amitgm/simple-dvc-demo
git branch -M main
git push origin main

tox command-

'''bash
tox
'''

for rebuilding
'''bash
tox -r
'''

pytest -v

setup commands -
pip install -e .

build your own package commands
'''bash
python setup.py sdist bdist wheel
'''bash


----
mlflow server command

mlflow server \

    <!-- storing the data in mlflow db -->
    --backend-store-uri sqlite:///mlflow.db \
    <!-- storing the model part -->   
     <!-- create an artifacts folder for this  -->
    --default-artifact-root ./artifacts \
    --host 0.0.0.0 -p 1234



mlflow server \

    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./artifacts \
    --host 0.0.0.0 -p 1234

    --host 127.0.0.1 -p 5000
    

To do github actions for another branch, specify branch name in ci-cd.yaml


<!-- dvc metrics show -->
<!-- dvc metrics diff -->

<!-- pip install -e . -->