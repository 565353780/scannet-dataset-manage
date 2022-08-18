#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
sys.path.append("../mesh_manage/")
from tqdm import tqdm

from mesh_manage.Module.channel_mesh import ChannelMesh
from Module.dataset_loader import DatasetLoader

class ObjectSpliter(object):
    def __init__(self, dataset_folder_path, save_object_folder_path):
        self.dataset_loader = DatasetLoader(dataset_folder_path)
        self.save_object_folder_path = save_object_folder_path
        if self.save_object_folder_path[-1] != "/":
            self.save_object_folder_path += "/"
        return

    def splitScene(self, scene):
        scene_name = scene.scene_name
        save_object_basepath = self.save_object_folder_path + scene_name + "/"

        scene_mesh_file_path = scene.vh_clean_2_ply
        if scene_mesh_file_path is None:
            print("[ERROR][ObjectSpliter::splitScene]")
            print("\t scene_mesh_file not found!")
            return False
        channel_mesh = ChannelMesh(scene_mesh_file_path)

        object_num = scene.getLabeledObjectNum()
        print("[INFO][ObjectSpliter::splitScene]")
        print("\t start split object in scene", scene_name, "...")
        for object_idx in tqdm(range(object_num)):
            labeled_object = scene.getLabeledObjectById(object_idx)
            if labeled_object is None:
                print("[ERROR][ObjectSpliter::splitObject]")
                print("\t getLabeledObjectById failed!")
                return False

            save_object_mesh_file_path = save_object_basepath + \
                str(labeled_object.object_id) + \
                "_" + labeled_object.label + ".ply"

            point_idx_list = scene.getPointIdxListByLabeledObject(labeled_object)
            if not channel_mesh.generateMeshByPoint(point_idx_list, save_object_mesh_file_path):
                print("[ERROR][ObjectSpliter::splitObject]")
                print("\t generateMeshByPoint failed!")
                return False
        return True

    def splitAll(self):
        scene_num = self.dataset_loader.getSceneNum()
        for scene_idx in range(scene_num):
            scene = self.dataset_loader.getScene(scene_idx)
            if scene is None:
                print("[ERROR][ObjectSpliter::splitAll]")
                print("\t getScene failed!")
                return False

            print("[INFO][ObjectSpliter::splitAll]")
            print("\t start split scene", scene.scene_name, ",", scene_idx + 1, "/", scene_num, "...")
            self.splitScene(scene)
            return
        return True

def demo():
    dataset_folder_path = "/home/chli/chLi/ScanNet/scans/"
    save_object_folder_path = "/home/chli/chLi/ScanNet/objects/"

    object_spliter = ObjectSpliter(dataset_folder_path, save_object_folder_path)
    object_spliter.splitAll()
    return True

