from os.path import dirname, abspath, join as pjoin
import scipy.io as sio
from pathlib import Path


def load():
    data = sio.loadmat('/Users/ryangreen/Desktop/Procedure Learning Research/data/assemble_clarinet/data.mat')
    print("foo")

if __name__ == "__main__":
    load()
