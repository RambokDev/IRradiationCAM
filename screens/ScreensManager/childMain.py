import sys
from PyQt5.uic import loadUi
from screens.ScreensManager.manager import *
from screens.SurfaceObservation.SurfaceObservationsScreens import *
from screens.TemperatureCalculation.TemperatureCalculationScreens import *


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        # self.pageapp = pageAPP()

        loadUi('main.ui', self)
        self.setWindowTitle("IR TP")

        # pour la gestion des pages
        # self.managerPagesApp()
        # self.indexbtn()
        #
        # # pour les video sufaceObservation
        # self.setupVideo1SurfaceObservation()
        # self.setupVideo2SurfaceObservation()
        # self.setupVideo3SurfaceObservation()
        #
        # # pour les plain text surfaceObservation
        # self.PlainTextSurfaceObservation1_text1()
        # self.PlainTextSurfaceObservation2_text1()
        # self.PlainTextSurfaceObservation3_text1()
        #
        # # pour les video Temperature Calculation
        # self.setupVideo1TemperatureCalculation()
        #


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
