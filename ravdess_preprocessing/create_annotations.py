# -*- coding: utf-8 -*-

import os
#root = '/lustre/scratch/chumache/RAVDESS_or/'
root = '/scratch/work/huangg5/ravdess_ser/data/av'

save_length = 4 #None 1~3.6sec
if save_length:         
    _cropped=f'cropped_{save_length}sec'
else:
    _cropped='full'

# todo: k-fold cv validation
n_folds=1
folds = [[[0,1,2,3],[4,5,6,7],[8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]],
         ]
for fold in range(n_folds):
        fold_ids = folds[fold]
        test_ids, val_ids, train_ids = fold_ids
	
        annotation_file = 'annotations_' + _cropped + '_fold'+str(fold+1)+'.txt'
        # annotation_file = 'annotations.txt'
	
        for i,actor in enumerate(os.listdir(root)):
            for video in os.listdir(os.path.join(root, actor)):
                if not video.endswith('.npy') or video.startswith('01') or not _cropped in video: # 01 - full A/V modality
                    continue
                label = str(int(video.split('-')[2]))
		     
                audio = '03' + os.path.basename(video)[2:-4] + '.wav' # replace 02 with 03 - audio modality, replace extension 
                if i in train_ids:
                   with open(annotation_file, 'a') as f:
                       f.write(os.path.join(root,actor, video) + ';' + os.path.join(root,actor, audio) + ';' + label + ';training' + '\n')
		

                elif i in val_ids:
                    with open(annotation_file, 'a') as f:
                        f.write(os.path.join(root, actor, video) + ';' + os.path.join(root,actor, audio) + ';'+ label + ';validation' + '\n')
		
                else:
                    with open(annotation_file, 'a') as f:
                        f.write(os.path.join(root, actor, video) + ';' + os.path.join(root,actor, audio) + ';'+ label + ';testing' + '\n')
		

