#!/usr/bin/env bash

# Create env and install dependencies
#conda create --name pymarl python=3.7
#conda activate pymarl

conda install --name pymarl -c pytorch pytorch torchvision
python -m pip install numpy scipy pyyaml matplotlib imageio tensorboard-logger pygame setuptools snakeviz pytest probscale sacred gym

# Install SMAC and QPLEX SMAC MATRIX GAMES
python -m pip install -e smac
python -m pip install -e ../QPLEX_smac_env

# Install SC2 and add the custom maps
mkdir 3rdparty
cd 3rdparty

export SC2PATH=`pwd`'/StarCraftII'
echo 'SC2PATH is set to '$SC2PATH

if [ ! -d $SC2PATH ]; then
        echo 'StarCraftII is not installed. Installing now ...';
        wget http://blzdistsc2-a.akamaihd.net/Linux/SC2.4.6.2.69232.zip
        unzip -P iagreetotheeula SC2.4.6.2.69232.zip
        rm -rf SC2.4.6.2.69232.zip
else
        echo 'StarCraftII is already installed.'
fi

echo 'Adding SMAC maps.'
MAP_DIR="$SC2PATH/Maps/"
echo 'MAP_DIR is set to '$MAP_DIR

if [ ! -d $MAP_DIR ]; then
        mkdir -p $MAP_DIR
fi

cd ..
wget https://github.com/oxwhirl/smac/releases/download/v0.1-beta1/SMAC_Maps.zip
unzip SMAC_Maps.zip
mv SMAC_Maps $MAP_DIR
rm -rf SMAC_Maps.zip

echo 'StarCraft II and SMAC are installed.'
