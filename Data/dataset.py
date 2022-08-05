#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from Data.scene import Scene

class Dataset(object):
    def __init__(self, dataset_folder_path):
        self.dataset_folder_path = dataset_folder_path
        if self.dataset_folder_path[-1] != "/":
            self.dataset_folder_path += "/"

        self.scene_list = []

        self.is_valid = False

        self.update()
        return

    def updateSceneList(self):
        scene_folder_name_list = os.listdir(self.dataset_folder_path)
        for scene_folder_name in scene_folder_name_list:
            if "scene" not in scene_folder_name:
                continue
            scene_folder_path = self.dataset_folder_path + scene_folder_name + "/"
            self.scene_list.append(Scene(scene_folder_path))
        return True

    def update(self):
        if not os.path.exists(self.dataset_folder_path):
            print("[ERROR][Dataset::update]")
            print("\t dataset_folder not exist!")
            print("\t " + self.dataset_folder_path)
            return False

        if not self.updateSceneList():
            print("[ERROR][Dataset::update]")
            print("\t updateSceneList failed!")
            return False

        self.is_valid = True
        return True

    def isValid(self):
        return self.is_valid

    def outputInfo(self, info_level=0):
        line_start = "\t" * info_level
        print(line_start + "[Dataset]")
        print(line_start + "\t dataset_folder_path =", self.dataset_folder_path)
        print(line_start + "\t scene_num =", len(self.scene_list))
        print(line_start + "\t is_valid =", self.is_valid)
        print(line_start + "\t scene_list =")
        for scene in self.scene_list:
            scene.outputInfo(info_level + 2)
        return True

