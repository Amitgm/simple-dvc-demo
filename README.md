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




<!-- dvc metrics show -->
<!-- dvc metrics diff -->