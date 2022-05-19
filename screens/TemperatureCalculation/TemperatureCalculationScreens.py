import os
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

cheminBDD = "dataBase/TP.db"


class TemperatureCalculation:

    ##############################################################
    # Setup pour la video
    def setupVideo1TemperatureCalculation(self):

        self.mediaPlayer4 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.playButtonPage_11.clicked.connect(self.play_video4)
        self.stopbuttonPage_11.clicked.connect(self.stop_video4)
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        self.widgetVideoPage_11.setLayout(vboxLayout)
        self.mediaPlayer4.setVideoOutput(videowidget)
        path = os.getcwd()


        self.mediaPlayer4.setMedia(QMediaContent(
            QUrl.fromLocalFile('{}/screens/TemperatureCalculation/video1TemperatureCalculation.mp4'.format(path))))

    def play_video4(self):
        if self.mediaPlayer4.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer4.pause()
        else:

            self.mediaPlayer4.play()

    def stop_video4(self):
        self.mediaPlayer4.stop()

    ##############################################################
    # setup pour les textes
    def PlainTextTemperatureCalculation1(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute(
            "SELECT ContactTemperatureCalculation1_text1,ContactTemperatureCalculation1_text2,ContactTemperatureCalculation1_text3 FROM ContactTemperatureCalculation WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()


        if len(resultats) != 0 :
            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute(
                "SELECT ContactTemperatureCalculation1_text1,ContactTemperatureCalculation1_text2,ContactTemperatureCalculation1_text3 FROM ContactTemperatureCalculation WHERE id_users = ? ",
                (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage11.insertPlainText(resultats2[0])
            self.lineEditPage11_1.setText(resultats2[1])
            self.lineEditPage11_2.setText(resultats2[2])

            self.updateResponsePage11.clicked.connect(lambda : self.onClickedUpdatePlainTextTemperatureCalculation1(user))
        else:
            self.updateResponsePage11.clicked.connect(lambda : self.onClickedUpdatePlainTextTemperatureCalculation1(user))

    def onClickedUpdatePlainTextTemperatureCalculation1(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text1 = self.plainTextEditPage11.toPlainText()
        text2 = self.lineEditPage11_1.text()
        text3 = self.lineEditPage11_2.text()


        curseur.execute("SELECT ContactTemperatureCalculation1_text1,ContactTemperatureCalculation1_text2,"
                        "ContactTemperatureCalculation1_text3 FROM ContactTemperatureCalculation WHERE id_users = ? ",
                        (user,))
        resultats = curseur.fetchall()


        if len(resultats) != 0:

            curseur.execute(
                "UPDATE ContactTemperatureCalculation SET ContactTemperatureCalculation1_text1 = ? , ContactTemperatureCalculation1_text2 = ? , ContactTemperatureCalculation1_text3 = ?  WHERE id_users = ? ",
                (text1, text2, text3, user,))

        else:
            queryInsert = """INSERT INTO ContactTemperatureCalculation (id_users, ContactTemperatureCalculation1_text1,ContactTemperatureCalculation1_text2,ContactTemperatureCalculation1_text3) VALUES (?,?,?,?)"""
            dataVariable = (user, text1, text2, text3)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        print('update')
        self.updateLabelPage11.setText("Update")




    def PlainTextTemperatureCalculation2(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute(
            "SELECT ContactTemperatureCalculation2_text1,ContactTemperatureCalculation2_text2 FROM ContactTemperatureCalculation WHERE id_users = ? ",
            (user,))


        resultats = curseur.fetchall()

        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute(
                "SELECT ContactTemperatureCalculation2_text1,ContactTemperatureCalculation2_text2 FROM ContactTemperatureCalculation WHERE id_users = ? ",
                (user,))

            resultats2 = curseur2.fetchone()


            self.lineEditPage12_1.setText(resultats2[0])
            self.lineEditPage12_2.setText(resultats2[1])
            self.updateResponsePage12.clicked.connect(lambda : self.onClickedUpdatePlainTextTemperatureCalculation2(user))
        else:

            self.updateResponsePage12.clicked.connect(lambda : self.onClickedUpdatePlainTextTemperatureCalculation2(user))

    def onClickedUpdatePlainTextTemperatureCalculation2(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()

        text1 = self.lineEditPage12_1.text()
        text2 = self.lineEditPage12_2.text()
        # print(text1, text2)

        curseur.execute(
            "SELECT ContactTemperatureCalculation2_text1,ContactTemperatureCalculation2_text2 FROM ContactTemperatureCalculation WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:
            curseur.execute(
                "UPDATE ContactTemperatureCalculation SET ContactTemperatureCalculation2_text1 = ? , ContactTemperatureCalculation2_text2 = ?  WHERE id_users = ? ",
                (text1, text2, user,))
        else:
            queryInsert = """INSERT INTO ContactTemperatureCalculation (id_users, ContactTemperatureCalculation2_text1,ContactTemperatureCalculation2_text2) VALUES (?,?,?)"""
            dataVariable = (user, text1, text2)
            curseur.execute(queryInsert, dataVariable)


        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage12.setText("Update")
        print('update')



