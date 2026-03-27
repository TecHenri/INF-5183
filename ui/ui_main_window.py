# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1000, 700))
        MainWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"        background-color: #2b2b2b;\n"
"        color: #ffffff;\n"
"    }\n"
"\n"
"    QWidget {\n"
"        background-color: #2b2b2b;\n"
"        color: #ffffff;\n"
"        font-family: 'Segoe UI', Arial, sans-serif;\n"
"        font-size: 11pt;\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        background-color: #0078d4;\n"
"        border: none;\n"
"        border-radius: 6px;\n"
"        padding: 8px 16px;\n"
"        font-weight: bold;\n"
"        min-width: 80px;\n"
"        min-height: 30px;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #106ebe;\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #005a9e;\n"
"    }\n"
"\n"
"    QPushButton#btnGenerate {\n"
"        background-color: #16a085;\n"
"    }\n"
"\n"
"    QPushButton#btnGenerate:hover {\n"
"        background-color: #138d75;\n"
"    }\n"
"\n"
"    QPushButton#btnRun {\n"
"        background-color: #e74c3c;\n"
"    }\n"
"\n"
"    QPushButton#btnRun:hover {\n"
"        ba"
                        "ckground-color: #c0392b;\n"
"    }\n"
"\n"
"    QSpinBox, QDoubleSpinBox {\n"
"    	background-color: #404040;\n"
"    	border: 2px solid #555555;\n"
"    	border-radius: 4px;\n"
"    	padding-right: 20px; \n"
"    	min-width: 60px;\n"
"    	color: #ffffff;\n"
"	}\n"
"\n"
"    QSpinBox::up-button, QSpinBox::down-button {\n"
"    	width: 18px;\n"
"    	background-color: #555555;\n"
"    	border: none;\n"
"	}\n"
"\n"
"	QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    	background-color: #0078d4;\n"
"	}\n"
"\n"
"    QComboBox {\n"
"        background-color: #404040;\n"
"        border: 2px solid #555555;\n"
"        border-radius: 4px;\n"
"        padding: 5px;\n"
"        min-width: 150px;\n"
"        color: #ffffff;\n"
"    }\n"
"\n"
"    QComboBox:focus {\n"
"        border-color: #0078d4;\n"
"    }\n"
"\n"
"    QComboBox::drop-down {\n"
"        border: none;\n"
"        width: 20px;\n"
"    }\n"
"\n"
"    QCheckBox {\n"
"        color: #ffffff;\n"
"        spacing: 6px;\n"
"    }\n"
"\n"
"    "
                        "QCheckBox::indicator {\n"
"        width: 16px;\n"
"        height: 16px;\n"
"        border-radius: 3px;\n"
"        border: 2px solid #555555;\n"
"        background-color: #404040;\n"
"    }\n"
"\n"
"    QCheckBox::indicator:checked {\n"
"        background-color: #f39c12;\n"
"        border-color: #f39c12;\n"
"    }\n"
"\n"
"    QCheckBox::indicator:hover {\n"
"        border-color: #f39c12;\n"
"    }\n"
"\n"
"    QTextEdit {\n"
"        background-color: #1e1e1e;\n"
"        border: 1px solid #555555;\n"
"        border-radius: 4px;\n"
"        padding: 10px;\n"
"        font-family: 'Consolas', 'Monaco', monospace;\n"
"        font-size: 10pt;\n"
"        color: #ffffff;\n"
"    }\n"
"\n"
"    QLabel {\n"
"        color: #ffffff;\n"
"        font-weight: 500;\n"
"    }\n"
"\n"
"    QLabel#seedValueDisplay {\n"
"        background-color: #1e1e1e;\n"
"        border: 2px solid #555555;\n"
"        border-radius: 4px;\n"
"        padding: 4px 8px;\n"
"        color: #f39c12;\n"
"        font-family: 'Consol"
                        "as', monospace;\n"
