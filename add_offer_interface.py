# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_offer_interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtWidgets import QMainWindow
from database import *
import arrow # date

db = Database()

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(245, 473)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")

        self.addCompanyEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.addCompanyEditBox.setGeometry(QtCore.QRect(100, 50, 113, 25))
        self.addCompanyEditBox.setObjectName("addCompanyEditBox")
        self.addContactEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.addContactEditBox.setGeometry(QtCore.QRect(100, 100, 113, 25))
        self.addContactEditBox.setObjectName("addContactEditBox")
        self.addTelephoneEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.addTelephoneEditBox.setGeometry(QtCore.QRect(100, 150, 113, 25))
        self.addTelephoneEditBox.setObjectName("addTelephoneEditBox")
        self.addMailEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.addMailEditBox.setGeometry(QtCore.QRect(100, 200, 113, 25))
        self.addMailEditBox.setObjectName("addMailEditBox")
        self.addAddressEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.addAddressEditBox.setGeometry(QtCore.QRect(100, 250, 113, 25))
        self.addAddressEditBox.setObjectName("addAddressEditBox")
        self.addRemindTimeEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.addRemindTimeEditBox.setGeometry(QtCore.QRect(100, 300, 113, 25))
        self.addRemindTimeEditBox.setObjectName("addRemindTimeEditBox")
        self.addOfferDateEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.addOfferDateEditBox.setGeometry(QtCore.QRect(100, 350, 113, 25))
        self.addOfferDateEditBox.setObjectName("addOfferDateEditBox")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(50,50,100,25))
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.label2.setGeometry(QtCore.QRect(50,100,100,25))
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("label")
        self.label3.setGeometry(QtCore.QRect(50,150,100,25))
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setObjectName("label")
        self.label4.setGeometry(QtCore.QRect(50,200,100,25))
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setObjectName("label")
        self.label5.setGeometry(QtCore.QRect(50,250,100,25))
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setObjectName("label")
        self.label6.setGeometry(QtCore.QRect(0,300,100,25))
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setObjectName("label")
        self.label7.setGeometry(QtCore.QRect(20,350,100,25))

        self.completer = QCompleter(db.make_list_for_recommend_autofill())
        self.completer.activated.connect(lambda: self.autofill(self.addCompanyEditBox.text()))
        self.addCompanyEditBox.setCompleter(self.completer)

        self.addPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPushButton.setGeometry(QtCore.QRect(70, 400, 89, 25))
        self.addPushButton.setObjectName("addPushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        self.addPushButton.clicked.connect(lambda: self.send_data_to_add())
        self.addPushButton.clicked.connect(self.addCompanyEditBox.clear)
        self.addPushButton.clicked.connect(self.addContactEditBox.clear)
        self.addPushButton.clicked.connect(self.addTelephoneEditBox.clear)
        self.addPushButton.clicked.connect(self.addMailEditBox.clear)
        self.addPushButton.clicked.connect(self.addAddressEditBox.clear)
        self.addPushButton.clicked.connect(self.addRemindTimeEditBox.clear)
        self.addPushButton.clicked.connect(lambda: self.addOfferDateEditBox.setText(arrow.now().format('DDMMYY')))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addPushButton.setText(_translate("Dialog", "Ekle"))
        self.label.setText(_translate("Dialog", "Şirket: "))
        self.label2.setText(_translate("Dialog", "Yetkili: "))
        self.label3.setText(_translate("Dialog", "Telefon: "))
        self.label4.setText(_translate("Dialog", "Mail: "))
        self.label5.setText(_translate("Dialog", "Adres: "))
        self.label6.setText(_translate("Dialog", "Yenileme Tarihi: "))
        self.label7.setText(_translate("Dialog", "Teklif Tarihi: "))
        self.addOfferDateEditBox.setText(arrow.now().format('DDMMYY'))

    def send_data_to_add(self):
        company = self.addCompanyEditBox.text()
        contact = self.addContactEditBox.text()
        telephone = self.addTelephoneEditBox.text()
        mail = self.addMailEditBox.text()
        address = self.addAddressEditBox.text()
        remindTime = int(self.addRemindTimeEditBox.text())
        date = self.addOfferDateEditBox.text()
        new_offer = Offer(date, company, contact, telephone, mail, address, remindTime)
        db.add_offer(new_offer)

    def renew_completers(self):
        self.completer = QCompleter(db.make_list_for_recommend_autofill())
        self.completer.activated.connect(lambda: self.autofill(self.addCompanyEditBox.text()))
        self.addCompanyEditBox.setCompleter(self.completer)


    def autofill(self, name):
        list = db.get_last_offer_for_autofill(name)
        self.addContactEditBox.setText(list[0][0])
        self.addTelephoneEditBox.setText(list[0][1])
        self.addMailEditBox.setText(list[0][2])
        self.addAddressEditBox.setText(list[0][3])
        self.addRemindTimeEditBox.setText(str(list[0][4]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
