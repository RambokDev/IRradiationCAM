import os
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

cheminBDD = "dataBase/TP.db"


class HeatTransfer:

    def setupVideo1HeatTransfer(self):

        self.mediaPlayer7 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.playButtonPage_17.clicked.connect(self.play_video7)
        self.stopbuttonPage_17.clicked.connect(self.stop_video7)
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        self.widgetVideoPage_17.setLayout(vboxLayout)
        self.mediaPlayer7.setVideoOutput(videowidget)
        path = os.getcwd()

        self.mediaPlayer7.setMedia(QMediaContent(
            QUrl.fromLocalFile('{}/screens/HeatTransfer/video1HeatTransfer.mp4'.format(path))))

    def play_video7(self):
        if self.mediaPlayer7.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer7.pause()
        else:
            self.mediaPlayer7.play()

    def stop_video7(self):
        self.mediaPlayer7.stop()




    ##############################################################
    # setup pour les textes




    def PlainTextHeatTransfer1_text1(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT HeatTransferInFins1_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()



        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute("SELECT HeatTransferInFins1_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage17.insertPlainText(resultats2[0])
            self.updateResponsePage17.clicked.connect(lambda : self.onClickedUpdateTextHeatTransfer1(user))

        else:
            self.updateResponsePage17.clicked.connect(lambda : self.onClickedUpdateTextHeatTransfer1(user))


    def onClickedUpdateTextHeatTransfer1(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text = self.plainTextEditPage17.toPlainText()

        curseur.execute("SELECT HeatTransferInFins1_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()
        if len(resultats) != 0:
            curseur.execute("UPDATE HeatTransferInFins SET HeatTransferInFins1_text1 = ? WHERE id_users = ? ",
                            (text, user,))

        else:
            queryInsert = """INSERT INTO HeatTransferInFins (id_users, HeatTransferInFins1_text1) VALUES (?,?)"""
            dataVariable = (user, text)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage17.setText("Update")

        print("update")






    def PlainTextHeatTransfer2_text1(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT HeatTransferInFins2_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()



        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute("SELECT HeatTransferInFins2_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage18.insertPlainText(resultats2[0])
            self.updateResponsePage18.clicked.connect(lambda : self.onClickedUpdateTextHeatTransfer2(user))

        else:
            self.updateResponsePage18.clicked.connect(lambda : self.onClickedUpdateTextHeatTransfer2(user))


    def onClickedUpdateTextHeatTransfer2(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text = self.plainTextEditPage18.toPlainText()

        curseur.execute("SELECT HeatTransferInFins2_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()
        if len(resultats) != 0:
            curseur.execute("UPDATE HeatTransferInFins SET HeatTransferInFins2_text1 = ? WHERE id_users = ? ",
                            (text, user,))

        else:
            queryInsert = """INSERT INTO HeatTransferInFins (id_users, HeatTransferInFins2_text1) VALUES (?,?)"""
            dataVariable = (user, text)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage18.setText("Update")
        print("update")



    def PlainTextHeatTransfer3_text1(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT HeatTransferInFins3_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()



        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute("SELECT HeatTransferInFins3_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))
            resultats2 = curseur2.fetchone()

            self.plainTextEditPage19.insertPlainText(resultats2[0])
            self.updateResponsePage19.clicked.connect(lambda : self.onClickedUpdateTextHeatTransfer3(user))

        else:
            self.updateResponsePage19.clicked.connect(lambda : self.onClickedUpdateTextHeatTransfer3(user))


    def onClickedUpdateTextHeatTransfer3(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        text = self.plainTextEditPage19.toPlainText()

        curseur.execute("SELECT HeatTransferInFins3_text1 FROM HeatTransferInFins WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()
        if len(resultats) != 0:
            curseur.execute("UPDATE HeatTransferInFins SET HeatTransferInFins3_text1 = ? WHERE id_users = ? ",
                            (text, user,))

        else:
            queryInsert = """INSERT INTO HeatTransferInFins (id_users, HeatTransferInFins3_text1) VALUES (?,?)"""
            dataVariable = (user, text)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage19.setText("Update")

        print("update")






    def PlainTextHeatTransfer4(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT HeatTransferInFins4_text1,HeatTransferInFins4_text2,HeatTransferInFins4_text3,HeatTransferInFins4_text4,HeatTransferInFins4_text5,HeatTransferInFins4_text6,HeatTransferInFins4_text7 FROM HeatTransferInFins WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()



        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute("SELECT HeatTransferInFins4_text1,HeatTransferInFins4_text2,HeatTransferInFins4_text3,HeatTransferInFins4_text4,HeatTransferInFins4_text5,HeatTransferInFins4_text6,HeatTransferInFins4_text7 FROM HeatTransferInFins WHERE id_users = ? ", (user,))
            resultats2 = curseur2.fetchone()

            self.lineEditPage20_1.setText(resultats2[0])
            self.lineEditPage20_2.setText(resultats2[1])
            self.lineEditPage20_3.setText(resultats2[2])
            self.lineEditPage20_4.setText(resultats2[3])
            self.lineEditPage20_5.setText(resultats2[4])
            self.lineEditPage20_6.setText(resultats2[5])
            self.lineEditPage20_7.setText(resultats2[6])

            self.updateResponsePage20.clicked.connect(lambda : self.onClickedUpdateTextHeatTransfer4(user))

        else:
            self.updateResponsePage20.clicked.connect(lambda : self.onClickedUpdateTextHeatTransfer4(user))


    def onClickedUpdateTextHeatTransfer4(self,user):


        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()
        line1 = self.lineEditPage20_1.text()
        line2 = self.lineEditPage20_2.text()
        line3 = self.lineEditPage20_3.text()
        line4 = self.lineEditPage20_4.text()
        line5 = self.lineEditPage20_5.text()
        line6 = self.lineEditPage20_6.text()
        line7 = self.lineEditPage20_7.text()


        curseur.execute("SELECT HeatTransferInFins4_text1,HeatTransferInFins4_text2,HeatTransferInFins4_text3,HeatTransferInFins4_text4,HeatTransferInFins4_text5,HeatTransferInFins4_text6,HeatTransferInFins4_text7 FROM HeatTransferInFins WHERE id_users = ? ", (user,))

        resultats = curseur.fetchall()
        if len(resultats) != 0:
            curseur.execute("UPDATE HeatTransferInFins SET HeatTransferInFins4_text1 = ?, HeatTransferInFins4_text2 = ? ,HeatTransferInFins4_text3 = ? , HeatTransferInFins4_text4 = ? ,HeatTransferInFins4_text5 =? ,HeatTransferInFins4_text6 =? ,HeatTransferInFins4_text7 = ? WHERE id_users = ? ",
                            (line1, line2, line3, line4, line5, line6, line7, user,))

        else:
            queryInsert = """INSERT INTO HeatTransferInFins (id_users, HeatTransferInFins4_text1,HeatTransferInFins4_text2,HeatTransferInFins4_text3,HeatTransferInFins4_text4,HeatTransferInFins4_text5,HeatTransferInFins4_text6,HeatTransferInFins4_text7) VALUES (?,?,?,?,?,?,?,?)"""
            dataVariable = (user, line1, line2, line3, line4, line5, line6, line7)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage20.setText("Update")

        print("update")

