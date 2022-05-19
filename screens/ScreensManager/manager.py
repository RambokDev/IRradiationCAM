from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow



class managerApp():

    def __init__(self):
        self.index = 0


    def managerPagesApp(self):
        # Pages
        ###################


        self.btn_acceuil.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Acceuil))
        self.btn_acceuil.clicked.connect(self.indexbtn)

        # page 2
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_page_2.clicked.connect(self.indexbtn)

        # page 3
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_page_3.clicked.connect(self.indexbtn)

        # page 4
        self.btn_page_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.btn_page_4.clicked.connect(self.indexbtn)

        # page 5
        self.btn_page_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.btn_page_5.clicked.connect(self.indexbtn)

        # page 6
        self.btn_page_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.btn_page_6.clicked.connect(self.indexbtn)

        # page 7
        self.btn_page_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7))
        self.btn_page_7.clicked.connect(self.indexbtn)

        # page 8
        self.btn_page_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_8))
        self.btn_page_8.clicked.connect(self.indexbtn)

        # page 9
        self.btn_page_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_9))
        self.btn_page_9.clicked.connect(self.indexbtn)

        # page 10
        self.btn_page_10.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_10))
        self.btn_page_10.clicked.connect(self.indexbtn)

        # page 11
        self.btn_page_11.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_11))
        self.btn_page_11.clicked.connect(self.indexbtn)

        # page 12
        self.btn_page_12.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_12))
        self.btn_page_12.clicked.connect(self.indexbtn)

        # page 13
        self.btn_page_13.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_13))
        self.btn_page_13.clicked.connect(self.indexbtn)

        # page 14
        self.btn_page_14.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_14))
        self.btn_page_14.clicked.connect(self.indexbtn)

        # page 15
        self.btn_page_15.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_15))
        self.btn_page_15.clicked.connect(self.indexbtn)

        # page 16
        self.btn_page_16.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_16))
        self.btn_page_16.clicked.connect(self.indexbtn)

        # page 17
        self.btn_page_17.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_17))
        self.btn_page_17.clicked.connect(self.indexbtn)

        # page 18
        self.btn_page_18.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_18))
        self.btn_page_18.clicked.connect(self.indexbtn)

        # page 19
        self.btn_page_19.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_19))
        self.btn_page_19.clicked.connect(self.indexbtn)

        # page 20
        self.btn_page_20.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_20))
        self.btn_page_20.clicked.connect(self.indexbtn)

        # page 21
        self.btn_page_21.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_21))
        self.btn_page_21.clicked.connect(self.indexbtn)

        # page 22
        self.btn_page_22.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_22))
        self.btn_page_22.clicked.connect(self.indexbtn)

        # page 23
        self.btn_page_23.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_23))
        self.btn_page_23.clicked.connect(self.indexbtn)

        # page 24
        self.btn_page_24.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_24))
        self.btn_page_24.clicked.connect(self.indexbtn)

    def indexbtn(self):

        self.index = self.stackedWidget.currentIndex()


        page = [self.page_Acceuil, self.page_2, self.page_3, self.page_4, self.page_5, self.page_6, self.page_7,
                self.page_8, self.page_9, self.page_10, self.page_11, self.page_12, self.page_13, self.page_14,
                self.page_15, self.page_16, self.page_17, self.page_18, self.page_19, self.page_20, self.page_21,
                self.page_22, self.page_23, self.page_24]

        next = [self.next1, self.next2, self.next3, self.next4, self.next5, self.next6, self.next7, self.next8,
                self.next9, self.next10, self.next11, self.next12, self.next13, self.next14, self.next15, self.next16,
                self.next17, self.next18, self.next19, self.next20, self.next21, self.next22, self.next23, self.next24]

        back = [self.page_Acceuil, self.back2, self.back3, self.back4, self.back5, self.back6, self.back7, self.back8,
                self.back9, self.back10, self.back11, self.back12, self.back13, self.back14, self.back15, self.back16,
                self.back17, self.back18, self.back19, self.back20, self.back21, self.back22,
                self.back23, self.back24]

        exit = [self.exit1, self.exit2, self.exit3, self.exit4, self.exit5, self.exit6, self.exit7, self.exit8,
                self.exit9, self.exit10, self.exit11, self.exit12, self.exit13, self.exit14, self.exit15, self.exit16,
                self.exit17, self.exit18, self.exit19, self.exit20, self.exit21, self.exit22,
                self.exit23, self.exit24]

        if self.index == 0:
            exit[0].clicked.connect(self.closeApp)
            next[0].disconnect()
            next[0].clicked.connect(lambda: self.stackedWidget.setCurrentWidget(page[self.index + 1]))
            next[self.index].clicked.connect(self.indexbtn)

        elif self.index == 23:
            exit[23].clicked.connect(self.closeApp)
            back[23].disconnect()
            back[23].clicked.connect(lambda: self.stackedWidget.setCurrentWidget(page[23 - 1]))
            back[self.index].clicked.connect(self.indexbtn)
            next[23].disconnect()
            next[23].clicked.connect(lambda: self.stackedWidget.setCurrentWidget(page[0]))
            next[self.index].clicked.connect(self.indexbtn)

        elif 0 < self.index < 23:
            next[self.index].disconnect()
            next[self.index].pressed.connect(lambda: self.stackedWidget.setCurrentWidget(page[self.index + 1]))
            back[self.index].disconnect()
            back[self.index].pressed.connect(lambda: self.stackedWidget.setCurrentWidget(page[self.index - 1]))
            next[self.index].pressed.connect(self.indexbtn)
            back[self.index].pressed.connect(self.indexbtn)
            exit[self.index].pressed.connect(self.closeApp)



    def closeApp(self):
        QApplication.quit()
