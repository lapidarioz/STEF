#!/usr/bin/env bash

if ! type "conda" > /dev/null; then
    wget -O /tmp/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x /tmp/miniconda.sh
    bash /tmp/miniconda.sh
    source ~/.bashrc
fi
conda update -y -n base conda
conda create --name stef
source activate stef
conda install -y numpy pandas xlrd matplotlib scikit-learn pathlib scipy
pip install seasnake
python main.py
