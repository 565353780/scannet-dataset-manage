#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
sys.path.append("../mesh_manage/")

from mesh_manage.Module.mesh_loader import MeshLoader

class ObjectSpliter(object):
    def __init__(self):
        self.mesh_loader = MeshLoader()
        return

def demo():
    object_spliter = ObjectSpliter()
    return True

