# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_dialog

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(315, 373)
        Dialog.setStyleSheet(u"backgound-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Gill Sans\";")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_new_transaction = QLabel(self.frame)
        self.lb_new_transaction.setObjectName(u"lb_new_transaction")
        self.lb_new_transaction.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lb_new_transaction.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_new_transaction)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox: item {\n"
"color: black\n"
"}")

        self.verticalLayout.addWidget(self.cb_category)

        self.de_transaction_date = QDateEdit(self.frame)
        self.de_transaction_date.setObjectName(u"de_transaction_date")
        self.de_transaction_date.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10 px;\n"
"")
        self.de_transaction_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_transaction_date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.de_transaction_date.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.de_transaction_date)

        self.le_transaction_description = QLineEdit(self.frame)
        self.le_transaction_description.setObjectName(u"le_transaction_description")
        self.le_transaction_description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10 px;\n"
"")

        self.verticalLayout.addWidget(self.le_transaction_description)

        self.le_transaction_amount = QLineEdit(self.frame)
        self.le_transaction_amount.setObjectName(u"le_transaction_amount")
        self.le_transaction_amount.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10 px;")

        self.verticalLayout.addWidget(self.le_transaction_amount)

        self.cb_type = QComboBox(self.frame)
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.setObjectName(u"cb_type")
        self.cb_type.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox: item {\n"
"color: black\n"
"}")

        self.verticalLayout.addWidget(self.cb_type)

        self.bt_save_transaction = QPushButton(self.frame)
        self.bt_save_transaction.setObjectName(u"bt_save_transaction")
        self.bt_save_transaction.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"widgth: 230 px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/dialog-window/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_save_transaction.setIcon(icon)
        self.bt_save_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.bt_save_transaction)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lb_new_transaction.setText(QCoreApplication.translate("Dialog", u"New transaction", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Dialog", u"Grocery", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Dialog", u"Entertaiment", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category ...", None))
        self.le_transaction_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Put transaction description here ...", None))
        self.le_transaction_amount.setPlaceholderText(QCoreApplication.translate("Dialog", u"Put transaction amount here ...", None))
        self.cb_type.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.cb_type.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.bt_save_transaction.setText(QCoreApplication.translate("Dialog", u"Save new transaction", None))
    # retranslateUi

