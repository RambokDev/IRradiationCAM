import os
import sqlite3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from functools import partial
from numpy import array

cheminBDD = "dataBase/TP.db"


class tableData():

    def GetDataTable(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT cosh1,cosh2,cosh3,Tx FROM tableData WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()



        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute(
                "SELECT cosh1,cosh2,cosh3,Tx FROM tableData WHERE id_users = ? ",
                (user,))




            resultats2 = curseur2.fetchall()
            print(resultats2)

            line1 = list(resultats2[0])
            line2 = list(resultats2[1])
            line3 = list(resultats2[2])

            for i in range(len(line1)):
                line1[i] = str(line1[i])
                line2[i] = str(line2[i])
                line3[i] = str(line3[i])

            matrice = array([line1, line2, line3])

            # print(matrice)
            self.writeTableData(matrice)

            self.readBtn.clicked.connect(lambda: self.readTableData(user, resultats))
        else:
            print("ici2")
            self.readBtn.clicked.connect(lambda: self.readTableData(user, resultats))










    def writeTableData(self, matrice):

        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()
        print(rowCount)
        for row in range(rowCount):
            #     user = 2

            #     rowData.append(user)
            for column in range(columnCount):
                widgetItem = self.tableWidget.item(row, column)
                rowData = ['1']

                widgetItem.setText(matrice[row][column])


    def readTableData(self, user, resultats):
        print('ici')

        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()
        for row in range(rowCount):

            rowData = []
            rowData.append(user)

            rowData2 = []
            for column in range(columnCount):
                widgetItem = self.tableWidget.item(row, column)
                if (widgetItem and widgetItem.text):

                    # rowData = rowData + ' - '+ widgetItem.text()
                    rowData.append(widgetItem.text())
                    rowData2.append(widgetItem.text())

                else:
                    # rowData + ' - '+
                    rowData.append('NULL')
                    rowData2.append('NULL')
            # print(rowData +'\n')
            rowData2.append(user)
            # idLine = ["1", "2", "3"]
            # rowData2.append(idLine[0])

            # rowData2[i] = idLine[i]

            print(rowData2)

            self.onclickUpdateTable(rowData, rowData2, resultats, row,user)

    def onclickUpdateTable(self, rowData, rowData2, resultats, row,user):

        print(row)

        if len(resultats) != 0:
            # print('update')
            connexion4 = sqlite3.connect(cheminBDD)
            curseur4 = connexion4.cursor()

            print(rowData2)


            curseur4.execute(
                "SELECT id FROM tableData WHERE id_users = ? ",
                (user,))
            idd = curseur4.fetchall()
            print(idd)

            idLine = []
            for all in idd :
                idLine.append(all[0])

            print(idLine)




            if row == 0:
                id = idLine[0]
            elif row == 1:
                id = idLine[1]
            else:
                id = idLine[2]

            # curseur4.execute(
            #     "UPDATE tableData SET cosh1 = ? , cosh2 = ?, cosh3 = ? , Tx = ?   WHERE id_users = ? ",
            #     (rowData2))

            rowData2.append(id)

            upd = """UPDATE tableData SET cosh1 = ? , cosh2 = ?, cosh3 = ? , Tx = ?   WHERE id_users = ? AND id = ?  """
            curseur4.execute(upd, rowData2)
            connexion4.commit()  # enregistrement des modifications
            connexion4.close()
            print("update")


        else:
            print("insert")
            connexion2 = sqlite3.connect(cheminBDD)
            curseur2 = connexion2.cursor()

            queryInsert = """INSERT INTO tableData ( id_users, cosh1,cosh2,cosh3,Tx) VALUES (?, ?, ?, ?, ?) """
            # dataVariable = (user, text)
            curseur2.execute(queryInsert, rowData)

            connexion2.commit()  # enregistrement des modifications
            connexion2.close()
            print("update")
