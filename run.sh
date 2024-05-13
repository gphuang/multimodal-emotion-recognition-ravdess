#!/bin/bash
#SBATCH --time=47:59:59
#SBATCH --mem=250G
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=6
#SBATCH --output=logs/%A.out
#SBATCH --job-name=merr
#SBATCH -n 1

module load mamba

source activate merr

# cd ravdess_preprocessing
# python extract_faces.py
# python extract_audios.py
# python create_annotations.py
# cd ..

/usr/bin/time -v python main.py 

## setup
# update librosa to be compatible with numpy in requirements.txt
# Done extract features
# 158879 training