"        font-weight: bold;\n"
"    }\n"
"\n"
"    QLabel#seedValueDisplay:disabled {\n"
"        color: #555555;\n"
"        border-color: #3a3a3a;\n"
"    }\n"
"\n"
"    QGroupBox {\n"
"        font-weight: bold;\n"
"        border: 2px solid #555555;\n"
"        border-radius: 8px;\n"
"        margin-top: 10px;\n"
"        padding-top: 10px;\n"
"    }\n"
"\n"
"    QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 10px;\n"
"        padding: 0 8px 0 8px;\n"
"        color: #0078d4;\n"
"    }\n"
"\n"
"    QProgressBar {\n"
"        border: 1px solid #555555;\n"
"        border-radius: 4px;\n"
"        text-align: center;\n"
"        background-color: #404040;\n"
"        color: #ffffff;\n"
"    }\n"
"\n"
"    QProgressBar::chunk {\n"
"        background-color: #16a085;\n"
"        border-radius: 3px;\n"
"    }\n"
"\n"
"    QFrame#separatorLine {\n"
"        color: #555555;\n"
"        background-color: #555555;\n"
"    }\n"
"   ")
        self.actionNouveau = QAction(MainWindow)
        self.actionNouveau.setObjectName(u"actionNouveau")
        self.actionSauvegarder = QAction(MainWindow)
        self.actionSauvegarder.setObjectName(u"actionSauvegarder")
        self.actionImport_un_cas = QAction(MainWindow)
        self.actionImport_un_cas.setObjectName(u"actionImport_un_cas")
        self.actionAlgorithm_de_recherches = QAction(MainWindow)
        self.actionAlgorithm_de_recherches.setObjectName(u"actionAlgorithm_de_recherches")
        self.actionImporter_un_script = QAction(MainWindow)
        self.actionImporter_un_script.setObjectName(u"actionImporter_un_script")
        self.actionSupprimer_un_cas = QAction(MainWindow)
        self.actionSupprimer_un_cas.setObjectName(u"actionSupprimer_un_cas")
        self.actionRecherche_de_cas = QAction(MainWindow)
        self.actionRecherche_de_cas.setObjectName(u"actionRecherche_de_cas")
        self.actionMode_sombre = QAction(MainWindow)
        self.actionMode_sombre.setObjectName(u"actionMode_sombre")
        self.actionMode_sombre.setCheckable(True)
        self.actionMode_sombre.setChecked(True)
        self.actionZoom = QAction(MainWindow)
        self.actionZoom.setObjectName(u"actionZoom")
        self.actionRaccourcis = QAction(MainWindow)
        self.actionRaccourcis.setObjectName(u"actionRaccourcis")
        self.actionA_propos = QAction(MainWindow)
        self.actionA_propos.setObjectName(u"actionA_propos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainHorizontalLayout = QHBoxLayout(self.centralwidget)
        self.mainHorizontalLayout.setSpacing(15)
        self.mainHorizontalLayout.setObjectName(u"mainHorizontalLayout")
        self.mainHorizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.leftPanel = QWidget(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMaximumSize(QSize(300, 16777215))
        self.leftPanelLayout = QVBoxLayout(self.leftPanel)
        self.leftPanelLayout.setSpacing(12)
        self.leftPanelLayout.setObjectName(u"leftPanelLayout")
        self.generationGroup = QGroupBox(self.leftPanel)
        self.generationGroup.setObjectName(u"generationGroup")
        self.generationFormLayout = QFormLayout(self.generationGroup)
        self.generationFormLayout.setObjectName(u"generationFormLayout")
        self.generationFormLayout.setHorizontalSpacing(12)
        self.generationFormLayout.setVerticalSpacing(10)
        self.generationFormLayout.setContentsMargins(10, -1, 10, 12)
        self.labelSize = QLabel(self.generationGroup)
        self.labelSize.setObjectName(u"labelSize")
        self.labelSize.setStyleSheet(u"...")

        self.generationFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelSize)

        self.spinBoxSize = QSpinBox(self.generationGroup)
        self.spinBoxSize.setObjectName(u"spinBoxSize")
        self.spinBoxSize.setStyleSheet(u"	QSpinBox::up-arrow {\n"
"    	image: url(:/icons/up.png);\n"
"	}\n"
"\n"
"	QSpinBox::down-arrow {\n"
"    	image: url(:/icons/down.png);\n"
"	}")
        self.spinBoxSize.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxSize.setMinimum(2)
        self.spinBoxSize.setMaximum(30)
        self.spinBoxSize.setValue(16)

        self.generationFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBoxSize)

        self.separatorLine1 = QFrame(self.generationGroup)
        self.separatorLine1.setObjectName(u"separatorLine1")
        self.separatorLine1.setStyleSheet(u"background-color: #444444; max-height: 1px;")
        self.separatorLine1.setFrameShape(QFrame.HLine)
        self.separatorLine1.setFrameShadow(QFrame.Sunken)

        self.generationFormLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.separatorLine1)

        self.labelFillRate = QLabel(self.generationGroup)
        self.labelFillRate.setObjectName(u"labelFillRate")

        self.generationFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelFillRate)

        self.fillRateLayout = QHBoxLayout()
        self.fillRateLayout.setObjectName(u"fillRateLayout")
        self.spinBoxFillRate = QSpinBox(self.generationGroup)
        self.spinBoxFillRate.setObjectName(u"spinBoxFillRate")
        self.spinBoxFillRate.setStyleSheet(u"")
        self.spinBoxFillRate.setMinimum(0)
        self.spinBoxFillRate.setMaximum(100)
        self.spinBoxFillRate.setSingleStep(5)
        self.spinBoxFillRate.setValue(50)

        self.fillRateLayout.addWidget(self.spinBoxFillRate)


        self.generationFormLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.fillRateLayout)

        self.separatorLine2 = QFrame(self.generationGroup)
        self.separatorLine2.setObjectName(u"separatorLine2")
        self.separatorLine2.setStyleSheet(u"background-color: #444444; max-height: 1px;")
        self.separatorLine2.setFrameShape(QFrame.HLine)
        self.separatorLine2.setFrameShadow(QFrame.Sunken)

        self.generationFormLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.separatorLine2)

        self.checkBoxSeed = QCheckBox(self.generationGroup)
        self.checkBoxSeed.setObjectName(u"checkBoxSeed")
        self.checkBoxSeed.setChecked(False)

        self.generationFormLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.checkBoxSeed)

        self.spinBoxSeed = QSpinBox(self.generationGroup)
        self.spinBoxSeed.setObjectName(u"spinBoxSeed")
        self.spinBoxSeed.setEnabled(False)
        self.spinBoxSeed.setMinimum(0)
        self.spinBoxSeed.setMaximum(999999)
        self.spinBoxSeed.setValue(42)

        self.generationFormLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spinBoxSeed)

        self.seedStatusLabel = QLabel(self.generationGroup)
        self.seedStatusLabel.setObjectName(u"seedStatusLabel")
        self.seedStatusLabel.setStyleSheet(u"\n"
"              color: #777777;\n"
"              font-size: 9pt;\n"
"              font-style: italic;\n"
"              padding: 3px;\n"
"              border: 1px solid #3a3a3a;\n"
"              border-radius: 4px;\n"
"              background-color: #222222;\n"
"             ")
        self.seedStatusLabel.setAlignment(Qt.AlignCenter)

        self.generationFormLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.seedStatusLabel)

        self.btnGenerate = QPushButton(self.generationGroup)
        self.btnGenerate.setObjectName(u"btnGenerate")

        self.generationFormLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.btnGenerate)


        self.leftPanelLayout.addWidget(self.generationGroup)

        self.algorithmGroup = QGroupBox(self.leftPanel)
        self.algorithmGroup.setObjectName(u"algorithmGroup")
        self.algorithmLayout = QVBoxLayout(self.algorithmGroup)
        self.algorithmLayout.setSpacing(8)
        self.algorithmLayout.setObjectName(u"algorithmLayout")
        self.algorithmLayout.setContentsMargins(10, -1, 10, 12)
        self.comboAlgo = QComboBox(self.algorithmGroup)
        self.comboAlgo.addItem("")
        self.comboAlgo.addItem("")
        self.comboAlgo.addItem("")
        self.comboAlgo.setObjectName(u"comboAlgo")

        self.algorithmLayout.addWidget(self.comboAlgo)

        self.btnRun = QPushButton(self.algorithmGroup)
        self.btnRun.setObjectName(u"btnRun")

        self.algorithmLayout.addWidget(self.btnRun)

        self.progressBar = QProgressBar(self.algorithmGroup)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)

        self.algorithmLayout.addWidget(self.progressBar)


        self.leftPanelLayout.addWidget(self.algorithmGroup)

        self.statsGroup = QGroupBox(self.leftPanel)
        self.statsGroup.setObjectName(u"statsGroup")
        self.statsFormLayout = QFormLayout(self.statsGroup)
        self.statsFormLayout.setObjectName(u"statsFormLayout")
        self.statsFormLayout.setHorizontalSpacing(12)
        self.statsFormLayout.setVerticalSpacing(8)
        self.statsFormLayout.setContentsMargins(10, -1, 10, 12)
        self.labelCells = QLabel(self.statsGroup)
        self.labelCells.setObjectName(u"labelCells")

        self.statsFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelCells)

        self.valueCells = QLabel(self.statsGroup)
        self.valueCells.setObjectName(u"valueCells")
        self.valueCells.setStyleSheet(u"color: #16a085; font-weight: bold;")

        self.statsFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.valueCells)

        self.labelPath = QLabel(self.statsGroup)
        self.labelPath.setObjectName(u"labelPath")

        self.statsFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelPath)

        self.valuePath = QLabel(self.statsGroup)
        self.valuePath.setObjectName(u"valuePath")
        self.valuePath.setStyleSheet(u"color: #e74c3c; font-weight: bold;")

        self.statsFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.valuePath)

        self.labelTime = QLabel(self.statsGroup)
        self.labelTime.setObjectName(u"labelTime")

        self.statsFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelTime)

        self.valueTime = QLabel(self.statsGroup)
        self.valueTime.setObjectName(u"valueTime")
        self.valueTime.setStyleSheet(u"color: #f39c12; font-weight: bold;")

        self.statsFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.valueTime)


        self.leftPanelLayout.addWidget(self.statsGroup)

        self.leftVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftPanelLayout.addItem(self.leftVerticalSpacer)


        self.mainHorizontalLayout.addWidget(self.leftPanel)

        self.centerPanel = QWidget(self.centralwidget)
        self.centerPanel.setObjectName(u"centerPanel")
        self.centerPanelLayout = QVBoxLayout(self.centerPanel)
        self.centerPanelLayout.setObjectName(u"centerPanelLayout")
        self.titleLabel = QLabel(self.centerPanel)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"\n"
