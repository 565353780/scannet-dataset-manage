#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_dataset_manage.Module.dataset_loader import demo as demo_dataset
from scannet_dataset_manage.Module.object_spliter import demo as demo_split_object
from scannet_dataset_manage.Module.object_bbox_generator import demo as demo_generate_object_bbox


def autoExtractDataset():
    demo_split_object()
    demo_generate_object_bbox()
    return True


if __name__ == "__main__":
    #  demo_dataset()
    demo_split_object()
    demo_generate_object_bbox()

    #  autoExtractDataset()
