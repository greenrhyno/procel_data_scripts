from os.path import dirname, abspath, join as pjoin
import scipy.io as sio
from pathlib import Path

data = sio.loadmat('/Users/ryangreen/Desktop/Procedure Learning Research/data/assemble_clarinet/data.mat')

video_idx = 0
for video in data['key_steps'][:,0]:
    print('\n' + str(video_idx) + '\n')
    steps = [step_range.tolist() for step_range in video[:,0]]
    
    # make superframe mapping to all background class 'SIL'
    groundtruth = ['SIL'] * data['superframe_frame'][video_idx][0].shape[0]
    
    for step_idx in range(len(steps)):
        step = steps[step_idx]
        key_step_name = data['grammar'][:,0][step_idx][0]
        
        for segment in step:
            if len(segment) == 2:
                for sf_idx in range(segment[0], segment[1]):
                    groundtruth[sf_idx] = key_step_name
    print(groundtruth)
    video_idx += 1