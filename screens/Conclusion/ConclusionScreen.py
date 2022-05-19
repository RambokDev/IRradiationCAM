import os
import sqlite3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from numpy import array
from fpdf import FPDF, XPos, YPos

cheminBDD = "dataBase/TP.db"


class Conslusion:

    def PlainTextConclusion(self, user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute(
            "SELECT IR_RadiationCAM1_text1 FROM IR_RadiationCAM WHERE id_users = ? ",
            (user,))

        resultats = curseur.fetchall()

        if len(resultats) != 0:

            curseur2 = connexion.cursor()  # Récupération d'un curseur
            curseur2.execute(
                "SELECT IR_RadiationCAM1_text1 FROM IR_RadiationCAM WHERE id_users = ? ",
                (user,))

            resultats2 = curseur2.fetchone()

            self.plainTextEditPage24.insertPlainText(resultats2[0])
            self.updateResponsePage24.clicked.connect(lambda: self.onClickedUpdatePlainTextConclusion(user))
        else:

            self.updateResponsePage24.clicked.connect(lambda: self.onClickedUpdatePlainTextConclusion(user))

    def onClickedUpdatePlainTextConclusion(self, user):

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()

        text = self.plainTextEditPage24.toPlainText()

        curseur.execute(
            "SELECT IR_RadiationCAM1_text1 FROM IR_RadiationCAM WHERE id_users = ? ",
            (user,))
        resultats = curseur.fetchall()

        if len(resultats) != 0:
            curseur.execute(
                "UPDATE IR_RadiationCAM SET IR_RadiationCAM1_text1 = ?  WHERE id_users = ? ",
                (text, user,))
        else:
            queryInsert = """INSERT INTO IR_RadiationCAM (id_users, IR_RadiationCAM1_text1) VALUES (?,?)"""
            dataVariable = (user, text)
            curseur.execute(queryInsert, dataVariable)

        connexion.commit()  # enregistrement des modifications
        connexion.close()
        self.updateLabelPage24.setText("Update")

        print('update')

    def OpenFile(self,user):
        self.ExportResponsePage24.clicked.connect(lambda : self.OnclickedOpen_file(user))

    def OnclickedOpen_file(self,user):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File')
        print(filename)



        # requettes pour bdd PDF

        # -------------Surface Observation --------------
        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT * FROM surfaceObservation WHERE id_users = ? ", (user,))
        resultats = curseur.fetchall()
        SurfaceObservationData = []
        if len(resultats) != 0:
            for all in resultats:
                SurfaceObservationData.append(all[2])
                SurfaceObservationData.append(all[3])
                SurfaceObservationData.append(all[4])
        else:
            for i in range(3):
                SurfaceObservationData.append("Vous n'avez pas répondu à la question !  ")

        connexion.commit()  # enregistrement des modifications
        connexion.close()

        # -------------ContactTemperatureCalculation --------------
        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT * FROM ContactTemperatureCalculation WHERE id_users = ? ", (user,))
        resultats2 = curseur.fetchall()
        ContactTemperatureCalculationData = []
        if len(resultats2) != 0:
            for all in resultats2:
                ContactTemperatureCalculationData.append(all[2])
                ContactTemperatureCalculationData.append(all[3])
                ContactTemperatureCalculationData.append(all[4])
                ContactTemperatureCalculationData.append(all[5])
                ContactTemperatureCalculationData.append(all[6])
        else:
            for i in range(5):
                ContactTemperatureCalculationData.append("Vous n'avez pas répondu à la question !  ")

        connexion.commit()  # enregistrement des modifications
        connexion.close()

        # -------------ThermalApproachOfElectricPhenomena --------------

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT * FROM ThermalApproachOfElectricPhenomena WHERE id_users = ? ", (user,))
        resultats2 = curseur.fetchall()
        ThermalApproachOfElectricPhenomenaData = []
        if len(resultats2) != 0:
            for all in resultats2:
                ThermalApproachOfElectricPhenomenaData.append(all[2])
                ThermalApproachOfElectricPhenomenaData.append(all[3])
                ThermalApproachOfElectricPhenomenaData.append(all[4])
                ThermalApproachOfElectricPhenomenaData.append(all[5])
                ThermalApproachOfElectricPhenomenaData.append(all[6])
                ThermalApproachOfElectricPhenomenaData.append(all[7])
                ThermalApproachOfElectricPhenomenaData.append(all[8])
                ThermalApproachOfElectricPhenomenaData.append(all[9])
                ThermalApproachOfElectricPhenomenaData.append(all[10])
        else:
            for i in range(9):
                ThermalApproachOfElectricPhenomenaData.append("Vous n'avez pas répondu à la question !  ")

        connexion.commit()  # enregistrement des modifications
        connexion.close()

        # -------------HeatTransferInFins --------------

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT * FROM HeatTransferInFins WHERE id_users = ? ", (user,))
        resultats2 = curseur.fetchall()
        HeatTransferInFinsData = []
        if len(resultats2) != 0:
            for all in resultats2:
                HeatTransferInFinsData.append(all[2])
                HeatTransferInFinsData.append(all[3])
                HeatTransferInFinsData.append(all[4])
                HeatTransferInFinsData.append(all[5])
                HeatTransferInFinsData.append(all[6])
                HeatTransferInFinsData.append(all[7])
                HeatTransferInFinsData.append(all[8])
                HeatTransferInFinsData.append(all[9])
                HeatTransferInFinsData.append(all[10])
                HeatTransferInFinsData.append(all[11])
        else:
            for i in range(10):
                HeatTransferInFinsData.append("Vous n'avez pas répondu à la question !  ")

        connexion.commit()  # enregistrement des modifications
        connexion.close()

        # -------------IR_RadiationCAM --------------

        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT * FROM IR_RadiationCAM WHERE id_users = ? ", (user,))
        resultats2 = curseur.fetchall()
        IR_RadiationCAMData = []
        if len(resultats2) != 0:
            for all in resultats2:
                IR_RadiationCAMData.append(all[2])


        else:
            for i in range(1):
                IR_RadiationCAMData.append("Vous n'avez pas répondu à la question !  ")

        connexion.commit()  # enregistrement des modifications
        connexion.close()

        # -------------tableData --------------
        connexion = sqlite3.connect(cheminBDD)
        curseur = connexion.cursor()  # Récupération d'un curseur
        curseur.execute("SELECT * FROM tableData WHERE id_users = ? ", (user,))
        resultats2 = curseur.fetchall()
        # print(resultats2)
        tableDataBDD = []
        tableData = []
        tableData2 = []
        tableData3 = []
        tableData.append("L1=0.005")
        tableData2.append("L2/2=0.035")
        tableData3.append("L2=0.070")
        if len(resultats2) != 0:
            for all in resultats2:
                tableDataBDD.append(all[2])
                tableDataBDD.append(all[3])
                tableDataBDD.append(all[4])
                tableDataBDD.append(all[5])

            for i in range(4):
                tableData.append(tableDataBDD[i])

            for i2 in range(4,8):
                print(i2)
                tableData2.append(tableDataBDD[i2])

            for i3 in range(8,12):
                tableData3.append(tableDataBDD[i3])

            print(tableData)
            print(tableData2)
            print(tableData3)


            matriceTab1 = array([
                [' ','cosh(w.(L-x))', 'cosh(w.L)', 'cosh(w.(L-x))/cosh(x.L)', 'T(x)'],
                tableData,
                tableData2,
                tableData3,
            ])
            print(matriceTab1)

        else:
            matriceTab1 = array([
                [' ','cosh(w.(L-x))', 'cosh(w.L)', 'cosh(w.(L-x))/cosh(x.L)', 'T(x)'],
                ['L1=0.005','0', '0', '0', '0'],
                ['L2/2=0.035','0', '0', '0', '0'],
                ['L2=0.070','0', '0', '0', '0'],
            ])
            # for i in range(4):
            #     tableDataBDD.append(" - ")

        connexion.commit()  # enregistrement des modifications
        connexion.close()

        #
        # print(SurfaceObservationData)
        # print(ContactTemperatureCalculationData)
        # print(ThermalApproachOfElectricPhenomenaData)
        # print(HeatTransferInFinsData)
        # print(IR_RadiationCAMData)
        # print(tableData)
        self.pdfWrite(filename, SurfaceObservationData, ContactTemperatureCalculationData,
                      ThermalApproachOfElectricPhenomenaData, HeatTransferInFinsData,matriceTab1,IR_RadiationCAMData)
        # # if filename != '':
        # path = os.getcwd()
        # print(path)
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('/screens/SurfaceObservation/video1SurfaceObservation.mp4')))
        #
        # self.playBtn.setEnabled(True)

    def pdfWrite(self, filename, SurfaceObservationData, ContactTemperatureCalculationData,
                 ThermalApproachOfElectricPhenomenaData, HeatTransferInFinsData,matriceTab1,IR_RadiationCAMData):
        global nom1, nom2
        nom1 = "Gregoire BLANC"
        nom2 = "Charles GAUTHEREAU"
        # create a fpdf object
        pdf = PDF('P', 'mm', 'A4')
        pdf.set_auto_page_break(auto=True, margin=50)
        pdf.add_page()
        pdf.set_font('helvetica', '', 16)
        pdf.set_font('helvetica', 'B', 34)
        pdf.line(10, 70, 200, 70)
        pdf.cell(0, 120, "TP IR-RadiationCAM", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.line(10, 150, 200, 150)
        pdf.image('img/image3.png', x=60, y=170, w=90, h=70, type='', link='')
        pdf.add_page()

        # Surface Observation
        pdf.set_font('helvetica', 'U', 20)
        pdf.cell(0, 20, "I - Surface Observation :  ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.set_font('helvetica', '', 15)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, "Not painted aluminium surface", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        pdf.set_font('helvetica', '', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        border = pdf.x
        pdf.multi_cell(150, 5, 'What is the disadvantage of such a surface for infrared measurements?\n\n', 0, 0)

        # Reset x coordinate
        pdf.x = border
        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(150, 5, '{}\n\n\n'.format(SurfaceObservationData[0]), 0, 0)
        # Reset x coordinate
        pdf.x = border

        pdf.set_font('helvetica', '', 15)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, "Black painted aluminium surface", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        pdf.set_font('helvetica', '', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.multi_cell(170, 5, 'Explain why the measure is more realistic in comparison to the aluminum surface '
                               'temperature measurement?\n\n', 0, 0)

        # Reset x coordinate
        pdf.x = border
        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(SurfaceObservationData[1]), 0, 0)
        # Reset x coordinate
        pdf.x = border

        pdf.set_font('helvetica', '', 15)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, "Glass surface", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        pdf.set_font('helvetica', '', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.multi_cell(170, 5,
                       'Comment on the properties of the glass in the field of the visible and infrared. Do the '
                       'same by placing this time, the thin PVC sheet. What do you observe compared to the '
                       'previous experience?\n\n', 0, 0)

        # Reset x coordinate
        pdf.x = border
        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(SurfaceObservationData[2]), 0, 0)
        # Reset x coordinate
        pdf.x = border

        pdf.add_page()

        # Contact temperature calculation
        pdf.set_font('helvetica', 'U', 20)
        pdf.cell(0, 20, "II - Contact temperature calculation :  ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.set_font('helvetica', '', 15)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 20, "Watch video and record temperatures", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        pdf.set_font('helvetica', '', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(ContactTemperatureCalculationData[0]), 0, 0)
        # Reset x coordinate
        pdf.x = border
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, "IR T foam :  {}   °C ".format(ContactTemperatureCalculationData[1]), new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT, )
        pdf.cell(0, 5, "IR T aluminum :   {}   °C ".format(ContactTemperatureCalculationData[2]), new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT, )

        pdf.multi_cell(170, 5,
                       '\n\nUsing your documents, calculate the temperature of contact between your skin and the foam '
                       'and between your skin and the aluminum plate considering that samples are at 23 ° C and '
                       'your skin at 37 ° C.\n\n', 0, 0)

        # Reset x coordinate
        pdf.x = border
        pdf.cell(0, 5, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.cell(0, 5, "foam :  {}   °C ".format(ContactTemperatureCalculationData[3]), new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT, )
        pdf.cell(0, 5, "aluminum :   {}   °C ".format(ContactTemperatureCalculationData[4]), new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT, )

        # Thermal approach of electric phenomena
        pdf.set_font('helvetica', 'U', 20)
        pdf.cell(0, 20, "III - Thermal approach of electric phenomena :  ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.set_font('helvetica', '', 15)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 20, "Watch video and record temperatures", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        pdf.set_font('helvetica', '', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(ThermalApproachOfElectricPhenomenaData[0]), 0, 0)
        # Reset x coordinate
        pdf.x = border
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, "IR T à 6V :  {}   °C ".format(ThermalApproachOfElectricPhenomenaData[1]), new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT, )
        pdf.cell(0, 5, "IR T à 12V  :   {}   °C ".format(ThermalApproachOfElectricPhenomenaData[2]), new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT, )

        pdf.multi_cell(170, 5,
                       '\n\nKnowing that the bulb is composed of a glass, a filament and a gas envelope, what is the temperature element of the bulb you measure?\n\n',
                       0, 0)

        # Reset x coordinate
        pdf.x = border
        pdf.cell(0, 5, "CONCLUSION :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.cell(0, 5, "{}".format(ThermalApproachOfElectricPhenomenaData[3]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.set_font('helvetica', '', 15)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 20, "Watch video and record temperatures", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        pdf.set_font('helvetica', '', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 5, "What type of connection ?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(ThermalApproachOfElectricPhenomenaData[4]), 0, 0)
        # Reset x coordinate
        pdf.x = border
        pdf.multi_cell(170, 5,
                       '\n\nNote that the resistances are 100, 150 and 180 Ohms. Based on the infrared image taken with the IR camera, identify the three resistors. \n\n\n',
                       0, 0)

        pdf.x = border
        pdf.cell(0, 10, "For 100 Ohms :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', '', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(ThermalApproachOfElectricPhenomenaData[5]), 0, 0)
        pdf.x = border
        pdf.cell(0, 10, "For 150 Ohms :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(ThermalApproachOfElectricPhenomenaData[6]), 0, 0)
        pdf.x = border
        pdf.cell(0, 10, "For 180 Ohms :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', '', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(ThermalApproachOfElectricPhenomenaData[7]), 0, 0)
        pdf.x = border
        pdf.cell(0, 5, "CONCLUSION :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.cell(0, 5, "{}".format(ThermalApproachOfElectricPhenomenaData[8]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        # Heat transfer
        pdf.set_font('helvetica', 'U', 20)
        pdf.cell(0, 20, "IV - Heat transfer in fins :  ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', '', 15)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 20, "Watch video and record temperatures", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        pdf.set_font('helvetica', '', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(HeatTransferInFinsData[0]), 0, 0)
        # Reset x coordinate
        pdf.x = border

        pdf.set_font('helvetica', '', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.image('img/image10.png', x=60, w=90, h=70, type='', link='')
        pdf.cell(0, 5, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.cell(0, 5, "Write The order  : ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(HeatTransferInFinsData[1]), 0, 0)
        # Reset x coordinate
        pdf.x = border
        pdf.set_font('helvetica', '', 12)
        pdf.multi_cell(170, 5,
                       '\n\n Identifiez les différentes ailettes  de la gauche vers la droite (aluminium, acier et PVC) sur les images précédentes (justifiez votre choix)\n\n\n',
                       0, 0)

        pdf.x = border
        pdf.cell(0, 5, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border

        pdf.image('img/image11.png', x=60, w=90, h=70, type='', link='')
        pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(HeatTransferInFinsData[2]), 0, 0)
        pdf.x = border
        pdf.set_font('helvetica', '', 12)
        pdf.multi_cell(170, 5,
                       '\n\n With the IR camera, find the fins temperatures at the two extremities of the fin: at x = L1 = 5 mm and x = L2 = 70 mm. Find also T0 of the aluminum plate supporting the fins\n\n\n',
                       0, 0)

        pdf.x = border
        pdf.image('img/image16.png', x=60, w=90, h=70, type='', link='')

        pdf.cell(0, 10, "IR T1 Al: {}".format(HeatTransferInFinsData[3]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "IR T2 Al : {}".format(HeatTransferInFinsData[4]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "IR T0 base : {}".format(HeatTransferInFinsData[5]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "IR T1 ss : {}".format(HeatTransferInFinsData[6]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "IR T2 ss : {}".format(HeatTransferInFinsData[7]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "IR T1 PVC : {}".format(HeatTransferInFinsData[8]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "IR T2 PVC : {}".format(HeatTransferInFinsData[9]), new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "For Aluminuim fin : ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border
        pdf.cell(0, 10, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.x = border





        epw = pdf.w - 2 * pdf.l_margin
        col_width = epw / 5
        pdf.ln(0.5)
        th = pdf.font_size
        for row in matriceTab1:
            for datum in row:
                pdf.cell(col_width, 2*th, str(datum), border=1)
            pdf.ln(2*th)
        pdf.ln(4 * th)


        # Conclusion
        pdf.set_font('helvetica', 'U', 20)
        pdf.cell(0, 20, "V - Conclusion :  ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', '', 15)

        pdf.cell(0, 10, "Your Conclusion about this practical work :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
        pdf.set_font('helvetica', 'I', 12)
        pdf.multi_cell(170, 5, '{}\n\n\n'.format(IR_RadiationCAMData[0]), 0, 0)
        pdf.x = border


        pdf.output(filename + '.pdf')


class PDF(FPDF):

    def header(self):
        # logo
        self.image('img/icam.png', 150, 5, 25)
        self.set_font('helvetica', '', 12)
        self.cell(0, 10, '{}'.format(nom1), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 10, '{}'.format(nom2), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # self.cell(0, 10, 'TP', border=False, ln=1, align='C')
        # self.set_font('helvetica', 'B', 20)
        self.ln(10)

    # def Title(self):
    #     self.set_font('helvetica', 'B', 20)
    #     self.cell(10, 10, 'TP', border=False, ln=1, align='C')
    def footer(self):
        self.set_y(-15)
        self.image('img/footer.png', 5, 260, 215)
