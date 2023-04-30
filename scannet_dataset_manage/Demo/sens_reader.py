#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_dataset_manage.Module.sens_reader import SensReader


def demo():
    sens_file_path = '/home/chli/chLi/ScanNet/scans/scene0000_01/scene0000_01.sens'
    sens_file_path = '/home/chli/scene0000_01.sens'
    header_only = True
    output_path = './tmp/'

    sens_reader = SensReader(sens_file_path, header_only)

    print('num_frames =', sens_reader.num_frames)

    return
    sens_reader.export_depth_images(output_path + 'depth/')
    sens_reader.export_color_images(output_path + 'color/')
    sens_reader.export_poses(output_path + 'pose/')
    sens_reader.export_intrinsics(output_path + 'intrinsic/')
    return True
