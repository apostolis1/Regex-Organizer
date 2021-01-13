# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from backend.CopyFiles import organize_files
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_mainWindow(object):

    def set_root_folder(self)->None:
        file = str(QtWidgets.QFileDialog.getExistingDirectory(MainWindow, "Select Root Directory"))
        print(file)
        self.label_5.setText(file)
        return

    def set_dest_folder(self)->None:
        file = str(QtWidgets.QFileDialog.getExistingDirectory(MainWindow, "Select Destination Directory"))
        print(file)
        self.label_6.setText(file)
        return

    def prepare_organize_files(self) -> None:
        print("Clicked")
        src = self.label_5.text()
        dest_folder = self.label_6.text()
        regex_param = self.lineEdit.text()

        if not src.strip() or not dest_folder.strip() or not regex_param.strip() or src == "Root Folder" or dest_folder == "Destination Folder":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Invalid Input")
            msg.setInformativeText('Make sure you have selected a valid root and destination folder, and have provided a regex')
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        context = {}
        type_mappings = {
            "Move":"move",
            "Copy":"copy",
        }
        context["type"] = type_mappings[str(self.comboBox_3.currentText())]

        subfolder_mappings = {
            "Search in subfolders":True,
            "Search only in the root folder":False,
        }
        context["search_subfolders"] = subfolder_mappings[str(self.comboBox.currentText())]

        filename_mappings = {
            "Use only the filename":True,
            "Use the whole relative path":False,
        }
        context["use_filename_only"] = filename_mappings[str(self.comboBox_2.currentText())]



        regex_combo = str(self.comboBox_4.currentText())
        universal_regex = "(.*?)" #Used to match anything
        regex = regex_param

        regex_preset_mappings = {
            "Starts With": "startswith",
            "Ends With": "endswith",
            "Equals": "equals",
            "Contains": "contains",
            "Custom RegEx": "custom",
        }

        context["preset"] = regex_preset_mappings[regex_combo]

        print(context)
        try:
            response = organize_files(src, dest_folder, regex, context)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Operation Finished")
            msg.setInformativeText(response)
            msg.setWindowTitle("Finish")
            msg.exec_()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error occurred during operation")
            msg.setInformativeText('Something went wrong, please make sure everything is set up correctly')
            msg.setWindowTitle("Error")
            msg.exec_()
        return


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(607, 480)
        mainWindow.setWindowIcon(QtGui.QIcon('./frontend/logo.png'))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, 10, 20, 251))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(7, 260, 591, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 100, 361, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 400, 591, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 280, 591, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setAcceptDrops(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_4)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(240, 10, 361, 61))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 10, 191, 241))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.pushButton.clicked.connect(self.set_root_folder)
        self.pushButton_2.clicked.connect(self.set_dest_folder)
        self.pushButton_3.clicked.connect(self.prepare_organize_files)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Regex Organizer"))
        mainWindow.setFixedSize(mainWindow.size())
        self.pushButton_2.setText(_translate("mainWindow", "Pick Destination Folder"))
        self.label_6.setText(_translate("mainWindow", "Destination Folder"))
        self.pushButton_3.setText(_translate("mainWindow", "Organize"))
        self.label_4.setText(_translate("mainWindow", "Regular Expression. Pick one of the common ones or use a custom one:"))
        self.comboBox_4.setItemText(0, _translate("mainWindow", "Starts With"))
        self.comboBox_4.setItemText(1, _translate("mainWindow", "Ends With"))
        self.comboBox_4.setItemText(2, _translate("mainWindow", "Contains"))
        self.comboBox_4.setItemText(3, _translate("mainWindow", "Equals"))
        self.comboBox_4.setItemText(4, _translate("mainWindow", "Custom RegEx"))
        self.pushButton.setText(_translate("mainWindow", "Pick Root Folder"))
        self.label_5.setText(_translate("mainWindow", "Root Folder"))
        self.label.setText(_translate("mainWindow", "Search Subfolders:"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Search in subfolders"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Search only in the root folder"))
        self.label_2.setText(_translate("mainWindow", "Filename to search:"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "Use the whole relative path"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "Use only the filename"))
        self.label_3.setText(_translate("mainWindow", "Move/Copy:"))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "Move"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "Copy"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qss = "./frontend/stylesheet.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
