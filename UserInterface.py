import blocker
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QTableWidgetItem

class alertPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        loadUi("ui/alertPopup.ui", self)
        self.btn_alert.accepted.connect(self.alertAccept)
        self.btn_alert.rejected.connect(self.alertRejected)

    def alertAccept(self):
        self.close()
        start()

    def alertRejected(self):
        self.close()






class HomeWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        loadUi("ui/home.ui", self)
        self.btn_blockedHistory.clicked.connect(self.goBlockedWindow)



    def goBlockedWindow(self):
        win = BlockedSitesWindow()
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)




class BlockedSitesWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        loadUi("ui/blockedhistory.ui", self)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(0, 638)
        self.loaditems()
        self.btn_home.clicked.connect(self.goHomeWindow)
        self.btn_add.clicked.connect(self.addItem)
        self.btn_delete.clicked.connect(self.removeItem)


    def loaditems(self):
        blocked_sites = blocker.blocked_IPS()
        row=0
        self.tableWidget.setRowCount(len(blocked_sites))

        for site in blocked_sites.keys():
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(site))
            row += 1


    def addItem(self):
        value = self.blockSiteTextBox.toPlainText()
        if value:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, QTableWidgetItem(value))
            blocker.add_block(value)
        else:
            print("Enter non-empty address")

        self.blockSiteTextBox.clear()

    def removeItem(self):
        if self.tableWidget.rowCount() > 0:
            hostname = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            blocker.delete_block(hostname)
            self.tableWidget.removeRow(self.tableWidget.currentRow())



    def goHomeWindow(self):
        win = HomeWindow()
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()-1)







def confirmStart():
    global widget
    widget = QStackedWidget()
    alertWin = alertPopup()
    alertWin.show()
    try:
        sys.exit(app.exec_())
    except:
        print("exiting")

def start():
    blocker.close_browsers()

    homeWin = HomeWindow()
    widget.addWidget(homeWin)

    widget.resize(800, 500)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("exiting")

app = QApplication(sys.argv)
