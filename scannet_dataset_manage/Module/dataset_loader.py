#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_dataset_manage.Data.dataset import Dataset

class DatasetLoader(object):
    def __init__(self, dataset_folder_path):
        self.dataset = Dataset(dataset_folder_path)
        return

    def getSceneNum(self):
        return len(self.dataset.scene_list)

    def getScene(self, scene_idx):
        if scene_idx >= self.getSceneNum():
            print("[ERROR][DatasetLoader::getScene]")
            print("\t scene_idx out of range!")
            return None
        return self.dataset.scene_list[scene_idx]

def demo():
    dataset_folder_path = "/home/chli/chLi/ScanNet/scans/"

    dataset_loader = DatasetLoader(dataset_folder_path)
    return True

