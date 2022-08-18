#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def removeIfExist(file_path):
    if not os.path.exists(file_path):
        return True
    os.remove(file_path)
    return True

