#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from Data.scene import Scene

class SceneLoader(object):
    def __init__(self, scene_folder_path):
        self.scene = Scene(scene_folder_path)
        return

    def getLabeledObjectNum(self):
        return len(self.scene.labeled_object_list)

    def getLabeledObjectById(self, labeled_object_id):
        for labeled_object in self.scene.labeled_object_list:
            if labeled_object.id == labeled_object_id:
                return labeled_object

        print("[ERROR][SceneLoader::getLabeledObjectById]")
        print("\t labeled_object with this id not found!")
        return None

    def getPointIdxListBySegmentIdxList(self, segment_idx_list):
        point_idx_list = np.where(np.isin(self.scene.segment_idx_list, segment_idx_list))[0].tolist()
        return point_idx_list

    def getPointIdxListByLabeledObjectId(self, labeled_object_id):
        labeled_object = self.getLabeledObjectById(labeled_object_id)
        if labeled_object is None:
            print("[ERROR][SceneLoader::getObjectPointIdxList]")
            print("\t getLabeledObjectById failed!")
            return None

        object_segment_idx_list = labeled_object.segment_idx_list
        point_idx_list = self.getPointIdxListBySegmentIdxList(object_segment_idx_list)
        return point_idx_list

def demo():
    scene_folder_path = "/home/chli/chLi/ScanNet/scans/scene0000_00/"

    scene_loader = SceneLoader(scene_folder_path)
    labeled_object_num = scene_loader.getLabeledObjectNum()
    print(labeled_object_num)
    point_idx_list = scene_loader.getPointIdxListByLabeledObjectId(0)
    print(point_idx_list)
    return True

