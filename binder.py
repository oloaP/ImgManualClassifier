#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   === This file is part of ImgClassifier ===
#
#   Copyright 2017, Paolo de Vathaire <paolo.devathaire@gmail.com>
#
#   ImgClassifier is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   ImgClassifier is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with ImgClassifier. If not, see <http://www.gnu.org/licenses/>.
#
import ntpath
import os
import tempfile

import shutil


class Binder(object):
    def __init__(self, nb_tabs: int):
        self.binder_dict = {x: list() for x in range(0, nb_tabs)}
        self.history = []

    def classify(self, obj, category):
        self.binder_dict[category].append(obj)
        self.history.append((category, obj))

    def remove_last(self):
        category, obj = self.history.pop()
        self.binder_dict[category].remove(obj)
        return category, obj


class FileBinder(Binder):
    def to_archive(self, dest_path):
        # Create the file tree view for the archive in temp dir
        dirpath = tempfile.mkdtemp()
        for cat, file_paths in self.binder_dict.items():
            cat_folder_path = os.path.join(dirpath, str(cat))
            os.makedirs(cat_folder_path)
            for fpath in file_paths:
                shutil.copyfile(fpath, os.path.join(cat_folder_path, ntpath.basename(fpath)))
        shutil.make_archive(dest_path, 'zip', dirpath)
        shutil.rmtree(dirpath)
