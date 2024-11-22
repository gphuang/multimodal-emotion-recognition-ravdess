#!/bin/bash
#SBATCH --time=10:59:59
#SBATCH --mem=250G
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=6
#SBATCH --output=logs/%A.out
#SBATCH --job-name=merr
#SBATCH -n 1

module load mamba

source activate ser_venv

## Jupyter: https://scicomp.aalto.fi/triton/apps/jupyter/
# module load jupyterhub/live
# envkernel conda --user --name huangg5 --display-name="merr" /scratch/work/huangg5/.conda_envs/merr

# cd ravdess_preprocessing
# python extract_faces.py  # save_length=None (full), 1, 3
# python extract_audios.py
# python create_annotations.py 
# cd ..


ANNOTATION_PATH="ravdess_preprocessing/annotations_cropped_1sec_fold1.txt"
# /usr/bin/time -v python main.py --annotation_path $ANNOTATION_PATH --n_epochs 1 
# python main.py --no_train
python main.py --no_train --no_val --test --annotation_path $ANNOTATION_PATH # --n_epochs 1

## setup
# update librosa to be compatible with numpy in requirements.txt
# 162328 Prec1: 81.04167
# 221383 multi_acc: 80.7
# 232175 --test 80.7

## Architecture
# CNN
# RNN
# CRNN
# CRNN-ATTN

## Temporal
# 1~10 seconds
# first last 

## Modality
#
