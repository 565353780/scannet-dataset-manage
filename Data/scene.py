#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import numpy as np

from Data.labeled_object import LabeledObject

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

        self.segment_idx_list = []
        self.labeled_object_list = []

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

    def loadSegmentIdx(self):
        if self.vh_clean_2_segs_json is None:
            print("[ERROR][Scene::loadSegmentIdx]")
            print("\t file vh_clean_2_segs_json not exist!")
            return False

        vh_clean_2_segs_json = {}
        with open(self.vh_clean_2_segs_json, "r") as f:
            vh_clean_2_segs_json = json.load(f)

        if "segIndices" not in vh_clean_2_segs_json.keys():
            print("[ERROR][Scene::loadSegmentIdx]")
            print("\t key segIndices not found!")
            return False

        self.segment_idx_list = vh_clean_2_segs_json["segIndices"]
        return True

    def loadAggregation(self):
        if self.vh_clean_aggregation_json is None:
            print("[ERROR][Scene::loadAggregation]")
            print("\t file vh_clean_aggregation_json not exist!")
            return False

        vh_clean_aggregation_json = {}
        with open(self.vh_clean_aggregation_json, "r") as f:
            vh_clean_aggregation_json = json.load(f)

        if "segGroups" not in vh_clean_aggregation_json.keys():
            print("[ERROR][Scene::loadAggregation]")
            print("\t key segGroups not found!")
            return False

        for object_dict in vh_clean_aggregation_json["segGroups"]:
            labeled_object = LabeledObject(object_dict=object_dict)
            self.labeled_object_list.append(labeled_object)
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

        if not self.loadSegmentIdx():
            print("[ERROR][Scene::loadData]")
            print("\t loadSegmentIdx failed!")
            return False
        if not self.loadAggregation():
            print("[ERROR][Scene::loadData]")
            print("\t loadAggregation failed!")
            return False
        return True

    def getLabeledObjectNum(self):
        return len(self.labeled_object_list)

    def getLabeledObjectById(self, labeled_object_id):
        for labeled_object in self.labeled_object_list:
            if labeled_object.id == labeled_object_id:
                return labeled_object

        print("[ERROR][Scene::getLabeledObjectById]")
        print("\t labeled_object with this id not found!")
        return None

    def getLabeledObjectByObjectId(self, labeled_object_object_id):
        for labeled_object in self.labeled_object_list:
            if labeled_object.object_id == labeled_object_object_id:
                return labeled_object

        print("[ERROR][Scene::getLabeledObjectByObjectId]")
        print("\t labeled_object with this object_id not found!")
        return None

    def getPointIdxListBySegmentIdxList(self, segment_idx_list):
        point_idx_list = np.where(np.isin(self.segment_idx_list, segment_idx_list))[0].tolist()
        return point_idx_list

    def getPointIdxListByLabeledObject(self, labeled_object):
        if labeled_object is None:
            print("[ERROR][Scene::getPointIdxListByLabeledObject]")
            print("\t labeled_object is None!")
            return None

        object_segment_idx_list = labeled_object.segment_idx_list
        point_idx_list = self.getPointIdxListBySegmentIdxList(object_segment_idx_list)
        return point_idx_list

    def outputInfo(self, info_level=0):
        line_start = "\t" * info_level
        print(line_start + "[Scene]")
        print(line_start + "\t scene_folder_path =", self.scene_folder_path)
        print(line_start + "\t scene_name =", self.scene_name)
        print(line_start + "\t space_id =", self.space_id)
        print(line_start + "\t scan_id =", self.scan_id)
        return True

