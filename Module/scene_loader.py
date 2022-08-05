#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Data.scene import Scene

class SceneLoader(object):
    def __init__(self, scene_folder_path):
        self.scene = Scene(scene_folder_path)
        return

def demo():
    scene_folder_path = "/home/chli/scan2cad/scannet/scans/scene0474_02/"
    scene_loader = SceneLoader(scene_folder_path)
    return True

