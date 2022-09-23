#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append("../mesh-manage/")
from mesh_manage.Module.channel_mesh import ChannelMesh

import os
from tqdm import tqdm

from scannet_dataset_manage.Method.path import renameFile, removeIfExist

from scannet_dataset_manage.Module.dataset_loader import DatasetLoader


class ObjectSpliter(object):

    def __init__(self, dataset_folder_path, save_object_folder_path):
        self.dataset_loader = DatasetLoader(dataset_folder_path)
        self.save_object_folder_path = save_object_folder_path
        return

    def splitScene(self, scene):
        scene_name = scene.scene_name
        save_object_basepath = self.save_object_folder_path + scene_name + "/"

        scene_mesh_file_path = scene.vh_clean_2_ply
        assert scene_mesh_file_path is not None

        channel_mesh = ChannelMesh(scene_mesh_file_path)

        object_num = scene.getLabeledObjectNum()
        print("[INFO][ObjectSpliter::splitScene]")
        print("\t start split object in scene", scene_name, "...")
        for object_idx in tqdm(range(object_num)):
            labeled_object = scene.getLabeledObjectById(object_idx)
            assert labeled_object is not None

            save_object_mesh_file_path = save_object_basepath + \
                str(labeled_object.object_id) + \
                "_" + labeled_object.label + ".ply"
            if os.path.exists(save_object_mesh_file_path):
                continue

            tmp_save_object_mesh_file_path = save_object_mesh_file_path[:-4] + "_tmp.ply"
            removeIfExist(tmp_save_object_mesh_file_path)

            point_idx_list = scene.getPointIdxListByLabeledObject(
                labeled_object)
            assert channel_mesh.generateMeshByPoint(
                point_idx_list, tmp_save_object_mesh_file_path)

            renameFile(tmp_save_object_mesh_file_path,
                       save_object_mesh_file_path)
        return True

    def splitAll(self):
        # for me only
        finished_scene_idx = 317
        scene_name_list = self.dataset_loader.getSceneNameList()
        for i, scene_name in enumerate(scene_name_list):
            if i + 1 < finished_scene_idx:
                continue

            scene = self.dataset_loader.getScene(scene_name)
            assert scene is not None

            print("[INFO][ObjectSpliter::splitAll]")
            print("\t start split scene", scene.scene_name, ",", i + 1, "/",
                  len(scene_name_list), "...")
            self.splitScene(scene)
        return True


def demo():
    dataset_folder_path = "/home/chli/chLi/ScanNet/scans/"
    save_object_folder_path = "/home/chli/chLi/ScanNet/objects/"

    object_spliter = ObjectSpliter(dataset_folder_path,
                                   save_object_folder_path)
    object_spliter.splitAll()
    return True
