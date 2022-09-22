#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_dataset_manage.Data.dataset import Dataset


class DatasetLoader(object):

    def __init__(self, dataset_folder_path=None):
        self.dataset = Dataset(dataset_folder_path)
        return

    def getSceneNum(self):
        return len(self.dataset.scene_dict.keys())

    def getSceneNameList(self):
        return list(self.dataset.scene_dict.keys())

    def getScene(self, scene_name):
        if scene_name not in self.dataset.scene_dict.keys():
            print("[ERROR][DatasetLoader::getScene]")
            print("\t scene_name out of range!")
            return None
        return self.dataset.scene_dict[scene_name]


def demo():
    dataset_folder_path = "/home/chli/chLi/ScanNet/scans/"

    dataset_loader = DatasetLoader(dataset_folder_path)
    scene_num = dataset_loader.getSceneNum()
    print("scene_num =", scene_num)
    scene_name_list = dataset_loader.getSceneNameList()
    print("scene_name_list =", scene_name_list)
    return True
