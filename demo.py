#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_dataset_manage.Demo.dataset_loader import demo as demo_load_dataset
from scannet_dataset_manage.Demo.object_spliter import demo as demo_split_object
from scannet_dataset_manage.Demo.object_bbox_generator import demo as demo_generate_object_bbox
from scannet_dataset_manage.Demo.glb_generator import demo as demo_generate_glb

if __name__ == "__main__":
    #  demo_load_dataset()
    demo_split_object()
    demo_generate_object_bbox()
    demo_generate_glb()
