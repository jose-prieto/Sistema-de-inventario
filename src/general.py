from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QIcon

class ModuloListItem(QListWidgetItem):
    ''' A list item for the menu with extra configs '''
    def __init__(self, *args):
        super(ModuloListItem, self).__init__(*args)
        self.setSizeHint(QSize(50, 50))
        self.setTextAlignment(Qt.AlignCenter)