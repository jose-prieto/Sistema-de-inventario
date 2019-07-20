from PyQt5.QtGui import QIcon

from general import ModuloListItem

from DevolucionProducto import ModDevolucionItem
from RetiroProducto import ModRetiroItem

class ModGestionPrestamoItem(ModuloListItem):
    ''' This represents the module GestionPrestamo item on the QListWidget '''
    def __init__(self, buttonBack, listNotifications, *args):
        super(ModGestionPrestamoItem, self).__init__(*args)
        self.listNotifications = listNotifications
        self.buttonBack = buttonBack
        self.listMenu = args[2]
        self.iconMenu = args[0]

    def open_mod(self):
        self.listMenu.clear()

        ModRetiroItem(self.listNotifications, self.iconMenu, 'Retiro de Producto', self.listMenu)
        ModDevolucionItem(self.listNotifications, self.iconMenu, 'Devolucion de Producto', self.listMenu)

        self.buttonBack.setEnabled(True)