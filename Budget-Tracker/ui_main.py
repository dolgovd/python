# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 600)
        MainWindow.setStyleSheet(u"backgound-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Gill Sans\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.All_actions = QHBoxLayout()
        self.All_actions.setObjectName(u"All_actions")
        self.Balance_frame = QFrame(self.centralwidget)
        self.Balance_frame.setObjectName(u"Balance_frame")
        self.Balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.Balance = QVBoxLayout(self.Balance_frame)
        self.Balance.setSpacing(0)
        self.Balance.setObjectName(u"Balance")
        self.Balance.setContentsMargins(12, 12, 12, 12)
        self.lb_balance_title = QLabel(self.Balance_frame)
        self.lb_balance_title.setObjectName(u"lb_balance_title")
        self.lb_balance_title.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.Balance.addWidget(self.lb_balance_title)

        self.lb_balance = QLabel(self.Balance_frame)
        self.lb_balance.setObjectName(u"lb_balance")
        self.lb_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.Balance.addWidget(self.lb_balance)

        self.Income = QHBoxLayout()
        self.Income.setSpacing(0)
        self.Income.setObjectName(u"Income")
        self.lb_income_ico = QLabel(self.Balance_frame)
        self.lb_income_ico.setObjectName(u"lb_income_ico")
        self.lb_income_ico.setMaximumSize(QSize(24, 16777215))
        self.lb_income_ico.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.lb_income_ico.setPixmap(QPixmap(u":/icons/icons/north_west_white_24dp.svg"))

        self.Income.addWidget(self.lb_income_ico)

        self.lb_income = QLabel(self.Balance_frame)
        self.lb_income.setObjectName(u"lb_income")
        self.lb_income.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.Income.addWidget(self.lb_income)


        self.Balance.addLayout(self.Income)

        self.lb_income_amount = QLabel(self.Balance_frame)
        self.lb_income_amount.setObjectName(u"lb_income_amount")
        self.lb_income_amount.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.Balance.addWidget(self.lb_income_amount)

        self.Outcome = QHBoxLayout()
        self.Outcome.setSpacing(0)
        self.Outcome.setObjectName(u"Outcome")
        self.lb_outcome_ico = QLabel(self.Balance_frame)
        self.lb_outcome_ico.setObjectName(u"lb_outcome_ico")
        self.lb_outcome_ico.setMaximumSize(QSize(24, 16777215))
        self.lb_outcome_ico.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.lb_outcome_ico.setPixmap(QPixmap(u":/icons/icons/call_received_white_24dp.svg"))

        self.Outcome.addWidget(self.lb_outcome_ico)

        self.lb_outcome = QLabel(self.Balance_frame)
        self.lb_outcome.setObjectName(u"lb_outcome")
        self.lb_outcome.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.Outcome.addWidget(self.lb_outcome)


        self.Balance.addLayout(self.Outcome)

        self.lb_outcome_amount = QLabel(self.Balance_frame)
        self.lb_outcome_amount.setObjectName(u"lb_outcome_amount")
        self.lb_outcome_amount.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.Balance.addWidget(self.lb_outcome_amount)


        self.All_actions.addWidget(self.Balance_frame)

        self.Expenses_frame = QFrame(self.centralwidget)
        self.Expenses_frame.setObjectName(u"Expenses_frame")
        self.Expenses_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.Expenses = QVBoxLayout(self.Expenses_frame)
        self.Expenses.setObjectName(u"Expenses")
        self.lb_expenses = QLabel(self.Expenses_frame)
        self.lb_expenses.setObjectName(u"lb_expenses")
        self.lb_expenses.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses.addWidget(self.lb_expenses)

        self.Expenses_grocery = QHBoxLayout()
        self.Expenses_grocery.setObjectName(u"Expenses_grocery")
        self.lb_exp_grocery_ico = QLabel(self.Expenses_frame)
        self.lb_exp_grocery_ico.setObjectName(u"lb_exp_grocery_ico")
        self.lb_exp_grocery_ico.setMaximumSize(QSize(24, 16777215))
        self.lb_exp_grocery_ico.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lb_exp_grocery_ico.setPixmap(QPixmap(u":/icons/icons/local_grocery_store_white_24dp.svg"))

        self.Expenses_grocery.addWidget(self.lb_exp_grocery_ico)

        self.lb_exp_grocery_category = QLabel(self.Expenses_frame)
        self.lb_exp_grocery_category.setObjectName(u"lb_exp_grocery_category")
        self.lb_exp_grocery_category.setMaximumSize(QSize(128, 16777215))
        self.lb_exp_grocery_category.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses_grocery.addWidget(self.lb_exp_grocery_category)

        self.lb_exp_grocery_amount = QLabel(self.Expenses_frame)
        self.lb_exp_grocery_amount.setObjectName(u"lb_exp_grocery_amount")
        self.lb_exp_grocery_amount.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses_grocery.addWidget(self.lb_exp_grocery_amount)


        self.Expenses.addLayout(self.Expenses_grocery)

        self.Expenses_entertaiment = QHBoxLayout()
        self.Expenses_entertaiment.setObjectName(u"Expenses_entertaiment")
        self.lb_exp_intertaiment_ico = QLabel(self.Expenses_frame)
        self.lb_exp_intertaiment_ico.setObjectName(u"lb_exp_intertaiment_ico")
        self.lb_exp_intertaiment_ico.setMaximumSize(QSize(24, 16777215))
        self.lb_exp_intertaiment_ico.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lb_exp_intertaiment_ico.setPixmap(QPixmap(u":/icons/icons/sports_esports_white_24dp.svg"))

        self.Expenses_entertaiment.addWidget(self.lb_exp_intertaiment_ico)

        self.lb_exp_entertaiment_category = QLabel(self.Expenses_frame)
        self.lb_exp_entertaiment_category.setObjectName(u"lb_exp_entertaiment_category")
        self.lb_exp_entertaiment_category.setMaximumSize(QSize(128, 16777215))
        self.lb_exp_entertaiment_category.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses_entertaiment.addWidget(self.lb_exp_entertaiment_category)

        self.lb_exp_entertaiment_amount = QLabel(self.Expenses_frame)
        self.lb_exp_entertaiment_amount.setObjectName(u"lb_exp_entertaiment_amount")
        self.lb_exp_entertaiment_amount.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses_entertaiment.addWidget(self.lb_exp_entertaiment_amount)


        self.Expenses.addLayout(self.Expenses_entertaiment)

        self.Expenses_auto = QHBoxLayout()
        self.Expenses_auto.setObjectName(u"Expenses_auto")
        self.lb_exp_auto_ico = QLabel(self.Expenses_frame)
        self.lb_exp_auto_ico.setObjectName(u"lb_exp_auto_ico")
        self.lb_exp_auto_ico.setMaximumSize(QSize(24, 16777215))
        self.lb_exp_auto_ico.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lb_exp_auto_ico.setPixmap(QPixmap(u":/icons/icons/directions_car_white_24dp.svg"))

        self.Expenses_auto.addWidget(self.lb_exp_auto_ico)

        self.lb_exp_auto_category = QLabel(self.Expenses_frame)
        self.lb_exp_auto_category.setObjectName(u"lb_exp_auto_category")
        self.lb_exp_auto_category.setMaximumSize(QSize(128, 16777215))
        self.lb_exp_auto_category.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses_auto.addWidget(self.lb_exp_auto_category)

        self.lb_exp_auto_amount = QLabel(self.Expenses_frame)
        self.lb_exp_auto_amount.setObjectName(u"lb_exp_auto_amount")
        self.lb_exp_auto_amount.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses_auto.addWidget(self.lb_exp_auto_amount)


        self.Expenses.addLayout(self.Expenses_auto)

        self.Expenses_other = QHBoxLayout()
        self.Expenses_other.setObjectName(u"Expenses_other")
        self.lb_exp_other_ico = QLabel(self.Expenses_frame)
        self.lb_exp_other_ico.setObjectName(u"lb_exp_other_ico")
        self.lb_exp_other_ico.setMaximumSize(QSize(24, 16777215))
        self.lb_exp_other_ico.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lb_exp_other_ico.setPixmap(QPixmap(u":/icons/icons/list_white_24dp.svg"))

        self.Expenses_other.addWidget(self.lb_exp_other_ico)

        self.lb_exp_other_category = QLabel(self.Expenses_frame)
        self.lb_exp_other_category.setObjectName(u"lb_exp_other_category")
        self.lb_exp_other_category.setMaximumSize(QSize(128, 16777215))
        self.lb_exp_other_category.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses_other.addWidget(self.lb_exp_other_category)

        self.lb_exp_auto_ico_2 = QLabel(self.Expenses_frame)
        self.lb_exp_auto_ico_2.setObjectName(u"lb_exp_auto_ico_2")
        self.lb_exp_auto_ico_2.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.Expenses_other.addWidget(self.lb_exp_auto_ico_2)


        self.Expenses.addLayout(self.Expenses_other)


        self.All_actions.addWidget(self.Expenses_frame)


        self.verticalLayout_3.addLayout(self.All_actions)

        self.bt_actions = QHBoxLayout()
        self.bt_actions.setObjectName(u"bt_actions")
        self.bt_add_transaction = QPushButton(self.centralwidget)
        self.bt_add_transaction.setObjectName(u"bt_add_transaction")
        self.bt_add_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_add_transaction.setIcon(icon)
        self.bt_add_transaction.setIconSize(QSize(24, 24))

        self.bt_actions.addWidget(self.bt_add_transaction)

        self.bt_edit_transaction = QPushButton(self.centralwidget)
        self.bt_edit_transaction.setObjectName(u"bt_edit_transaction")
        self.bt_edit_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_edit_transaction.setIcon(icon1)
        self.bt_edit_transaction.setIconSize(QSize(24, 24))

        self.bt_actions.addWidget(self.bt_edit_transaction)

        self.bt_del_transaction = QPushButton(self.centralwidget)
        self.bt_del_transaction.setObjectName(u"bt_del_transaction")
        self.bt_del_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_del_transaction.setIcon(icon2)
        self.bt_del_transaction.setIconSize(QSize(24, 24))

        self.bt_actions.addWidget(self.bt_del_transaction)


        self.verticalLayout_3.addLayout(self.bt_actions)

        self.tb_summary = QTableView(self.centralwidget)
        self.tb_summary.setObjectName(u"tb_summary")
        self.tb_summary.setStyleSheet(u"QTableView {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView:: section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView:: item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableView:: item:select {\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tb_summary.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_summary.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_summary.setShowGrid(False)
        self.tb_summary.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tb_summary)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Budget Tracker", None))
        self.lb_balance_title.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.lb_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_income_ico.setText("")
        self.lb_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.lb_income_amount.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_outcome_ico.setText("")
        self.lb_outcome.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.lb_outcome_amount.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.lb_exp_grocery_ico.setText("")
        self.lb_exp_grocery_category.setText(QCoreApplication.translate("MainWindow", u"Grocery", None))
        self.lb_exp_grocery_amount.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_exp_intertaiment_ico.setText("")
        self.lb_exp_entertaiment_category.setText(QCoreApplication.translate("MainWindow", u"Entertaiment", None))
        self.lb_exp_entertaiment_amount.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_exp_auto_ico.setText("")
        self.lb_exp_auto_category.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.lb_exp_auto_amount.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_exp_other_ico.setText("")
        self.lb_exp_other_category.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.lb_exp_auto_ico_2.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.bt_add_transaction.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.bt_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
        self.bt_del_transaction.setText(QCoreApplication.translate("MainWindow", u"Delete transaction", None))
    # retranslateUi