"           font-size: 16pt;\n"
"           font-weight: bold;\n"
"           color: #0078d4;\n"
"           margin-bottom: 10px;\n"
"          ")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.centerPanelLayout.addWidget(self.titleLabel)

        self.scrollArea = QScrollArea(self.centerPanel)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"\n"
"           QScrollArea {\n"
"               border: 2px solid #555555;\n"
"               border-radius: 8px;\n"
"               background-color: #1e1e1e;\n"
"           }\n"
"          ")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 831, 447))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.centerPanelLayout.addWidget(self.scrollArea)

        self.logGroup = QGroupBox(self.centerPanel)
        self.logGroup.setObjectName(u"logGroup")
        self.logGroup.setMaximumSize(QSize(16777215, 200))
        self.logLayout = QVBoxLayout(self.logGroup)
        self.logLayout.setObjectName(u"logLayout")
        self.textLog = QTextEdit(self.logGroup)
        self.textLog.setObjectName(u"textLog")
        self.textLog.setReadOnly(True)

        self.logLayout.addWidget(self.textLog)


        self.centerPanelLayout.addWidget(self.logGroup)


        self.mainHorizontalLayout.addWidget(self.centerPanel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 36))
        self.menubar.setStyleSheet(u"\n"
"     QMenuBar {\n"
"         background-color: #404040;\n"
"         color: white;\n"
"         border-bottom: 1px solid #555555;\n"
"     }\n"
"     QMenuBar::item {\n"
"         padding: 5px 15px;\n"
"         background-color: transparent;\n"
"     }\n"
"     QMenuBar::item:selected {\n"
"         background-color: #0078d4;\n"
"     }\n"
"     QMenu {\n"
"         background-color: #404040;\n"
"         border: 1px solid #555555;\n"
"     }\n"
"     QMenu::item {\n"
"         padding: 8px 25px;\n"
"     }\n"
"     QMenu::item:selected {\n"
"         background-color: #0078d4;\n"
"     }\n"
"     QMenu::separator {\n"
"         height: 1px;\n"
"         background-color: #555555;\n"
"         margin: 4px 10px;\n"
"     }\n"
"    ")
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuEditer = QMenu(self.menubar)
        self.menuEditer.setObjectName(u"menuEditer")
        self.menuAffichage = QMenu(self.menubar)
        self.menuAffichage.setObjectName(u"menuAffichage")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuEditer.menuAction())
        self.menubar.addAction(self.menuAffichage.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionSauvegarder)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionImport_un_cas)
        self.menuFichier.addAction(self.actionSupprimer_un_cas)
        self.menuEditer.addAction(self.actionAlgorithm_de_recherches)
        self.menuEditer.addAction(self.actionImporter_un_script)
        self.menuEditer.addSeparator()
        self.menuEditer.addAction(self.actionRecherche_de_cas)
        self.menuAffichage.addAction(self.actionMode_sombre)
        self.menuAffichage.addAction(self.actionZoom)
        self.menuInfo.addAction(self.actionRaccourcis)
        self.menuInfo.addAction(self.actionA_propos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\U0001f500 LABYRINTHE - G\U000000e9n\U000000e9rateur & Solveur", None))
        self.actionNouveau.setText(QCoreApplication.translate("MainWindow", u"\U0001f195  Nouveau Labyrinthe", None))
#if QT_CONFIG(shortcut)
        self.actionNouveau.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionSauvegarder.setText(QCoreApplication.translate("MainWindow", u"\U0001f4be  Sauvegarder", None))
#if QT_CONFIG(shortcut)
        self.actionSauvegarder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionImport_un_cas.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c2  Importer un cas...", None))
#if QT_CONFIG(shortcut)
        self.actionImport_un_cas.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAlgorithm_de_recherches.setText(QCoreApplication.translate("MainWindow", u"\U0001f50d  Configurer Algorithmes", None))
        self.actionImporter_un_script.setText(QCoreApplication.translate("MainWindow", u"\U0001f4dc  Importer Script Personnalis\U000000e9", None))
        self.actionSupprimer_un_cas.setText(QCoreApplication.translate("MainWindow", u"\U0001f5d1\U0000fe0f  Supprimer un cas", None))
#if QT_CONFIG(shortcut)
        self.actionSupprimer_un_cas.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecherche_de_cas.setText(QCoreApplication.translate("MainWindow", u"\U0001f50e  Recherche de cas", None))
#if QT_CONFIG(shortcut)
        self.actionRecherche_de_cas.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionMode_sombre.setText(QCoreApplication.translate("MainWindow", u"\U0001f319  Basculer Mode Sombre", None))
        self.actionZoom.setText(QCoreApplication.translate("MainWindow", u"\U0001f50d  Contr\U000000f4les Zoom", None))
        self.actionRaccourcis.setText(QCoreApplication.translate("MainWindow", u"\u2328\ufe0f  Raccourcis Clavier", None))
#if QT_CONFIG(shortcut)
        self.actionRaccourcis.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionA_propos.setText(QCoreApplication.translate("MainWindow", u"\u2139\ufe0f  \u00c0 Propos", None))
        self.generationGroup.setTitle(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f  G\u00e9n\u00e9ration", None))
        self.labelSize.setText(QCoreApplication.translate("MainWindow", u"Taille (n \u00d7 n) :", None))
        self.spinBoxSize.setSuffix(QCoreApplication.translate("MainWindow", u" x ", None))
#if QT_CONFIG(tooltip)
        self.labelFillRate.setToolTip(QCoreApplication.translate("MainWindow", u"Taux de remplissage des murs du labyrinthe (en %)", None))
#endif // QT_CONFIG(tooltip)
        self.labelFillRate.setText(QCoreApplication.translate("MainWindow", u"Fill Rate :", None))
#if QT_CONFIG(tooltip)
        self.spinBoxFillRate.setToolTip(QCoreApplication.translate("MainWindow", u"Taux de remplissage des murs (0% = vide, 100% = plein)", None))
#endif // QT_CONFIG(tooltip)
        self.spinBoxFillRate.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSeed.setToolTip(QCoreApplication.translate("MainWindow", u"Cochez pour fixer un seed et obtenir un labyrinthe reproductible", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSeed.setText(QCoreApplication.translate("MainWindow", u"Seed fixe :", None))
#if QT_CONFIG(tooltip)
        self.spinBoxSeed.setToolTip(QCoreApplication.translate("MainWindow", u"Valeur du seed (activ\u00e9 uniquement si la case est coch\u00e9e)", None))
#endif // QT_CONFIG(tooltip)
        self.seedStatusLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b2 Seed : al\U000000e9atoire", None))
        self.btnGenerate.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b2  G\U000000e9n\U000000e9rer le Labyrinthe", None))
#if QT_CONFIG(shortcut)
        self.btnGenerate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.algorithmGroup.setTitle(QCoreApplication.translate("MainWindow", u"\U0001f50d  Algorithme de R\U000000e9solution", None))
        self.comboAlgo.setItemText(0, QCoreApplication.translate("MainWindow", u"BFS \u2014 Largeur d'abord", None))
        self.comboAlgo.setItemText(1, QCoreApplication.translate("MainWindow", u"DFS \u2014 Profondeur d'abord", None))
        self.comboAlgo.setItemText(2, QCoreApplication.translate("MainWindow", u"A* \u2014 A-Star", None))

        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"\U0001f680  R\U000000e9soudre", None))
#if QT_CONFIG(shortcut)
        self.btnRun.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.statsGroup.setTitle(QCoreApplication.translate("MainWindow", u"\U0001f4ca  Statistiques", None))
        self.labelCells.setText(QCoreApplication.translate("MainWindow", u"Cellules visit\u00e9es :", None))
        self.valueCells.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelPath.setText(QCoreApplication.translate("MainWindow", u"Longueur du chemin :", None))
        self.valuePath.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelTime.setText(QCoreApplication.translate("MainWindow", u"Temps d'ex\u00e9cution :", None))
        self.valueTime.setText(QCoreApplication.translate("MainWindow", u"0.00 s", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f500  Visualisation du Labyrinthe", None))
        self.logGroup.setTitle(QCoreApplication.translate("MainWindow", u"\U0001f4dd  Journal d'Ex\U000000e9cution", None))
        self.textLog.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas,Monaco,monospace'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#16a085;\">[INFO]</span> Interface initialis\u00e9e. Pr\u00eat \u00e0 g\u00e9n\u00e9rer un labyrinthe...</p></body></html>", None))
        self.textLog.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Les logs et \u00e9tapes d'ex\u00e9cution appara\u00eetront ici...", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"\U0001f4c1  Fichier", None))
        self.menuEditer.setTitle(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f  Algorithmes", None))
        self.menuAffichage.setTitle(QCoreApplication.translate("MainWindow", u"\U0001f441\U0000fe0f  Affichage", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"\u2139\ufe0f  Aide", None))
    # retranslateUi

