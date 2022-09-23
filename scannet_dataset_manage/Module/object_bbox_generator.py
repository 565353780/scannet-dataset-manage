#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append("../mesh-manage/")
from mesh_manage.Module.channel_mesh import ChannelMesh

import os
import json
from tqdm import tqdm

from scannet_dataset_manage.Method.path import createFileFolder


class ObjectBBoxGenerator(object):

    def __init__(self):
        self.object_bbox_dict = {}
        return

    def reset(self):
        self.object_bbox_dict = {}
        return True

    def getObjectBBox(self, object_file_path):
        assert os.path.exists(object_file_path)
        return ChannelMesh(object_file_path).getBBox().toList()

    def getSceneObjectBBoxDict(self, scene_folder_path):
        assert os.path.exists(scene_folder_path)

        scene_object_bbox_dict = {}

        object_file_name_list = os.listdir(scene_folder_path)
        print("[INFO][ObjectBBoxGenerator::getSceneObjectBBoxDict]")
        print("\t start get scene object bbox dict...")
        for object_file_name in tqdm(object_file_name_list):
            object_file_path = scene_folder_path + object_file_name

            scene_object_bbox_dict[object_file_name] = self.getObjectBBox(
                object_file_path)
        return scene_object_bbox_dict

    def loadAllObjectBBox(self, objects_folder_path):
        assert os.path.exists(objects_folder_path)

        self.reset()

        scene_name_list = os.listdir(objects_folder_path)
        for i, scene_name in enumerate(scene_name_list):
            scene_folder_path = objects_folder_path + scene_name + "/"

            print("[INFO][ObjectBBoxGenerator::loadAllObjectBBox]")
            print("\t start split scene", scene_name, ",", i + 1, "/",
                  len(scene_name_list), "...")
            self.object_bbox_dict[scene_name] = self.getSceneObjectBBoxDict(
                scene_folder_path)
        return True

    def generateObjectBBoxJson(self, objects_folder_path, save_json_file_path):
        assert self.loadAllObjectBBox(objects_folder_path)

        createFileFolder(save_json_file_path)

        with open(save_json_file_path, "w") as f:
            f.write(json.dumps(self.object_bbox_dict))
        return True


def demo():
    objects_folder_path = "/home/chli/chLi/ScanNet/objects/"
    save_json_file_path = "/home/chli/chLi/ScanNet/bboxs/object_bbox.json"

    object_bbox_generator = ObjectBBoxGenerator()
    object_bbox_generator.generateObjectBBoxJson(objects_folder_path,
                                                 save_json_file_path)
    return True
