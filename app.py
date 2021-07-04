#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QGridLayout

 


# procedure ???

    

# def get_QColor_from_hex(colors): #-> QColor
#     return [[
#         QTableWidgetItem(name), 
#         QTableWidgetItem(code), 
#         QTableWidgetItem(),    
#         item_color.setBackground(colors)
#         ] 
#     for i, (name, code) in enumerate(colors)]



def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])


def create_table():
    colors = [("Red", "#FF0000"),
            ("Green", "#00FF00"),
            ("Blue", "#0000FF"),
            ("Black", "#000000"),
            ("White", "#FFFFFF"),
            ("Electric Green", "#41CD52"),
            ("Dark Blue", "#222840"),
            ("Yellow", "#F9E56d")]

    table = QTableWidget()
    table.setRowCount(len(colors))
    table.setColumnCount(len(colors[0]) + 1)
    table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])
    

    for i, (name, code) in enumerate(colors):
        item_name = QTableWidgetItem(name)
        item_code = QTableWidgetItem(code)
        item_color = QTableWidgetItem()
        item_color.setBackground(get_rgb_from_hex(code))
        table.setItem(i, 0, item_name)
        table.setItem(i, 1, item_code)
        table.setItem(i, 2, item_color)
    
    return table


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        mainLayout = QGridLayout()

        mainLayout.addWidget(create_table())

        self.setLayout(mainLayout)


def main():
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
