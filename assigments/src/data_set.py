from __future__ import print_function
from __future__ import division

import os

# torch stuff
import torch
import torch.utils.data as data
import torchvision.transforms as transforms
import torchvision.datasets as dsets

imagenet_mean = [0.485, 0.456, 0.406]
imagenet_std = [0.229, 0.224, 0.225]


class DataSetCifar10(object):
    """
    Class manage CIFAR10 data-set
    """

    def __init__(self,
                 path_data,
                 num_dunkeys=4,
                 batch_size=100):

        init_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=imagenet_mean,
                                 std=imagenet_std)
        ])

        self.dataset = {}
        self.dataset['train'] = dsets.CIFAR10(root=path_data,
                                      train=True,
                                      transform=init_transform)

        self.dataset['test'] = dsets.CIFAR10(root=path_data,
                                    train=False,
                                    transform=init_transform)

        self.loader = {}
        self.loader['train'] = torch.utils.data.DataLoader(dataset=self.dataset['train'],
                                                           batch_size=batch_size,
                                                           shuffle=True,
                                                           num_workers=num_dunkeys)

        self.loader['test'] = torch.utils.data.DataLoader(dataset=self.dataset['test'],
                                                          batch_size=batch_size,
                                                          shuffle=False,
                                                          num_workers=num_dunkeys)


class DataSetDTD(object):
    """ 
    Class manage DTD data-set
    """

    def __init__(self,
                 path_data,
                 num_dunkeys=4,
                 batch_size=100,
                 fin_scale=32):

        init_transform = transforms.Compose([
            transforms.Scale(224),
            transforms.CenterCrop(224),
            transforms.Scale(fin_scale),
            transforms.ToTensor(),
            transforms.Normalize(mean=imagenet_mean,
                                 std=imagenet_std)
        ])

        self.dataset = {}
        self.dataset['train'] = dsets.ImageFolder(root=os.path.join(path_data, 'train'),
                                          transform=init_transform,
                                          target_transform=None)

        self.dataset['test'] = dsets.ImageFolder(root=os.path.join(path_data, 'test'),
                                        transform=init_transform,
                                        target_transform=None)

        self.loader = {}
        self.loader['train'] = torch.utils.data.DataLoader(dataset=self.dataset['train'],
                                                           batch_size=batch_size,
                                                           shuffle=True,
                                                           num_workers=num_dunkeys)

        self.loader['test'] = torch.utils.data.DataLoader(dataset=self.dataset['test'],
                                                          batch_size=batch_size,
                                                          shuffle=False,
                                                          num_workers=num_dunkeys)
