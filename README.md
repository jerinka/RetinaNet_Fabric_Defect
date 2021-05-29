# RetinaNet_Fabric defect detection

## clone repo

```git clone https://github.com/jerinka/RetinaNet_Fabric_Defect.git```

## RetinaNet

![RetinanNet](c7uqwbldw9w4zhbzmyo8.png)

## Defect detection

RetinaNet detects fabric defects: Stain, Line, Hole

Green rectangle is ground truth

Other color is detection

## Requirement 

Ubuntu 18.04

Might work in windows too(no guarantee), but some of the packages version might have to be changed. 

## Steps to run: 

cd RetinaNet_Fabric_Defect

virtualenv venvR --python=python3

source venvR/bin/activate

pip3 install jupyter notebook

python -m pip install ipykernel

python -m ipykernel install --user --name=venvR

## may refer link below incase of any difficulty in running jupter in virtualenv
![running-jupyter-in-venv](http://veekaybee.github.io/2020/02/18/running-jupyter-in-venv/)
![another link](https://janakiev.com/blog/jupyter-virtual-envs/)

jupyter notebook

Open RetinaMask.ipynb

Press shift+enter to execute cells





