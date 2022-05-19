import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
import re


from screens.SurfaceObservation.SurfaceObservationsScreens import *
from screens.TemperatureCalculation.TemperatureCalculationScreens import *
from screens.ThermalApproach.ThermalApproachScreens import *
from screens.ScreensManager.manager import *
from screens.HeatTransfer.HeatTransferScreen import *
from screens.TableData.TableDataScreen import *
from screens.Conclusion.ConclusionScreen import *

import sqlite3

cheminBDD = "dataBase/TP.db"


class MainWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(int, str, str,str,str)

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('UI/mainPage.ui', self)
        self.setWindowTitle("Connexion IR TP")
        self.quitButtonConnectForm.clicked.connect(self.closeApp)
        self.connexionButton.clicked.connect(self.connexion)
        self.validGroupButton.clicked.connect(self.userInfoComboBox)


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT * FROM users")
        resultats = curseur.fetchall()
        print(resultats)

        if len(resultats) != 0:
            listgroupMain = []
            for all in resultats :
                listgroupMain.append(all[1])

            print(listgroupMain)

            self.comboBoxGroup.addItems(listgroupMain)

            connexion.commit()
            connexion.close()






    def userInfoComboBox(self):
        self.errorLabel.setStyleSheet("color: red")
        Groupe = self.comboBoxGroup.currentText()
        if Groupe == "Groupe":
            self.errorLabel.setText("Choisissez un groupe ")
        else:
            self.errorLabel.setText("")


            connexion = sqlite3.connect(cheminBDD)
            curseur = connexion.cursor()  # Récupération d'un curseur
            curseur.execute("SELECT * FROM users WHERE GroupeName = ? ",(Groupe,))
            resultats = curseur.fetchall()

            # print(resultats)

            listDataComboBox = []
            for all in resultats :
                listDataComboBox.append(all[1])
                listDataComboBox.append(all[2])
                listDataComboBox.append(all[3])
                listDataComboBox.append(all[4])


            # print(listDataComboBox)



            Groupe = self.lineEditNomGroupe.setText(listDataComboBox[0])
            Mail1 = self.lineEditMail1.setText(listDataComboBox[1])
            Mail2 = self.lineEditMail2.setText(listDataComboBox[2])
            Mail3 = self.lineEditMail3.setText(listDataComboBox[3])





    def closeApp(self):
        QApplication.quit()

    def connexion(self):
        Groupe = self.lineEditNomGroupe.text()
        Mail1 = self.lineEditMail1.text()
        Mail2 = self.lineEditMail2.text()
        Mail3 = self.lineEditMail3.text()

        self.errorLabel.setStyleSheet("color: red")

        vide = ''
        if Groupe and Mail1 and Mail2 and Mail3 != vide:
            regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
            verifMail1 = re.match(regex, Mail1)
            verifMail2 = re.match(regex, Mail2)
            verifMail3 = re.match(regex, Mail3)

            if (verifMail1 and verifMail2 and verifMail3 != None):


                connexion = sqlite3.connect(cheminBDD)
                curseur = connexion.cursor()  # Récupération d'un curseur
                curseur.execute("SELECT COUNT(*) FROM users WHERE GroupeName =?  AND mail_users1=? AND mail_users2=? and mail_users3=? ",
                                (Groupe, Mail1, Mail2,Mail3))
                L = curseur.fetchall()
                C = L[0]

                if C[0] == 1:
                    curseur.execute("SELECT id_users FROM users WHERE GroupeName =?  ", (Groupe,))
                    id = curseur.fetchone()
                    id_user = id[0]
                    connexion.commit()
                    connexion.close()

                    self.errorLabel.setText("")
                    self.switch_window.emit(id_user,Groupe,Mail1,Mail2,Mail3)
                else:
                    insertUsers = "INSERT INTO users ( GroupeName, mail_users1,mail_users2,mail_users3) VALUES (?,?,?,?) "
                    dataVariable = (Groupe, Mail1,Mail2,Mail3)
                    curseur.execute(insertUsers, dataVariable)
                    connexion.commit()
                    connexion.close()
                    self.errorLabel.setText("Inscription OK \n(cliquez à nouveau sur connexion pour lancer l'app ) ")

                    print("user created")


            else:
                self.errorLabel.setText("Email pas valid ")
                print("mail pas valid")


        else:
            self.errorLabel.setText("Remplissez tous les champs !")
            print("remplissez tous les champs svp")

        # self.switch_window.emit()


class WindowTwo(QMainWindow,managerApp,TemperatureCalculation,SurfaceObservation,ThermalApproach,HeatTransfer,tableData,Conslusion):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, id_user, Groupe ,Mail1, Mail2,Mail3, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('UI/main.ui', self)

        self.setWindowTitle("IR TP")
        self.QuitButton.clicked.connect(self.close)

        # pour la gestion des pages
        self.managerPagesApp()
        self.indexbtn()


        #Pour la page d'acceuil
        self.GroupLabelPageA1.setText("Nom du Groupe : {}".format(Groupe))
        self.GroupLabelPageA2.setText("Email 1 : {}".format(Mail1))
        self.GroupLabelPageA3.setText("Email 2 : {}".format(Mail2))
        self.GroupLabelPageA4.setText("Email 3 : {}".format(Mail3))






        # Pour les videos
        #-------Surface Observation ------------
        self.setupVideo1SurfaceObservation()
        self.setupVideo2SurfaceObservation()
        self.setupVideo3SurfaceObservation()
        #-------Temperature Calculation ------------
        self.setupVideo1TemperatureCalculation()
        #-------Thermal Approach ------------
        self.setupVideo1ThermalApproach()
        self.setupVideo2ThermalApproach()
        #-------heat Transfer ------------
        self.setupVideo1HeatTransfer()



        # Pour les  Text
        #-------Surface Observation ------------
        self.PlainTextSurfaceObservation1_text1(id_user)
        self.PlainTextSurfaceObservation2_text1(id_user)
        self.PlainTextSurfaceObservation3_text1(id_user)
        # # #-------Temperature Calculation ------------
        self.PlainTextTemperatureCalculation1(id_user)
        self.PlainTextTemperatureCalculation2(id_user)
        # # #-------Thermal Approach ------------
        self.PlainTextThermalApproach1(id_user)
        self.PlainTextThermalApproach2(id_user)
        self.RadioButtonOnclickedThermalApproach3(id_user)
        self.GetDataThermalApproach4(id_user)
        # #-------heat Transfer ------------
        self.PlainTextHeatTransfer1_text1(id_user)
        self.PlainTextHeatTransfer2_text1(id_user)
        self.PlainTextHeatTransfer3_text1(id_user)
        self.PlainTextHeatTransfer4(id_user)



        self.GetDataTable(id_user)
        self.OpenFile(id_user)
        self.PlainTextConclusion(id_user)


    def close(self):
        QApplication.closeAllWindows()
        self.switch_window.emit()






class Ui:

    def __init__(self):
        pass



    def show_main(self):
        self.window1 = MainWindow()

        self.window1.switch_window.connect(self.show_window_two)

        self.window1.show()

    def show_window_two(self, id_user, Groupe, Mail1,Mail2,Mail3):
        self.window2 = WindowTwo(id_user, Groupe,Mail1,Mail2,Mail3)
        self.window2.switch_window.connect(self.show_main)

        self.window1.close()
        self.window2.show()


def main():
    app = QApplication(sys.argv)
    window = Ui()
    window.show_main()
    sys.exit(app.exec_())
    # app.exec_()


if __name__ == '__main__':
    main()
