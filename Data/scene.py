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
        self.file_basepath = None

        self.aggregation_json = None
        self.sens = None
        self.txt = None
        self.vh_clean_aggregation_json = None
        self.vh_clean_ply = None
        self.vh_clean_segs_json = None
        self.vh_clean_2_segs_json = None
        self.vh_clean_2_labels_ply = None
        self.vh_clean_2_ply = None

        self.is_valid = False

        self.update()
        return

    def updateSceneId(self):
        self.scene_name = self.scene_folder_path.split("/")[-2]
        if "scene" not in self.scene_name:
            print("[ERROR][Scene::updateSceneId]")
            print("\t scene_folder_name not valid!")
            return False

        self.space_id, self.scan_id = self.scene_name.split("scene")[1].split("_")
        return True

    def updateFilePath(self):
        self.file_basepath = self.scene_folder_path + self.scene_name

        not_exist_file_path_list = []

        aggregation_json = self.file_basepath + ".aggregation.json"
        if os.path.exists(aggregation_json):
            self.aggregation_json = aggregation_json
        else:
            not_exist_file_path_list.append(aggregation_json)

        sens = self.file_basepath + ".sens"
        if os.path.exists(sens):
            self.sens = sens
        else:
            not_exist_file_path_list.append(sens)

        txt = self.file_basepath + ".txt"
        if os.path.exists(txt):
            self.txt = txt
        else:
            not_exist_file_path_list.append(txt)

        vh_clean_aggregation_json = self.file_basepath + "_vh_clean.aggregation.json"
        if os.path.exists(vh_clean_aggregation_json):
            self.vh_clean_aggregation_json = vh_clean_aggregation_json
        else:
            not_exist_file_path_list.append(vh_clean_aggregation_json)

        vh_clean_ply = self.file_basepath + "_vh_clean.ply"
        if os.path.exists(vh_clean_ply):
            self.vh_clean_ply = vh_clean_ply
        else:
            not_exist_file_path_list.append(vh_clean_ply)

        vh_clean_segs_json = self.file_basepath + "_vh_clean.segs.json"
        if os.path.exists(vh_clean_segs_json):
            self.vh_clean_segs_json = vh_clean_segs_json
        else:
            not_exist_file_path_list.append(vh_clean_segs_json)

        vh_clean_2_segs_json = self.file_basepath + "_vh_clean_2.0.010000.segs.json"
        if os.path.exists(vh_clean_2_segs_json):
            self.vh_clean_2_segs_json = vh_clean_2_segs_json
        else:
            not_exist_file_path_list.append(vh_clean_2_segs_json)

        vh_clean_2_labels_ply = self.file_basepath + "_vh_clean_2.labels.ply"
        if os.path.exists(vh_clean_2_labels_ply):
            self.vh_clean_2_labels_ply = vh_clean_2_labels_ply
        else:
            not_exist_file_path_list.append(vh_clean_2_labels_ply)

        vh_clean_2_ply = self.file_basepath + "_vh_clean_2.ply"
        if os.path.exists(vh_clean_2_ply):
            self.vh_clean_2_ply = vh_clean_2_ply
        else:
            not_exist_file_path_list.append(vh_clean_2_ply)

        if len(not_exist_file_path_list) > 0:
            print("[WARN][Scene::updateFilePath]")
            print("\t find some files not exist!")
            for not_exist_file_path in not_exist_file_path_list:
                print("\t\t " + not_exist_file_path)
        return True

    def update(self):
        if not os.path.exists(self.scene_folder_path):
            print("[ERROR][Scene::update]")
            print("\t scene_folder not exist!")
            print("\t " + self.scene_folder_path)
            return False

        if not self.updateSceneId():
            print("[ERROR][Scene::update]")
            print("\t updateSceneId failed!")
            return False

        if not self.updateFilePath():
            print("[ERROR][Scene::update]")
            print("\t updateFilePath failed!")
            return False

        self.is_valid = True
        return True

    def isValid(self):
        return self.is_valid

    def outputInfo(self, info_level=0):
        line_start = "\t" * info_level
        print(line_start + "[Scene]")
        print(line_start + "\t scene_folder_path =", self.scene_folder_path)
        print(line_start + "\t scene_name =", self.scene_name)
        print(line_start + "\t space_id =", self.space_id)
        print(line_start + "\t scan_id =", self.scan_id)
        print(line_start + "\t is_valid =", self.is_valid)
        return True

