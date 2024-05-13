# -*- coding: utf-8 -*-

import librosa
import os
import soundfile as sf
import numpy as np
import pathlib

#audiofile = 'E://OpenDR_datasets//RAVDESS//Actor_19//03-01-07-02-01-02-19.wav'
##this file preprocess audio files to ensure they are of the same length. if length is less than 3.6 seconds, it is padded with zeros in the end. otherwise, it is equally cropped from 
##both sides

root = '/scratch/work/huangg5/ravdess_ser/data/audio_speech'
# root = '/scratch/elec/puhe/c/ravdess/audio_speech/' 
# root = '/lustre/scratch/chumache/RAVDESS_or/'
outdir = '/scratch/work/huangg5/ravdess_ser/data/cropped-av/'
target_time = 3.6 #sec
for actor in os.listdir(root):
    for audiofile in os.listdir(os.path.join(root, actor)):
        
        if not audiofile.endswith('.wav') or 'croppad' in audiofile:
            continue

        audios = librosa.core.load(os.path.join(root, actor, audiofile), sr=22050)
	
        y = audios[0]
        sr = audios[1]
        target_length = int(sr * target_time)
        if len(y) < target_length:
            y = np.array(list(y) + [0 for i in range(target_length - len(y))])
        else:
            remain = len(y) - target_length
            y = y[remain//2:-(remain - remain//2)]
	    
        pathlib.Path(os.path.join(outdir, actor)).mkdir(parents=True, exist_ok=True)
        sf.write(os.path.join(outdir, actor, audiofile[:-4]+'_croppad.wav'), y, sr)

	
