from __future__ import print_function
# %matplotlib inline
import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from absl import app
from absl import flags
from absl import logging

FLAGS = flags.FLAGS
flags.DEFINE_string("workdir", default=".", help="Where to store log output.")
flags.DEFINE_string('dataroot', default='dataset/',
                    help='the path to the root of the dataset folder.')
flags.DEFINE_integer('workers', default=2,
                     help='the number of worker threads for loading the data with the DataLoader')
flags.DEFINE_integer('seed', default=999,
                     help='random seed for reproducibility')
flags.DEFINE_integer('batch_size', default=128, help='')



# # Set random seed for reproducibility
# manualSeed = 999
# print("Random Seed: ", manualSeed)
# random.seed(manualSeed)
# torch.manual_seed(manualSeed)
