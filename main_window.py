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
from functools import partial
from os import path
from os import walk

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from binder import Binder


class MainWindow(QWidget):

    NB_IMG_CATEGORIES = 7

    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.buttons_layout = QVBoxLayout()
        self.open_folder_button = QPushButton(_("Open images folder"))
        self.image_widget = QLabel()
        self.image_dir = None
        self.img_queue = None
        self.current_img_path = None

        self.binder = Binder(self.NB_IMG_CATEGORIES)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(_('Image classifier'))
        self.buttons_layout.addWidget(self.open_folder_button)
        self.layout.addWidget(self.image_widget)
        self.layout.addLayout(self.buttons_layout)

        # Add Categories buttons
        for i in range(0, self.NB_IMG_CATEGORIES):
            button = QPushButton(str(i))
            button.shortcut = QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_1 + i), self)
            button.clicked.connect(partial(self.classify_image, i))
            button.shortcut.activated.connect(partial(self.classify_image, i))
            self.buttons_layout.addWidget(button)

        self.open_folder_button.clicked.connect(self.select_img_folder)

        self.setLayout(self.layout)
        self.showMaximized()
        self.show()

    def select_img_folder(self):
        self.image_dir = str(QFileDialog.getExistingDirectory(parent=None, caption=_('Select a folder:'),
                                                              options=QFileDialog.ShowDirsOnly))
        if self.image_dir:
            self.img_queue = self._walk_dir(self.image_dir)
            self.next_image()

    def classify_image(self, category):
        self.binder.classify(self.current_img_path, category)
        self.next_image()

    def next_image(self):
        self.current_img_path = next(self.img_queue)
        self.image_widget.setPixmap(QPixmap(self.current_img_path).scaled(
            self.image_widget.width(), self.image_widget.height(),
            Qt.KeepAspectRatio))

    @staticmethod
    def _walk_dir(dir_):
        for (dirpath, _, filenames) in walk(dir_):
            for filename in filenames:
                yield path.abspath(path.join(dirpath, filename))
