from PyQt5.QtGui import QIcon

from general import ModuloListItem

from AgregarProducto import ModAgregarItem
from ModificarProducto import ModModificarItem
from EliminarProducto import ModEliminarItem

class ModGestionProductoItem(ModuloListItem):
    ''' This represents the module GestionProducto item on the QListWidget '''
    def __init__(self, buttonBack, listNotifications, *args):
        super(ModGestionProductoItem, self).__init__(*args)
        self.listNotifications = listNotifications
        self.buttonBack = buttonBack
        self.listMenu = args[2]
        self.iconMenu = args[0]

    def open_mod(self):
        self.listMenu.clear()

        ModAgregarItem(self.iconMenu, 'Agregar Producto', self.listMenu)
        ModModificarItem(self.listNotifications, self.iconMenu, 'Modificar Producto', self.listMenu)
        ModEliminarItem(self.iconMenu, 'Eliminar Producto', self.listMenu)

        self.buttonBack.setEnabled(True)