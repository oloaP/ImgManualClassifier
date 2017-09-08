#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   === This file is part of DocumentClassifier ===
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
"""
Entry point module
"""
import gettext
import sys

from PyQt5.QtWidgets import QApplication

from main_window import MainWindow


def main(args=None):
    gettext.install('imgClassifier')
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
