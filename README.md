# LDSSS2017

This repository contains materials for "Deep Learning for Computer Vision" course, Lviv Data Science Summer School.

To start to work on it locally clone this repository

```
git clone https://github.com/lyubonko/LDSSS2017.git
``` 
or download as a zip file.

## Lectures

The lectures in html format are available in folder 'lectures'.


## Assignments
1. [Introduction to pytorch] assignments/a1_pytorch.ipynb
2. [Dataset] assignments/a2_dataset_cifar10.ipynb OR assignments/a2_dataset_dtd.ipynb
3. [Two layer network] assignments/a3_two_layer_network.ipynb
4. [Convolutional Neural Network] assignments/a4_cnn.ipynb

## Required packages
1. jupyter notebook
2. matplotlib
3. pytorch

To install pytorch follow the instructions on http://pytorch.org/ for your environment.

There may be some issues with pytorch for Windows. You can try one of the following ways to have pytorch for Windows OS.

**Install pytorch directly from Windows**

conda install -c peterjc123 pytorch=0.1.12 
see discussion on https://github.com/pytorch/pytorch/issues/494 
remarks: the guy who tested it had Python 3.6.1

**Use docker**
1. install docker on Windows, follow official documentation
2. pull the docker image with anaconda 3.6 by running
docker pull continuumio/anaconda3
from: https://hub.docker.com/r/continuumio/anaconda3/
3. run the this docker locally and install pytorch
conda install pytorch torchvision -c soumith
see for details:
http://pytorch.org/

**Use virtual machine**
1. install VirtualBox, follow official documentation
https://www.virtualbox.org/
2. install Ubuntu 16.04 on it
3. install Anaconda with python 3.6, following official docemntation
4. install pytorch
