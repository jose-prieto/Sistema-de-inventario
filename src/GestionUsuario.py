from PyQt5.QtGui import QIcon

from general import ModuloListItem

from CrearUsuario import ModCrearUsuarioItem
from ModificarUsuario import ModModificarUsuarioItem
from EliminarUsuario import ModEliminarUsuarioItem
from EliminarDeuda import ModEliminarDeudaItem


class ModGestionUsuarioItem(ModuloListItem):
    ''' This represents the module GestionUsuario item on the QListWidget '''
    def __init__(self, buttonBack, listNotifications, *args):
        super(ModGestionUsuarioItem, self).__init__(*args)
        self.listNotifications = listNotifications
        self.buttonBack = buttonBack
        self.listMenu = args[2]
        self.iconMenu = args[0]

    def open_mod(self):
        self.listMenu.clear()

        ModCrearUsuarioItem(self.iconMenu,'Crear Usuario', self.listMenu)
        ModModificarUsuarioItem(self.iconMenu, 'Modificar Usuario', self.listMenu)
        ModEliminarUsuarioItem(self.iconMenu, 'Eliminar Usuario', self.listMenu)
        ModEliminarDeudaItem(self.iconMenu, 'Eliminar Deuda', self.listMenu)

        self.buttonBack.setEnabled(True)