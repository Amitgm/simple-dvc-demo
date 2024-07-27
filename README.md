create env
conda create -n wineq python=3.7 -y

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