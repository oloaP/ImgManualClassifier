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

from PyQt5.QtWidgets import QHBoxLayout, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.buttons_layout = QVBoxLayout()
        self.open_folder_button = QPushButton(_("Open images folder"))
        self.image_widget = QLabel()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(_('Image classifier'))
        self.buttons_layout.addWidget(self.open_folder_button)
        self.layout.addWidget(self.image_widget)
        self.layout.addLayout(self.buttons_layout)

        self.setLayout(self.layout)
        self.showMaximized()
        self.show()

