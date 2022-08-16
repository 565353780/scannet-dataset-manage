#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Data.scene import Scene

class SceneLoader(object):
    def __init__(self, scene_folder_path):
        self.scene = Scene(scene_folder_path)
        return

    def getLabeledObjectNum(self):
        return self.scene.getLabeledObjectNum()

    def getPointIdxListByLabeledObjectId(self, labeled_object_id):
        labeled_object = self.scene.getLabeledObjectById(labeled_object_id)
        if labeled_object is None:
            print("[ERROR][SceneLoader::getPointIdxListByLabeledObjectId]")
            print("\t getLabeledObjectById failed!")
            return None
        return self.scene.getPointIdxListByLabeledObject(labeled_object)

def demo():
    scene_folder_path = "/home/chli/chLi/ScanNet/scans/scene0000_00/"

    scene_loader = SceneLoader(scene_folder_path)
    labeled_object_num = scene_loader.getLabeledObjectNum()
    for i in range(labeled_object_num):
        point_idx_list = scene_loader.getPointIdxListByLabeledObjectId(i)
        print("object", i, "have", len(point_idx_list), "points")
    return True

