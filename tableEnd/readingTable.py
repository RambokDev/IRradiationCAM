from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os.path
import sqlite3


class Ui_MainWindow(QtWidgets.QMainWindow):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR, "tableau.ui")
    db_path = os.path.join(BASE_DIR, "donnees.db")
    dbConnection = ''

    def initDBConnection(self):
        self.dbConnection = sqlite3.connect(self.db_path)
        self.prepareDBTables()

    def prepareDBTables(self):
        query = """ CREATE TABLE IF NOT EXISTS "tab" (
                        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                        "id_users" INTEGER,
                        "cosh1"    float,
                        "cosh2"    float,
                        "cosh3"    float,
                        "Tx"    float
                        ); """
        result = self.dbConnection.execute(query)
        self.dbConnection.commit()

    def insertRowInDB(self, rowData):


        id_user = 1
        p = tuple(rowData)
        # print(p)
        queryStr = """INSERT INTO tab ( id_users, cosh1,cosh2,cosh3,Tx) VALUES (?, ?, ?, ?, ?) """
        #
        self.dbConnection.execute(queryStr, rowData)
        self.dbConnection.commit()

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        uic.loadUi(self.UI_FILE, self)
        self.readBtn.clicked.connect(self.readTableData)
        self.initDBConnection()

    def readTableData(self):
        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()
        for row in range(rowCount):
            user = 1
            rowData = []
            rowData.append(user)
            for column in range(columnCount):
                widgetItem = self.tableWidget.item(row, column)
                if (widgetItem and widgetItem.text):


                    # rowData = rowData + ' - '+ widgetItem.text()
                    rowData.append(widgetItem.text())
                else:
                    # rowData + ' - '+
                    rowData.append('NULL')
            # print(rowData +'\n')
            print(rowData)

            self.insertRowInDB(rowData)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
