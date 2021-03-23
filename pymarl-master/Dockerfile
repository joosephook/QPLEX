FROM continuumio/miniconda3:4.9.2

WORKDIR /opt
RUN conda info --envs
RUN conda create --name pymarl python=3.7

ENV python=/opt/conda/envs/pymarl/bin/python
ENV conda_install=conda\ install\ -n\ pymarl

#RUN conda activate pymarl
#RUN conda info --envs
#RUN ls /opt/conda/envs/pymarl/bin

# Python packages we use (or used at one point...)
RUN $conda_install pytorch torchvision
RUN $python -m pip install numpy scipy pyyaml matplotlib imageio tensorboard-logger pygame setuptools snakeviz pytest probscale

RUN mkdir /install
WORKDIR /install

RUN $python -m pip install sacred
RUN git clone https://github.com/oxwhirl/smac.git && $python -m pip install -e smac

COPY QPLEX_smac_env QPLEX_smac_env
RUN $python -m pip install -e QPLEX_smac_env

ENV SC2PATH /pymarl/3rdparty/StarCraftII

# cd QPLEX_smac_env && $python setup.py install

WORKDIR /pymarl
