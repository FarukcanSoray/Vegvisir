#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QCompleter
from database import *
import pdfrw # pdf
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyQt5.QtCore import  QPoint
from add_offer_interface import Ui_Dialog as add_offer_dialog


db = Database()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 950, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Tarih', 'Şirket', 'Yetkili', 'Telefon', 'Mail', 'Adres', 'Hatırlatma'])
        self.tableWidget.verticalHeader().hide()

        self.listCompanyEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.listCompanyEditBox.setGeometry(QtCore.QRect(100,500,113,25))
        self.listCompanyEditBox.setObjectName("listCompanyEditBox")
        self.searchPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchPushButton.setGeometry(QtCore.QRect(100, 550, 89, 25))
        self.searchPushButton.setObjectName("searchPushButton")

        self.completer = QCompleter(db.make_list_for_recommend_autofill())
        #self.completer.activated.connect(lambda: self.otomatik_doldur(self.kitapAdi.text()))
        self.listCompanyEditBox.setCompleter(self.completer)

        self.companyEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.companyEditBox.setGeometry(QtCore.QRect(1000, 80, 113, 25))
        self.companyEditBox.setObjectName("companyEditBox")
        self.contactEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.contactEditBox.setGeometry(QtCore.QRect(1000, 130, 113, 25))
        self.contactEditBox.setObjectName("contactEditBox")
        self.telephoneEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.telephoneEditBox.setGeometry(QtCore.QRect(1000, 170, 113, 25))
        self.telephoneEditBox.setObjectName("telephoneEditBox")
        self.mailEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.mailEditBox.setGeometry(QtCore.QRect(1000, 210, 113, 25))
        self.mailEditBox.setObjectName("mailEditBox")
        self.addressEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.addressEditBox.setGeometry(QtCore.QRect(1000, 250, 113, 25))
        self.addressEditBox.setObjectName("addressEditBox")
        self.remindTimeEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.remindTimeEditBox.setGeometry(QtCore.QRect(1000, 290, 113, 25))
        self.remindTimeEditBox.setObjectName("remindTimeEditBox")
        self.offerDateEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.offerDateEditBox.setGeometry(QtCore.QRect(1000, 330, 113, 25))
        self.offerDateEditBox.setObjectName("offerDateEditBox")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1010, 390, 89, 25))
        self.pushButton.setObjectName("pushButton")





        self.addPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPushButton.setGeometry(QtCore.QRect(1510, 390, 89, 25))
        self.addPushButton.setObjectName("addPushButton")

        self.lastPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastPushButton.setGeometry(QtCore.QRect(250, 550, 89, 25))
        self.lastPushButton.setObjectName("lastPushButton")

        self.createLastPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.createLastPushButton.setGeometry(QtCore.QRect(350, 550, 140, 25))
        self.createLastPushButton.setObjectName("createLastPushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.last_10_offer()
        self.fill_boxes()
        self.pushButton.clicked.connect(lambda: self.send_data_to_edit())
        self.searchPushButton.clicked.connect(lambda: self.search_results_to_table(self.listCompanyEditBox.text()))

        #self.addPushButton.clicked.connect(lambda: self.renew_completers())
        #self.addPushButton.clicked.connect(lambda: self.last_10_offer())
        self.addPushButton.clicked.connect(lambda: self.open_add_offer_interface())

        self.lastPushButton.clicked.connect(lambda: self.last_10_offer())

        self.createLastPushButton.clicked.connect(lambda: self.create_last_offer_PDF())

        self.tableWidget.cellDoubleClicked.connect(self.create_PDF_from_table_click)

        self.tableWidget.cellDoubleClicked.connect(self.fill_boxes_by_id)

        #add_offer_dialog.addPushButton.clicked.connect(lambda: self.last_10_offer())

    def renew_completers(self):
        self.completer = QCompleter(db.make_list_for_recommend_autofill())
        self.listCompanyEditBox.setCompleter(self.completer)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.searchPushButton.setText(_translate("MainWindow", "Şirket Ara"))
        self.addPushButton.setText(_translate("MainWindow", "Teklif Ekle"))
        self.lastPushButton.setText(_translate("MainWindow", "Son 10 Teklif"))
        self.createLastPushButton.setText(_translate("MainWindow", "Son Teklif PDF Oluştur"))



    def create_last_offer_PDF(self):
        offer = db.make_last_offer()
        self.create_overlay(offer)
        self.merge_pdfs('Template-Teklif.pdf','simple_form_overlay.pdf','merged_form.pdf')
        self.open_PDF()

    def create_PDF_from_table_click(self, row, column):
        offerRowID = int(self.tableWidget.item(row,0).text())
        offer = db.get_offer_by_id(offerRowID)
        self.create_overlay(offer)
        self.merge_pdfs('Template-Teklif.pdf','simple_form_overlay.pdf','merged_form.pdf')
        self.open_PDF()

    def open_PDF(self):
        import webbrowser
        webbrowser.open_new(r'./merged_form.pdf')

    def fill_boxes_by_id(self, row, column):
        offerRowID = int(self.tableWidget.item(row,0).text())
        offer = db.get_offer_by_id(offerRowID)
        self.companyEditBox.setText(offer[0][2])
        self.contactEditBox.setText(offer[0][3])
        self.telephoneEditBox.setText(offer[0][4])
        self.mailEditBox.setText(offer[0][5])
        self.addressEditBox.setText(offer[0][6])
        self.remindTimeEditBox.setText(str(offer[0][7]))
        self.offerDateEditBox.setText(offer[0][1])


    def create_overlay(self, offer):
        pdfmetrics.registerFont(TTFont('Times-New-Roman', 'Times New Roman.ttf'))
        c = canvas.Canvas('simple_form_overlay.pdf')
        c.setFont('Times-New-Roman', 10)
        c.drawString(85, 624, offer[0][2])
        c.drawString(85, 610, offer[0][3])
        c.drawString(90, 596, offer[0][5])
        c.drawString(355, 624, offer[0][6])
        c.drawString(372, 610, offer[0][4])
        c.drawString(355, 596, 'Periyodik Kontrol')
        c.drawString(475, 659, offer[0][1] + "/" + format(offer[0][0], '04d'))

        c.save()

    def merge_pdfs(self, form_pdf, overlay_pdf, output):
        form = pdfrw.PdfReader(form_pdf)
        olay = pdfrw.PdfReader(overlay_pdf)

        for form_page, overlay_page in zip(form.pages, olay.pages):
            merge_obj = pdfrw.PageMerge()
            overlay = merge_obj.add(overlay_page)[0]
            pdfrw.PageMerge(form_page).add(overlay).render()

        writer = pdfrw.PdfWriter()
        writer.write(output, form)



    def last_10_offer(self):
        offers = db.make_last_10_offer()
        self.tableWidget.setRowCount(0)
        for i in range(len(offers)):
            self.tableWidget.insertRow(i)
            lst = list(offers[i])
            lst[0] = format(lst[0], '04d')
            offers[i] = tuple(lst)
            for j in range(8):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(offers[i][j])))

    def search_results_to_table(self, name):
        offers = db.search_by_company(name)
        self.tableWidget.setRowCount(0)
        for i in range(len(offers)):
            self.tableWidget.insertRow(i)
            lst = list(offers[i])
            lst[0] = format(lst[0], '04d')
            offers[i] = tuple(lst)
            for j in range(8):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(offers[i][j])))

    def fill_boxes(self):
        last_offer = db.find_last_offer()
        if len(last_offer) != 0:
            self.companyEditBox.setText(last_offer[0][1])
            self.contactEditBox.setText(last_offer[0][2])
            self.telephoneEditBox.setText(last_offer[0][3])
            self.mailEditBox.setText(last_offer[0][4])
            self.addressEditBox.setText(last_offer[0][5])
            self.remindTimeEditBox.setText(str(last_offer[0][6]))
            self.offerDateEditBox.setText(last_offer[0][0])

    def send_data_to_edit(self):
        offerDate = self.offerDateEditBox.text()
        company = self.companyEditBox.text()
        contact = self.contactEditBox.text()
        telephone = self.telephoneEditBox.text()
        mail = self.mailEditBox.text()
        address = self.addressEditBox.text()
        remindTime = int(self.remindTimeEditBox.text())
        data = Offer(offerDate, company, contact, telephone, mail, address, remindTime)
        db.edit_offer(data)

    def open_add_offer_interface(self):
        self.updateWindow = QDialog()
        self.ui_update = add_offer_dialog()
        self.ui_update.setupUi(self.updateWindow)
        self.ui_update.addPushButton.clicked.connect(lambda: self.last_10_offer())
        self.ui_update.addPushButton.clicked.connect(lambda: self.renew_completers())
        self.ui_update.addPushButton.clicked.connect(lambda: self.fill_boxes())
        self.updateWindow.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
