import torch
from torch import *
import torch.nn.functional as F


class CorrFusion(nn.Module):
    def __init__(self):
        super(CorrFusion, self).__init__()

