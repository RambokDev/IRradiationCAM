import os
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

cheminBDD = "dataBase/TP.db"


class ThermalApproach:

    ##############################################################
    # Setup pour la video
    def setupVideo1ThermalApproach(self):

        self.mediaPlayer5 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.playButtonPage_13.clicked.connect(self.play_video5)
        self.stopbuttonPage_13.clicked.connect(self.stop_video5)
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        self.widgetVideoPage_13.setLayout(vboxLayout)
        self.mediaPlayer5.setVideoOutput(videowidget)
        path = os.getcwd()

        self.mediaPlayer5.setMedia(QMediaContent(
            QUrl.fromLocalFile('{}/screens/ThermalApproach/video1ThermalApproach.mp4'.format(path))))

    def play_video5(self):
        if self.mediaPlayer5.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer5.pause()
        else:

            self.mediaPlayer5.play()

    def stop_video5(self):
        self.mediaPlayer5.stop()

    def setupVideo2ThermalApproach(self):

        self.mediaPlayer6 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.playButtonPage_15.clicked.connect(self.play_video6)
        self.stopbuttonPage_15.clicked.connect(self.stop_video6)
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        self.widgetVideoPage_15.setLayout(vboxLayout)
        self.mediaPlayer6.setVideoOutput(videowidget)
        path = os.getcwd()

        self.mediaPlayer6.setMedia(QMediaContent(
            QUrl.fromLocalFile('{}/screens/ThermalApproach/video2ThermalApproach.mp4'.format(path))))

    def play_video6(self):
        if self.mediaPlayer6.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer6.pause()
        else:
            self.mediaPlayer6.play()

    def stop_video6(self):
        self.mediaPlayer6.stop()

    ##############################################################
    # setup pour les textes
    def PlainTextThermalApproach1(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute(
            "SELECT ThermalApproachOfElectricPhenomena1_text1 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute(
                "SELECT ThermalApproachOfElectricPhenomena1_text1 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
                (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage13.insertPlainText(resultats2[0])
            self.updateResponsePage13.clicked.connect(lambda : self.onClickedUpdatePlainTextThermalApproach1(user))
        else:
            self.updateResponsePage13.clicked.connect(lambda : self.onClickedUpdatePlainTextThermalApproach1(user))

    def onClickedUpdatePlainTextThermalApproach1(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text1 = self.plainTextEditPage13.toPlainText()

        curseur.execute(
            "SELECT ThermalApproachOfElectricPhenomena1_text1 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:

            curseur.execute(
                "UPDATE ThermalApproachOfElectricPhenomena SET ThermalApproachOfElectricPhenomena1_text1 = ?   WHERE id_users = ? ",
                (text1, user,))

        else:
            queryInsert = """INSERT INTO ThermalApproachOfElectricPhenomena (id_users, ThermalApproachOfElectricPhenomena1_text1) VALUES (?,?)"""
            dataVariable = (user, text1)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage13.setText("Update")
        print("update")

    # setup pour les textes
    def PlainTextThermalApproach2(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute(
            "SELECT ThermalApproachOfElectricPhenomena2_text1,ThermalApproachOfElectricPhenomena2_text2,ThermalApproachOfElectricPhenomena2_text3 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:
            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute(
                "SELECT ThermalApproachOfElectricPhenomena2_text1,ThermalApproachOfElectricPhenomena2_text2,ThermalApproachOfElectricPhenomena2_text3 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
                (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage14.insertPlainText(resultats2[0])
            self.lineEditPage14_1.setText(resultats2[1])
            self.lineEditPage14_2.setText(resultats2[2])
            self.updateResponsePage14.clicked.connect(lambda : self.onClickedUpdatePlainTextThermalApproach2(user))
        else:
            self.updateResponsePage14.clicked.connect(lambda  : self.onClickedUpdatePlainTextThermalApproach2(user))

    def onClickedUpdatePlainTextThermalApproach2(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text1 = self.plainTextEditPage14.toPlainText()
        text2 = self.lineEditPage14_1.text()
        text3 = self.lineEditPage14_2.text()


        curseur.execute("SELECT ThermalApproachOfElectricPhenomena2_text1,ThermalApproachOfElectricPhenomena2_text2,"
                        "ThermalApproachOfElectricPhenomena2_text3 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
                        (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:

            curseur.execute(
                "UPDATE ThermalApproachOfElectricPhenomena SET ThermalApproachOfElectricPhenomena2_text1 = ? , ThermalApproachOfElectricPhenomena2_text2 = ? , ThermalApproachOfElectricPhenomena2_text3 = ?  WHERE id_users = ? ",
                (text1, text2, text3, user,))

        else:

            queryInsert = """INSERT INTO ThermalApproachOfElectricPhenomena (id_users, ThermalApproachOfElectricPhenomena2_text1,ThermalApproachOfElectricPhenomena2_text2,ThermalApproachOfElectricPhenomena2_text3) VALUES (?,?,?,?)"""
            dataVariable = (user, text1, text2, text3)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage14.setText("Update")
        print("update")

    def RadioButtonOnclickedThermalApproach3(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute(
            "SELECT ThermalApproachOfElectricPhenomena3_radioB FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:
            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute(
                "SELECT ThermalApproachOfElectricPhenomena3_radioB FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
                (user,))
            resultats2 = curseur2.fetchone()

            self.RadioButtonPage15Answer.setText("Your Answer : {}".format(resultats2[0]))
            if resultats2[0] == "Series":
                self.radioButtonPage15_1.setChecked(True)
            else:
                self.radioButtonPage15_2.setChecked(True)

            self.updateResponsePage15.clicked.connect(lambda : self.onClickedUpdateRadioTextThermalApproach3(user))
        else:
            self.updateResponsePage15.clicked.connect(lambda : self.onClickedUpdateRadioTextThermalApproach3(user))

    def onClickedUpdateRadioTextThermalApproach3(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        # self.radioButtonPage15_1.setChecked(True)
        if self.radioButtonPage15_1.isChecked() == True:

            AnswerRadioPage15 = "Series"
            self.RadioButtonPage15Answer.setText("Your Answer : {}".format(AnswerRadioPage15))
            curseur.execute(
                "UPDATE ThermalApproachOfElectricPhenomena SET ThermalApproachOfElectricPhenomena3_radioB = ?   WHERE id_users = ? ",
                (AnswerRadioPage15, user,))

        else:

            AnswerRadioPage15 = "Parallel"
            self.RadioButtonPage15Answer.setText("Your Answer : {}".format(AnswerRadioPage15))
            curseur.execute(
                "UPDATE ThermalApproachOfElectricPhenomena SET ThermalApproachOfElectricPhenomena3_radioB = ?   WHERE id_users = ? ",
                (AnswerRadioPage15, user,))

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        print("update")

    def GetDataThermalApproach4(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute(
            "SELECT ThermalApproachOfElectricPhenomena4_list1,ThermalApproachOfElectricPhenomena4_list2,ThermalApproachOfElectricPhenomena4_list3,ThermalApproachOfElectricPhenomena4_text1 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()


        if len(resultats) != 0:
            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute(
                "SELECT ThermalApproachOfElectricPhenomena4_list1,ThermalApproachOfElectricPhenomena4_list2,ThermalApproachOfElectricPhenomena4_list3,ThermalApproachOfElectricPhenomena4_text1 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
                (user,))
            resultats2 = curseur2.fetchone()
            self.comboBox.setCurrentText(resultats2[0])
            self.comboBox_2.setCurrentText(resultats2[1])
            self.comboBox_3.setCurrentText(resultats2[2])
            self.plainTextEditPage16.insertPlainText(resultats2[3])
            self.updateResponsePage16.clicked.connect(lambda : self.OnClikedUpdateGetDataThermalApproach4(user))

        else:
            self.updateResponsePage16.clicked.connect(lambda : self.OnClikedUpdateGetDataThermalApproach4(user))

    def OnClikedUpdateGetDataThermalApproach4(self,user):
        List1 = self.comboBox.currentText()
        List2 = self.comboBox_2.currentText()
        List3 = self.comboBox_3.currentText()
        Text = self.plainTextEditPage16.toPlainText()


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()

        curseur.execute(
            "SELECT ThermalApproachOfElectricPhenomena4_list1,ThermalApproachOfElectricPhenomena4_list2,ThermalApproachOfElectricPhenomena4_list3,ThermalApproachOfElectricPhenomena4_text1 FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()


        if len(resultats) != 0:

            curseur.execute(
                "UPDATE ThermalApproachOfElectricPhenomena SET ThermalApproachOfElectricPhenomena4_list1 = ? , ThermalApproachOfElectricPhenomena4_list2 = ? , ThermalApproachOfElectricPhenomena4_list3 = ?, ThermalApproachOfElectricPhenomena4_text1=?  WHERE id_users = ? ",
                (List1, List2, List3, Text, user,))
        else:

            queryInsert = """INSERT INTO ThermalApproachOfElectricPhenomena (id_users, ThermalApproachOfElectricPhenomena4_list1,ThermalApproachOfElectricPhenomena4_list2,ThermalApproachOfElectricPhenomena4_list3,ThermalApproachOfElectricPhenomena4_text1) VALUES (?,?,?,?,?)"""
            dataVariable = (user, List1, List2, List3, Text)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage16.setText("Update")
        print("update")
