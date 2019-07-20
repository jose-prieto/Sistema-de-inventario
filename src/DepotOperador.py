import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

from AgregarProducto import ModAgregarItem
from GestionPrestamo import ModGestionPrestamoItem
from Consultas import ModConsultasItem
from Notifications import NotificationList

class Depot(QMainWindow):
    ''' Main window '''
    
    def __init__(self, *args):
        super(Depot, self).__init__(*args)
        loadUi('../gui/mainwindow.ui', self)
        self.setWindowTitle("Depot")
        self.statusBar.showMessage('XSingularity')

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.setLists()
        iconBack = QIcon('../gui/images/back_arrow.svg')
        self.buttonBack.setIcon(iconBack)
        self.buttonBack.setEnabled(False)

        # load notifications
        notifications = NotificationList(self.listNotifications)
        notifications.update_list()

    def setLists(self):
        ''' Setting lists '''
        self.listNotifications.setSelectionMode(0)
        self.listNotifications.itemActivated.connect(self.noti_selected)
        self.listMenu.itemActivated.connect(self.mod_selected)

        iconMenu = QIcon('../gui/images/list.svg')

        ModAgregarItem(iconMenu, 'Agregar Producto', self.listMenu)
        ModGestionPrestamoItem(self.buttonBack, self.listNotifications, iconMenu, 'Gestion de Prestamos', self.listMenu)
        ModConsultasItem(iconMenu, 'Consultas', self.listMenu)

    def noti_selected(self):
        ''' When a notification is selected '''
        self.listNotifications.currentItem().open_noti()

    def mod_selected(self):
        ''' When a module is selected '''
        self.listMenu.currentItem().open_mod()

    @pyqtSlot()
    def on_buttonBack_clicked(self):
        self.listMenu.clear()
        iconMenu = QIcon('../gui/images/list.svg')

        ModAgregarItem(iconMenu, 'Agregar Producto', self.listMenu)
        ModGestionPrestamoItem(self.buttonBack, self.listNotifications, iconMenu, 'Gestion de Prestamos', self.listMenu)
        ModConsultasItem(iconMenu, 'Consultas', self.listMenu)

        self.buttonBack.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Depot()
    controller.show()
    sys.exit(app.exec_())
