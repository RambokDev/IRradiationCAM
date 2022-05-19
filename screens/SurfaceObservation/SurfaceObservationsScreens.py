import os
import sqlite3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from functools import partial

cheminBDD = "dataBase/TP.db"


class SurfaceObservation:

    ##############################################################
    # Setup pour la video
    def setupVideo1SurfaceObservation(self):

        self.mediaPlayer1 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.playButtonPage_8.clicked.connect(self.play_video1)
        self.stopbuttonPage_8.clicked.connect(self.stop_video1)
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        self.widgetVideoPage_8.setLayout(vboxLayout)
        self.mediaPlayer1.setVideoOutput(videowidget)
        path = os.getcwd()

        self.mediaPlayer1.setMedia(QMediaContent(
            QUrl.fromLocalFile('{}/screens/SurfaceObservation/video1SurfaceObservation.mp4'.format(path))))

    def setupVideo2SurfaceObservation(self):

        self.mediaPlayer2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.playButtonPage_9.clicked.connect(self.play_video2)
        self.stopbuttonPage_9.clicked.connect(self.stop_video2)
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        self.widgetVideoPage_9.setLayout(vboxLayout)
        self.mediaPlayer2.setVideoOutput(videowidget)
        path = os.getcwd()

        self.mediaPlayer2.setMedia(QMediaContent(
            QUrl.fromLocalFile('{}/screens/SurfaceObservation/video2SurfaceObservation.mp4'.format(path))))

    def setupVideo3SurfaceObservation(self):

        self.mediaPlayer3 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.playButtonPage_10.clicked.connect(self.play_video3)
        self.stopbuttonPage_10.clicked.connect(self.stop_video3)
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        self.widgetVideoPage_10.setLayout(vboxLayout)
        self.mediaPlayer3.setVideoOutput(videowidget)
        path = os.getcwd()

        self.mediaPlayer3.setMedia(QMediaContent(
            QUrl.fromLocalFile('{}/screens/SurfaceObservation/video3SurfaceObservation.mp4'.format(path))))

    def play_video1(self):
        # print('sO : ',self.pmAPP.index)
        if self.mediaPlayer1.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer1.pause()
        else:
            self.mediaPlayer1.play()

    def stop_video1(self):
        self.mediaPlayer1.stop()

    def play_video2(self):
        if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer2.pause()
        else:
            self.mediaPlayer2.play()

    def stop_video2(self):
        self.mediaPlayer2.stop()

    def play_video3(self):
        if self.mediaPlayer3.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer3.pause()
        else:
            self.mediaPlayer3.play()

    def stop_video3(self):
        self.mediaPlayer3.stop()

    ##############################################################
    # pour les plains text

    def PlainTextSurfaceObservation1_text1(self, user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT SurfaceObservation1_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()
        # print(resultats)

        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute("SELECT SurfaceObservation1_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage8.insertPlainText(resultats2[0])
            self.updateResponsePage8.clicked.connect(lambda: self.onClickedUpdateSurfaceObservation1(user))
            connexion.close()
        else:
            self.updateResponsePage8.clicked.connect(lambda: self.onClickedUpdateSurfaceObservation1(user))
            connexion.close()

    def onClickedUpdateSurfaceObservation1(self, user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text = self.plainTextEditPage8.toPlainText()

        curseur.execute("SELECT SurfaceObservation1_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()
        if len(resultats) != 0:
            curseur.execute("UPDATE surfaceObservation SET SurfaceObservation1_text1 = ? WHERE id_users = ? ",
                            (text, user,))

        else:
            queryInsert = """INSERT INTO surfaceObservation (id_users, SurfaceObservation1_text1) VALUES (?,?)"""
            dataVariable = (user, text)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage8.setText("Update")
        print("update")

    def PlainTextSurfaceObservation2_text1(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT SurfaceObservation2_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:
            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute("SELECT SurfaceObservation2_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage9.insertPlainText(resultats2[0])
            self.updateResponsePage9.clicked.connect(lambda : self.onClickedUpdateSurfaceObservation2(user))
        else:
            self.updateResponsePage9.clicked.connect(lambda : self.onClickedUpdateSurfaceObservation2(user))

    def onClickedUpdateSurfaceObservation2(self,user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text = self.plainTextEditPage9.toPlainText()

        curseur.execute("SELECT SurfaceObservation2_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))
        resultats = curseur.fetchall()
        if len(resultats) != 0:
            curseur.execute("UPDATE surfaceObservation SET SurfaceObservation2_text1 = ? WHERE id_users = ? ",
                            (text, user,))
        else:
            queryInsert = """INSERT INTO surfaceObservation (id_users, SurfaceObservation2_text1) VALUES (?,?)"""
            dataVariable = (user, text)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage9.setText("Update")
        print("update")

    def PlainTextSurfaceObservation3_text1(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT SurfaceObservation3_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute("SELECT SurfaceObservation3_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage10.insertPlainText(resultats2[0])
            self.updateResponsePage10.clicked.connect(lambda: self.onClickedUpdateSurfaceObservation3(user))
        else:

            self.updateResponsePage10.clicked.connect(lambda: self.onClickedUpdateSurfaceObservation3(user))

    def onClickedUpdateSurfaceObservation3(self, user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text = self.plainTextEditPage10.toPlainText()

        curseur.execute("SELECT SurfaceObservation3_text1 FROM surfaceObservation WHERE id_users = ? ", (user,))
        resultats = curseur.fetchall()
        if len(resultats) != 0:
            curseur.execute("UPDATE surfaceObservation SET SurfaceObservation3_text1 = ? WHERE id_users = ? ",
                            (text, user,))
        else:
            queryInsert = """INSERT INTO surfaceObservation (id_users, SurfaceObservation3_text1) VALUES (?,?)"""
            dataVariable = (user, text)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage10.setText("Update")
        print("update")
