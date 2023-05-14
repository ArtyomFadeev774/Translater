from PyQt5 import QtWidgets
import googletrans 
import pyperclip
import gtts 
from playsound import playsound
import os

app = QtWidgets.QApplication([])

class MainWindow(QtWidgets.QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.resize(width, height)
        self.setWindowTitle('Translater (by F.A.A. 2023)')
        self.globalHLine = QtWidgets.QHBoxLayout()
        self.globalVLine1 = QtWidgets.QVBoxLayout()
        self.globalVLine2 = QtWidgets.QVBoxLayout()
        self.globalVLine3 = QtWidgets.QVBoxLayout()
        self.textInput = QtWidgets.QPlainTextEdit()
        self.textInput.setStyleSheet("font-size: 20px")
        self.textInput.setPlaceholderText('Введите текст для перевода...')
        self.textOutput = QtWidgets.QPlainTextEdit()
        self.textOutput.setStyleSheet("font-size: 20px")
        self.languageTo = QtWidgets.QComboBox()
        self.languageFrom = QtWidgets.QComboBox()
        self.languageTo.addItems(googletrans.LANGUAGES.values())
        self.languageFrom.addItems(googletrans.LANGUAGES.values())
        self.languageFrom.setCurrentIndex(get_index(googletrans.LANGUAGES.values(), 'russian'))
        self.languageTo.setCurrentIndex(get_index(googletrans.LANGUAGES.values(), 'english'))
        self.buttonCopyInput = QtWidgets.QPushButton('Копировать')
        self.buttonCopyOutput = QtWidgets.QPushButton('Копировать')
        self.buttonTranslate = QtWidgets.QPushButton('->')
        self.buttonTranslate.setStyleSheet("font-size: 20px")
        self.buttonSoundInput = QtWidgets.QPushButton('Озвучить')
        self.buttonSoundOutput = QtWidgets.QPushButton('Озвучить')
        self.buttonClearInput = QtWidgets.QPushButton('Очистить поле ввода')
        self.langGroup1 = QtWidgets.QGroupBox('Язык:')
        self.lang1Layout = QtWidgets.QVBoxLayout()
        self.langGroup2 = QtWidgets.QGroupBox('Язык:')
        self.lang2Layout = QtWidgets.QVBoxLayout()
        self.buttonSelectRus1 = QtWidgets.QPushButton('Выбрать русский')
        self.buttonSelectRus2 = QtWidgets.QPushButton('Выбрать русский')
        self.buttonSelectEn1 = QtWidgets.QPushButton('Выбрать английский')
        self.buttonSelectEn2 = QtWidgets.QPushButton('Выбрать английский')
        #--------закрепление------------:
        self.globalHLine.addLayout(self.globalVLine1)
        self.globalHLine.addLayout(self.globalVLine2)
        self.globalHLine.addLayout(self.globalVLine3)
        #--globalVLine1--
        self.globalVLine1.addWidget(self.textInput)
        self.lang1Layout.addWidget(self.languageFrom)
        self.lang1Layout.addWidget(self.buttonSelectRus1)
        self.lang1Layout.addWidget(self.buttonSelectEn1)
        self.langGroup1.setLayout(self.lang1Layout)
        self.globalVLine1.addWidget(self.langGroup1)
        self.globalVLine1.addWidget(self.buttonCopyInput)
        self.globalVLine1.addWidget(self.buttonSoundInput)
        self.globalVLine1.addWidget(self.buttonClearInput)
        #--globalVLine2--
        self.globalVLine2.addWidget(self.buttonTranslate)
        #--globalVLine3--
        self.globalVLine3.addWidget(self.textOutput)
        self.lang2Layout.addWidget(self.languageTo)
        self.lang2Layout.addWidget(self.buttonSelectRus2)
        self.lang2Layout.addWidget(self.buttonSelectEn2)
        self.langGroup2.setLayout(self.lang2Layout)
        self.globalVLine3.addWidget(self.langGroup2)
        self.globalVLine3.addWidget(self.buttonCopyOutput)
        self.globalVLine3.addWidget(self.buttonSoundOutput)
        #--
        self.setLayout(self.globalHLine)

def get_index(list1, value):
    i = 0
    list1 = list(list1)
    for element in list1:
        if list1[i] == value:
            return i
        i += 1

window = MainWindow(800, 700)
window.show()

def get_key(value):
    for key, j in googletrans.LANGUAGES.items():
        if str(j) == str(value):
            return str(key)

def translate2():
    try:
        text = window.textInput.toPlainText()
        languageInput = get_key(window.languageFrom.currentText())
        languageOutput = get_key(window.languageTo.currentText())
        translator = googletrans.Translator()
        result = translator.translate(text, languageOutput, languageInput)
        window.textOutput.setPlainText(result.text)
    except: pass

def copyleft():
    pyperclip.copy(window.textInput.toPlainText())
    message = QtWidgets.QMessageBox(window)
    message.setWindowTitle('Уведомление')
    message.setText('Текст скопирован в буфер обмена.')
    message.exec_()

def copyright():
    pyperclip.copy(window.textOutput.toPlainText())
    message = QtWidgets.QMessageBox(window)
    message.setWindowTitle('Уведомление')
    message.setText('Текст скопирован в буфер обмена.')
    message.exec_()

def soundleft():
    try:
        text = gtts.gTTS(window.textInput.toPlainText(), lang=get_key(window.languageFrom.currentText()))
        text.save('soundleft.mp3')
        playsound('soundleft.mp3')
        os.remove('soundleft.mp3')
    except: pass

def soundright():
    try:
        text1 = gtts.gTTS(window.textOutput.toPlainText(), lang=get_key(window.languageTo.currentText()))
        text1.save('soundright.mp3')
        playsound('soundright.mp3')
        os.remove('soundright.mp3')
    except: pass

def clearLeft():
    window.textInput.clear()
    window.textOutput.clear()

def selectRus1():
    window.languageFrom.setCurrentIndex(get_index(googletrans.LANGUAGES.values(), 'russian'))

def selectEn1():
    window.languageFrom.setCurrentIndex(get_index(googletrans.LANGUAGES.values(), 'english'))

def selectRus2():
    window.languageTo.setCurrentIndex(get_index(googletrans.LANGUAGES.values(), 'russian'))

def selectEn2():
    window.languageTo.setCurrentIndex(get_index(googletrans.LANGUAGES.values(), 'english'))

window.buttonTranslate.clicked.connect(translate2)
window.buttonCopyInput.clicked.connect(copyleft)
window.buttonCopyOutput.clicked.connect(copyright)
window.buttonSoundInput.clicked.connect(soundleft)
window.buttonSoundOutput.clicked.connect(soundright)
window.buttonClearInput.clicked.connect(clearLeft)
window.buttonSelectRus1.clicked.connect(selectRus1)
window.buttonSelectRus2.clicked.connect(selectRus2)
window.buttonSelectEn1.clicked.connect(selectEn1)
window.buttonSelectEn2.clicked.connect(selectEn2)

app.exec_()