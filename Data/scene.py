#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Scene(object):
    def __init__(self, scene_folder_path):
        self.scene_folder_path = scene_folder_path
        if self.scene_folder_path[-1] != "/":
            self.scene_folder_path += "/"

        self.scene_name = None
        self.space_id = None
        self.scan_id = None

        self.sens = None
        self.vh_clean_ply = None
        self.vh_clean_segs_json = None
        self.aggregation_json = None
        self.vh_clean_aggregation_json = None
        self.txt = None
        return

    def update(self):
        if not os.path.exists(self.scene_folder_path):
            print("[ERROR][Scene::update]")
            print("\t scene_folder not exist!")
            return False

        self.scene_name = self.scene_folder_path.split("/")[-2]
        if "scene" not in self.scene_name:
            print("[ERROR][Scene::update]")
            print("\t scene_folder_name not valid!")
            return False

        self.space_id, self.scan_id = self.scene_name.split("scene")[1].split("_")
        return True

