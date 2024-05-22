#!/bin/bash
#SBATCH --time=00:59:59
#SBATCH --mem=250G
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=6
#SBATCH --output=logs/%A.out
#SBATCH --job-name=merr
#SBATCH -n 1

module load mamba

source activate merr

## Jupyter: https://scicomp.aalto.fi/triton/apps/jupyter/
# module load jupyterhub/live
# envkernel conda --user --name huangg5 --display-name="merr" /scratch/work/huangg5/.conda_envs/merr

# cd ravdess_preprocessing
# python extract_faces.py
# python extract_audios.py
# python create_annotations.py
# cd ..

/usr/bin/time -v python main.py 
# python main.py --no_train
# python main.py --no_train --no_val --test

## setup
# update librosa to be compatible with numpy in requirements.txt
# 162328 Prec1: 81.04167
# 221383 multi_acc: 80.7
# 232175 --test 80.7
