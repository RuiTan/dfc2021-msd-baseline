import functools

import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

import segmentation_models_pytorch as smp

import utils

class FCN(nn.Module):

    def __init__(self, num_input_channels, num_output_classes, num_filters=64):
        super(FCN,self).__init__()

        self.conv1 = nn.Conv2d(num_input_channels, num_filters, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(num_filters, num_filters,        kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(num_filters, num_filters,        kernel_size=3, stride=1, padding=1)
        self.conv4 = nn.Conv2d(num_filters, num_filters,        kernel_size=3, stride=1, padding=1)
        self.conv5 = nn.Conv2d(num_filters, num_filters,        kernel_size=3, stride=1, padding=1)
        self.last =  nn.Conv2d(num_filters, num_output_classes, kernel_size=1, stride=1, padding=0)

    def forward(self,inputs):
        x = F.relu(self.conv1(inputs))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = F.relu(self.conv5(x))
        x = self.last(x)
        return x


def get_unet():
    return smp.Unet(
        encoder_name='resnet18', encoder_depth=3, encoder_weights=None,
        decoder_channels=(128, 64, 64), in_channels=4, classes=utils.NLCD_CLASSES_COUNT
    )

def get_fcn(num_input_channels=4):
    return FCN(num_input_channels=num_input_channels, num_output_classes=utils.NLCD_CLASSES_COUNT, num_filters=64)

def get_deeplabv3p():
    return smp.DeepLabV3Plus(encoder_name='resnet34', encoder_depth=5, encoder_weights=None,
                encoder_output_stride=16, decoder_channels=256, decoder_atrous_rates=(12, 24, 36),
                in_channels=4, classes=utils.NLCD_CLASSES_COUNT, activation=None, upsampling=4, aux_params=None)

def get_unetpp():
    return smp.UnetPlusPlus(encoder_name='resnet34', encoder_depth=5, encoder_weights=None,
                            decoder_use_batchnorm=True, decoder_channels=(256, 128, 64, 32, 16),
                            decoder_attention_type=None, in_channels=4,
                            classes=utils.NLCD_CLASSES_COUNT, activation=None, aux_params=None)