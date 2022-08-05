#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Data.dataset import Dataset

class DatasetLoader(object):
    def __init__(self, dataset_folder_path):
        self.dataset = Dataset(dataset_folder_path)
        return

def demo():
    dataset_folder_path = "/home/chli/scan2cad/scannet/scans/"
    dataset_loader = DatasetLoader(dataset_folder_path)

    print(len(dataset_loader.dataset.scene_list))
    return True

