# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pcba_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 678)
        self.res_poe1 = QtWidgets.QLabel(Form)
        self.res_poe1.setGeometry(QtCore.QRect(140, 200, 161, 21))
        self.res_poe1.setFrameShape(QtWidgets.QFrame.Box)
        self.res_poe1.setAlignment(QtCore.Qt.AlignCenter)
        self.res_poe1.setObjectName("res_poe1")
        self.lab_ir10 = QtWidgets.QLabel(Form)
        self.lab_ir10.setGeometry(QtCore.QRect(320, 110, 91, 21))
        self.lab_ir10.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir10.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir10.setObjectName("lab_ir10")
        self.lab_tp28 = QtWidgets.QLabel(Form)
        self.lab_tp28.setGeometry(QtCore.QRect(40, 140, 91, 21))
        self.lab_tp28.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_tp28.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_tp28.setObjectName("lab_tp28")
        self.btn_ir = QtWidgets.QPushButton(Form)
        self.btn_ir.setGeometry(QtCore.QRect(40, 350, 261, 21))
        self.btn_ir.setObjectName("btn_ir")
        self.edit_wifimac = QtWidgets.QLineEdit(Form)
        self.edit_wifimac.setGeometry(QtCore.QRect(670, 290, 191, 21))
        self.edit_wifimac.setText("")
        self.edit_wifimac.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_wifimac.setObjectName("edit_wifimac")
        self.res_iperfeth = QtWidgets.QLabel(Form)
        self.res_iperfeth.setGeometry(QtCore.QRect(690, 200, 171, 21))
        self.res_iperfeth.setFrameShape(QtWidgets.QFrame.Box)
        self.res_iperfeth.setAlignment(QtCore.Qt.AlignCenter)
        self.res_iperfeth.setObjectName("res_iperfeth")
        self.edit_ethmac = QtWidgets.QLineEdit(Form)
        self.edit_ethmac.setGeometry(QtCore.QRect(670, 260, 191, 21))
        self.edit_ethmac.setText("")
        self.edit_ethmac.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_ethmac.setObjectName("edit_ethmac")
        self.lab_ir2 = QtWidgets.QLabel(Form)
        self.lab_ir2.setGeometry(QtCore.QRect(40, 410, 91, 21))
        self.lab_ir2.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir2.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir2.setObjectName("lab_ir2")
        self.lab_ir6 = QtWidgets.QLabel(Form)
        self.lab_ir6.setGeometry(QtCore.QRect(40, 530, 91, 21))
        self.lab_ir6.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir6.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir6.setObjectName("lab_ir6")
        self.res_ir11 = QtWidgets.QLabel(Form)
        self.res_ir11.setGeometry(QtCore.QRect(420, 140, 161, 21))
        self.res_ir11.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir11.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir11.setObjectName("res_ir11")
        self.btn_reset = QtWidgets.QPushButton(Form)
        self.btn_reset.setGeometry(QtCore.QRect(590, 620, 271, 21))
        self.btn_reset.setObjectName("btn_reset")
        self.lab_ir8 = QtWidgets.QLabel(Form)
        self.lab_ir8.setGeometry(QtCore.QRect(40, 590, 91, 21))
        self.lab_ir8.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir8.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir8.setObjectName("lab_ir8")
        self.btn_wifipower = QtWidgets.QPushButton(Form)
        self.btn_wifipower.setGeometry(QtCore.QRect(590, 170, 91, 21))
        self.btn_wifipower.setObjectName("btn_wifipower")
        self.res_ir1 = QtWidgets.QLabel(Form)
        self.res_ir1.setGeometry(QtCore.QRect(140, 380, 161, 21))
        self.res_ir1.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir1.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir1.setObjectName("res_ir1")
        self.res_sense3 = QtWidgets.QLabel(Form)
        self.res_sense3.setGeometry(QtCore.QRect(420, 320, 161, 21))
        self.res_sense3.setFrameShape(QtWidgets.QFrame.Box)
        self.res_sense3.setAlignment(QtCore.Qt.AlignCenter)
        self.res_sense3.setObjectName("res_sense3")
        self.lab_rs23248 = QtWidgets.QLabel(Form)
        self.lab_rs23248.setGeometry(QtCore.QRect(320, 500, 91, 21))
        self.lab_rs23248.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_rs23248.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_rs23248.setObjectName("lab_rs23248")
        self.btn_iperfeth = QtWidgets.QPushButton(Form)
        self.btn_iperfeth.setGeometry(QtCore.QRect(590, 200, 91, 21))
        self.btn_iperfeth.setObjectName("btn_iperfeth")
        self.edit_snscan = QtWidgets.QLineEdit(Form)
        self.edit_snscan.setGeometry(QtCore.QRect(140, 80, 441, 21))
        self.edit_snscan.setText("")
        self.edit_snscan.setMaxLength(18)
        self.edit_snscan.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_snscan.setObjectName("edit_snscan")
        self.lab_dc1 = QtWidgets.QLabel(Form)
        self.lab_dc1.setGeometry(QtCore.QRect(40, 170, 91, 21))
        self.lab_dc1.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_dc1.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_dc1.setObjectName("lab_dc1")
        self.btn_sense = QtWidgets.QPushButton(Form)
        self.btn_sense.setGeometry(QtCore.QRect(320, 230, 261, 21))
        self.btn_sense.setObjectName("btn_sense")
        self.res_tp28 = QtWidgets.QLabel(Form)
        self.res_tp28.setGeometry(QtCore.QRect(140, 140, 161, 21))
        self.res_tp28.setFrameShape(QtWidgets.QFrame.Box)
        self.res_tp28.setAlignment(QtCore.Qt.AlignCenter)
        self.res_tp28.setObjectName("res_tp28")
        self.res_usb3 = QtWidgets.QLabel(Form)
        self.res_usb3.setGeometry(QtCore.QRect(690, 140, 171, 21))
        self.res_usb3.setFrameShape(QtWidgets.QFrame.Box)
        self.res_usb3.setAlignment(QtCore.Qt.AlignCenter)
        self.res_usb3.setObjectName("res_usb3")
        self.res_ir12 = QtWidgets.QLabel(Form)
        self.res_ir12.setGeometry(QtCore.QRect(420, 170, 161, 21))
        self.res_ir12.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir12.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir12.setObjectName("res_ir12")
        self.btn_vol = QtWidgets.QPushButton(Form)
        self.btn_vol.setGeometry(QtCore.QRect(40, 110, 261, 21))
        self.btn_vol.setObjectName("btn_vol")
        self.res_wifipower = QtWidgets.QLabel(Form)
        self.res_wifipower.setGeometry(QtCore.QRect(690, 170, 171, 21))
        self.res_wifipower.setFrameShape(QtWidgets.QFrame.Box)
        self.res_wifipower.setAlignment(QtCore.Qt.AlignCenter)
        self.res_wifipower.setObjectName("res_wifipower")
        self.res_led = QtWidgets.QLabel(Form)
        self.res_led.setGeometry(QtCore.QRect(690, 380, 171, 21))
        self.res_led.setFrameShape(QtWidgets.QFrame.Box)
        self.res_led.setAlignment(QtCore.Qt.AlignCenter)
        self.res_led.setObjectName("res_led")
        self.res_hdmi = QtWidgets.QLabel(Form)
        self.res_hdmi.setGeometry(QtCore.QRect(690, 410, 171, 21))
        self.res_hdmi.setFrameShape(QtWidgets.QFrame.Box)
        self.res_hdmi.setAlignment(QtCore.Qt.AlignCenter)
        self.res_hdmi.setObjectName("res_hdmi")
        self.btn_inforw = QtWidgets.QPushButton(Form)
        self.btn_inforw.setGeometry(QtCore.QRect(590, 230, 91, 21))
        self.btn_inforw.setObjectName("btn_inforw")
        self.lab_ir11 = QtWidgets.QLabel(Form)
        self.lab_ir11.setGeometry(QtCore.QRect(320, 140, 91, 21))
        self.lab_ir11.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir11.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir11.setObjectName("lab_ir11")
        self.res_ir10 = QtWidgets.QLabel(Form)
        self.res_ir10.setGeometry(QtCore.QRect(420, 110, 161, 21))
        self.res_ir10.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir10.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir10.setObjectName("res_ir10")
        self.lab_rs23226 = QtWidgets.QLabel(Form)
        self.lab_rs23226.setGeometry(QtCore.QRect(320, 440, 91, 21))
        self.lab_rs23226.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_rs23226.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_rs23226.setObjectName("lab_rs23226")
        self.res_rstbtn = QtWidgets.QLabel(Form)
        self.res_rstbtn.setGeometry(QtCore.QRect(690, 440, 171, 21))
        self.res_rstbtn.setFrameShape(QtWidgets.QFrame.Box)
        self.res_rstbtn.setAlignment(QtCore.Qt.AlignCenter)
        self.res_rstbtn.setObjectName("res_rstbtn")
        self.res_amp = QtWidgets.QLabel(Form)
        self.res_amp.setGeometry(QtCore.QRect(420, 620, 161, 21))
        self.res_amp.setFrameShape(QtWidgets.QFrame.Box)
        self.res_amp.setAlignment(QtCore.Qt.AlignCenter)
        self.res_amp.setObjectName("res_amp")
        self.res_usb2 = QtWidgets.QLabel(Form)
        self.res_usb2.setGeometry(QtCore.QRect(690, 110, 171, 21))
        self.res_usb2.setFrameShape(QtWidgets.QFrame.Box)
        self.res_usb2.setAlignment(QtCore.Qt.AlignCenter)
        self.res_usb2.setObjectName("res_usb2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 621, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lab_poe1 = QtWidgets.QLabel(Form)
        self.lab_poe1.setGeometry(QtCore.QRect(40, 200, 91, 21))
        self.lab_poe1.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_poe1.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_poe1.setObjectName("lab_poe1")
        self.lab_sense4 = QtWidgets.QLabel(Form)
        self.lab_sense4.setGeometry(QtCore.QRect(320, 350, 91, 21))
        self.lab_sense4.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_sense4.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_sense4.setObjectName("lab_sense4")
        self.lab_ir4 = QtWidgets.QLabel(Form)
        self.lab_ir4.setGeometry(QtCore.QRect(40, 470, 91, 21))
        self.lab_ir4.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir4.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir4.setObjectName("lab_ir4")
        self.res_ir5 = QtWidgets.QLabel(Form)
        self.res_ir5.setGeometry(QtCore.QRect(140, 500, 161, 21))
        self.res_ir5.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir5.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir5.setObjectName("res_ir5")
        self.res_sense1 = QtWidgets.QLabel(Form)
        self.res_sense1.setGeometry(QtCore.QRect(420, 260, 161, 21))
        self.res_sense1.setFrameShape(QtWidgets.QFrame.Box)
        self.res_sense1.setAlignment(QtCore.Qt.AlignCenter)
        self.res_sense1.setObjectName("res_sense1")
        self.res_rs23215 = QtWidgets.QLabel(Form)
        self.res_rs23215.setGeometry(QtCore.QRect(420, 410, 161, 21))
        self.res_rs23215.setFrameShape(QtWidgets.QFrame.Box)
        self.res_rs23215.setAlignment(QtCore.Qt.AlignCenter)
        self.res_rs23215.setObjectName("res_rs23215")
        self.lab_ir3 = QtWidgets.QLabel(Form)
        self.lab_ir3.setGeometry(QtCore.QRect(40, 440, 91, 21))
        self.lab_ir3.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir3.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir3.setObjectName("lab_ir3")
        self.lab_sense2 = QtWidgets.QLabel(Form)
        self.lab_sense2.setGeometry(QtCore.QRect(320, 290, 91, 21))
        self.lab_sense2.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_sense2.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_sense2.setObjectName("lab_sense2")
        self.res_ir3 = QtWidgets.QLabel(Form)
        self.res_ir3.setGeometry(QtCore.QRect(140, 440, 161, 21))
        self.res_ir3.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir3.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir3.setObjectName("res_ir3")
        self.lab_ir7 = QtWidgets.QLabel(Form)
        self.lab_ir7.setGeometry(QtCore.QRect(40, 560, 91, 21))
        self.lab_ir7.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir7.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir7.setObjectName("lab_ir7")
        self.res_rs23248 = QtWidgets.QLabel(Form)
        self.res_rs23248.setGeometry(QtCore.QRect(420, 500, 161, 21))
        self.res_rs23248.setFrameShape(QtWidgets.QFrame.Box)
        self.res_rs23248.setAlignment(QtCore.Qt.AlignCenter)
        self.res_rs23248.setObjectName("res_rs23248")
        self.lab_ir12 = QtWidgets.QLabel(Form)
        self.lab_ir12.setGeometry(QtCore.QRect(320, 170, 91, 21))
        self.lab_ir12.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir12.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir12.setObjectName("lab_ir12")
        self.res_thd = QtWidgets.QLabel(Form)
        self.res_thd.setGeometry(QtCore.QRect(420, 590, 161, 21))
        self.res_thd.setFrameShape(QtWidgets.QFrame.Box)
        self.res_thd.setAlignment(QtCore.Qt.AlignCenter)
        self.res_thd.setObjectName("res_thd")
        self.lab_ir1 = QtWidgets.QLabel(Form)
        self.lab_ir1.setGeometry(QtCore.QRect(40, 380, 91, 21))
        self.lab_ir1.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir1.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir1.setObjectName("lab_ir1")
        self.res_dc1 = QtWidgets.QLabel(Form)
        self.res_dc1.setGeometry(QtCore.QRect(140, 170, 161, 21))
        self.res_dc1.setFrameShape(QtWidgets.QFrame.Box)
        self.res_dc1.setAlignment(QtCore.Qt.AlignCenter)
        self.res_dc1.setObjectName("res_dc1")
        self.btn_usb2 = QtWidgets.QPushButton(Form)
        self.btn_usb2.setGeometry(QtCore.QRect(590, 110, 91, 21))
        self.btn_usb2.setObjectName("btn_usb2")
        self.btn_rs485 = QtWidgets.QPushButton(Form)
        self.btn_rs485.setGeometry(QtCore.QRect(320, 200, 91, 21))
        self.btn_rs485.setObjectName("btn_rs485")
        self.lab_amp = QtWidgets.QLabel(Form)
        self.lab_amp.setGeometry(QtCore.QRect(320, 620, 91, 21))
        self.lab_amp.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_amp.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_amp.setObjectName("lab_amp")
        self.lab_sense3 = QtWidgets.QLabel(Form)
        self.lab_sense3.setGeometry(QtCore.QRect(320, 320, 91, 21))
        self.lab_sense3.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_sense3.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_sense3.setObjectName("lab_sense3")
        self.res_ir6 = QtWidgets.QLabel(Form)
        self.res_ir6.setGeometry(QtCore.QRect(140, 530, 161, 21))
        self.res_ir6.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir6.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir6.setObjectName("res_ir6")
        self.res_sense4 = QtWidgets.QLabel(Form)
        self.res_sense4.setGeometry(QtCore.QRect(420, 350, 161, 21))
        self.res_sense4.setFrameShape(QtWidgets.QFrame.Box)
        self.res_sense4.setAlignment(QtCore.Qt.AlignCenter)
        self.res_sense4.setObjectName("res_sense4")
        self.res_ir4 = QtWidgets.QLabel(Form)
        self.res_ir4.setGeometry(QtCore.QRect(140, 470, 161, 21))
        self.res_ir4.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir4.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir4.setObjectName("res_ir4")
        self.lab_ir5 = QtWidgets.QLabel(Form)
        self.lab_ir5.setGeometry(QtCore.QRect(40, 500, 91, 21))
        self.lab_ir5.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir5.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir5.setObjectName("lab_ir5")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(40, 40, 621, 21))
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.res_rs23237 = QtWidgets.QLabel(Form)
        self.res_rs23237.setGeometry(QtCore.QRect(420, 470, 161, 21))
        self.res_rs23237.setFrameShape(QtWidgets.QFrame.Box)
        self.res_rs23237.setAlignment(QtCore.Qt.AlignCenter)
        self.res_rs23237.setObjectName("res_rs23237")
        self.res_rs23226 = QtWidgets.QLabel(Form)
        self.res_rs23226.setGeometry(QtCore.QRect(420, 440, 161, 21))
        self.res_rs23226.setFrameShape(QtWidgets.QFrame.Box)
        self.res_rs23226.setAlignment(QtCore.Qt.AlignCenter)
        self.res_rs23226.setObjectName("res_rs23226")
        self.btn_usb3 = QtWidgets.QPushButton(Form)
        self.btn_usb3.setGeometry(QtCore.QRect(590, 140, 91, 21))
        self.btn_usb3.setObjectName("btn_usb3")
        self.btn_auto = QtWidgets.QPushButton(Form)
        self.btn_auto.setGeometry(QtCore.QRect(590, 530, 271, 21))
        self.btn_auto.setObjectName("btn_auto")
        self.res_ir8 = QtWidgets.QLabel(Form)
        self.res_ir8.setGeometry(QtCore.QRect(140, 590, 161, 21))
        self.res_ir8.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir8.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir8.setObjectName("res_ir8")
        self.res_inforw = QtWidgets.QLabel(Form)
        self.res_inforw.setGeometry(QtCore.QRect(690, 230, 171, 21))
        self.res_inforw.setFrameShape(QtWidgets.QFrame.Box)
        self.res_inforw.setAlignment(QtCore.Qt.AlignCenter)
        self.res_inforw.setObjectName("res_inforw")
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(40, 230, 91, 21))
        self.btn_login.setObjectName("btn_login")
        self.lab_sense1 = QtWidgets.QLabel(Form)
        self.lab_sense1.setGeometry(QtCore.QRect(320, 260, 91, 21))
        self.lab_sense1.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_sense1.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_sense1.setObjectName("lab_sense1")
        self.res_ir7 = QtWidgets.QLabel(Form)
        self.res_ir7.setGeometry(QtCore.QRect(140, 560, 161, 21))
        self.res_ir7.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir7.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir7.setObjectName("res_ir7")
        self.lab_rs23237 = QtWidgets.QLabel(Form)
        self.lab_rs23237.setGeometry(QtCore.QRect(320, 470, 91, 21))
        self.lab_rs23237.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_rs23237.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_rs23237.setObjectName("lab_rs23237")
        self.res_relay = QtWidgets.QLabel(Form)
        self.res_relay.setGeometry(QtCore.QRect(420, 530, 161, 21))
        self.res_relay.setFrameShape(QtWidgets.QFrame.Box)
        self.res_relay.setAlignment(QtCore.Qt.AlignCenter)
        self.res_relay.setObjectName("res_relay")
        self.lab_rs23215 = QtWidgets.QLabel(Form)
        self.lab_rs23215.setGeometry(QtCore.QRect(320, 410, 91, 21))
        self.lab_rs23215.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_rs23215.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_rs23215.setObjectName("lab_rs23215")
        self.btn_submit = QtWidgets.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(590, 560, 271, 21))
        self.btn_submit.setObjectName("btn_submit")
        self.res_rs485 = QtWidgets.QLabel(Form)
        self.res_rs485.setGeometry(QtCore.QRect(420, 200, 161, 21))
        self.res_rs485.setFrameShape(QtWidgets.QFrame.Box)
        self.res_rs485.setAlignment(QtCore.Qt.AlignCenter)
        self.res_rs485.setObjectName("res_rs485")
        self.btn_relay = QtWidgets.QPushButton(Form)
        self.btn_relay.setGeometry(QtCore.QRect(320, 530, 91, 21))
        self.btn_relay.setObjectName("btn_relay")
        self.res_ir2 = QtWidgets.QLabel(Form)
        self.res_ir2.setGeometry(QtCore.QRect(140, 410, 161, 21))
        self.res_ir2.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir2.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir2.setObjectName("res_ir2")
        self.btn_printer = QtWidgets.QPushButton(Form)
        self.btn_printer.setGeometry(QtCore.QRect(590, 590, 271, 21))
        self.btn_printer.setObjectName("btn_printer")
        self.btn_rs232 = QtWidgets.QPushButton(Form)
        self.btn_rs232.setGeometry(QtCore.QRect(320, 380, 261, 21))
        self.btn_rs232.setObjectName("btn_rs232")
        self.res_login = QtWidgets.QLabel(Form)
        self.res_login.setGeometry(QtCore.QRect(140, 230, 161, 21))
        self.res_login.setFrameShape(QtWidgets.QFrame.Box)
        self.res_login.setAlignment(QtCore.Qt.AlignCenter)
        self.res_login.setObjectName("res_login")
        self.lab_ir9 = QtWidgets.QLabel(Form)
        self.lab_ir9.setGeometry(QtCore.QRect(40, 620, 91, 21))
        self.lab_ir9.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ir9.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ir9.setObjectName("lab_ir9")
        self.res_powbtn = QtWidgets.QLabel(Form)
        self.res_powbtn.setGeometry(QtCore.QRect(690, 470, 171, 21))
        self.res_powbtn.setFrameShape(QtWidgets.QFrame.Box)
        self.res_powbtn.setAlignment(QtCore.Qt.AlignCenter)
        self.res_powbtn.setObjectName("res_powbtn")
        self.res_sense2 = QtWidgets.QLabel(Form)
        self.res_sense2.setGeometry(QtCore.QRect(420, 290, 161, 21))
        self.res_sense2.setFrameShape(QtWidgets.QFrame.Box)
        self.res_sense2.setAlignment(QtCore.Qt.AlignCenter)
        self.res_sense2.setObjectName("res_sense2")
        self.res_ir9 = QtWidgets.QLabel(Form)
        self.res_ir9.setGeometry(QtCore.QRect(140, 620, 161, 21))
        self.res_ir9.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ir9.setAlignment(QtCore.Qt.AlignCenter)
        self.res_ir9.setObjectName("res_ir9")
        self.btn_audio = QtWidgets.QPushButton(Form)
        self.btn_audio.setGeometry(QtCore.QRect(320, 560, 261, 21))
        self.btn_audio.setObjectName("btn_audio")
        self.lab_thd = QtWidgets.QLabel(Form)
        self.lab_thd.setGeometry(QtCore.QRect(320, 590, 91, 21))
        self.lab_thd.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_thd.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_thd.setObjectName("lab_thd")
        self.btn_conf = QtWidgets.QPushButton(Form)
        self.btn_conf.setGeometry(QtCore.QRect(690, 10, 161, 31))
        self.btn_conf.setObjectName("btn_conf")
        self.btn_cri = QtWidgets.QPushButton(Form)
        self.btn_cri.setGeometry(QtCore.QRect(690, 40, 161, 31))
        self.btn_cri.setObjectName("btn_cri")
        self.lab_scansn = QtWidgets.QLabel(Form)
        self.lab_scansn.setGeometry(QtCore.QRect(40, 80, 91, 21))
        self.lab_scansn.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_scansn.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_scansn.setObjectName("lab_scansn")
        self.lab_ethmac = QtWidgets.QLabel(Form)
        self.lab_ethmac.setGeometry(QtCore.QRect(590, 260, 71, 21))
        self.lab_ethmac.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ethmac.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_ethmac.setObjectName("lab_ethmac")
        self.lab_wifimac = QtWidgets.QLabel(Form)
        self.lab_wifimac.setGeometry(QtCore.QRect(590, 290, 71, 21))
        self.lab_wifimac.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_wifimac.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_wifimac.setObjectName("lab_wifimac")
        self.edit_sn = QtWidgets.QLineEdit(Form)
        self.edit_sn.setGeometry(QtCore.QRect(670, 320, 191, 21))
        self.edit_sn.setText("")
        self.edit_sn.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_sn.setObjectName("edit_sn")
        self.lab_sn = QtWidgets.QLabel(Form)
        self.lab_sn.setGeometry(QtCore.QRect(590, 320, 71, 21))
        self.lab_sn.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_sn.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_sn.setObjectName("lab_sn")
        self.btn_uic = QtWidgets.QPushButton(Form)
        self.btn_uic.setGeometry(QtCore.QRect(590, 350, 271, 21))
        self.btn_uic.setObjectName("btn_uic")
        self.lab_led = QtWidgets.QLabel(Form)
        self.lab_led.setGeometry(QtCore.QRect(590, 380, 91, 21))
        self.lab_led.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_led.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_led.setObjectName("lab_led")
        self.lab_hdmi = QtWidgets.QLabel(Form)
        self.lab_hdmi.setGeometry(QtCore.QRect(590, 410, 91, 21))
        self.lab_hdmi.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_hdmi.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_hdmi.setObjectName("lab_hdmi")
        self.lab_rstbtn = QtWidgets.QLabel(Form)
        self.lab_rstbtn.setGeometry(QtCore.QRect(590, 440, 91, 21))
        self.lab_rstbtn.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_rstbtn.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_rstbtn.setObjectName("lab_rstbtn")
        self.lab_powbtn = QtWidgets.QLabel(Form)
        self.lab_powbtn.setGeometry(QtCore.QRect(590, 470, 91, 21))
        self.lab_powbtn.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_powbtn.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_powbtn.setObjectName("lab_powbtn")
        self.lab_sensever = QtWidgets.QLabel(Form)
        self.lab_sensever.setGeometry(QtCore.QRect(40, 320, 91, 21))
        self.lab_sensever.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_sensever.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_sensever.setObjectName("lab_sensever")
        self.lab_bspver = QtWidgets.QLabel(Form)
        self.lab_bspver.setGeometry(QtCore.QRect(40, 260, 91, 21))
        self.lab_bspver.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_bspver.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_bspver.setObjectName("lab_bspver")
        self.res_bspver = QtWidgets.QLabel(Form)
        self.res_bspver.setGeometry(QtCore.QRect(140, 260, 161, 21))
        self.res_bspver.setFrameShape(QtWidgets.QFrame.Box)
        self.res_bspver.setAlignment(QtCore.Qt.AlignCenter)
        self.res_bspver.setObjectName("res_bspver")
        self.res_sensever = QtWidgets.QLabel(Form)
        self.res_sensever.setGeometry(QtCore.QRect(140, 320, 161, 21))
        self.res_sensever.setFrameShape(QtWidgets.QFrame.Box)
        self.res_sensever.setAlignment(QtCore.Qt.AlignCenter)
        self.res_sensever.setObjectName("res_sensever")
        self.res_irver = QtWidgets.QLabel(Form)
        self.res_irver.setGeometry(QtCore.QRect(140, 290, 161, 21))
        self.res_irver.setFrameShape(QtWidgets.QFrame.Box)
        self.res_irver.setAlignment(QtCore.Qt.AlignCenter)
        self.res_irver.setObjectName("res_irver")
        self.lab_irver = QtWidgets.QLabel(Form)
        self.lab_irver.setGeometry(QtCore.QRect(40, 290, 91, 21))
        self.lab_irver.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_irver.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_irver.setObjectName("lab_irver")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SC300"))
        self.res_poe1.setText(_translate("Form", "NA"))
        self.lab_ir10.setText(_translate("Form", "IR_10"))
        self.lab_tp28.setText(_translate("Form", "TP28"))
        self.btn_ir.setText(_translate("Form", "IR"))
        self.res_iperfeth.setText(_translate("Form", "NA"))
        self.lab_ir2.setText(_translate("Form", "IR_2"))
        self.lab_ir6.setText(_translate("Form", "IR_6"))
        self.res_ir11.setText(_translate("Form", "NA"))
        self.btn_reset.setText(_translate("Form", "Reset"))
        self.lab_ir8.setText(_translate("Form", "IR_8"))
        self.btn_wifipower.setText(_translate("Form", "WIFI Power"))
        self.res_ir1.setText(_translate("Form", "NA"))
        self.res_sense3.setText(_translate("Form", "NA"))
        self.lab_rs23248.setText(_translate("Form", "RS232_48"))
        self.btn_iperfeth.setText(_translate("Form", "Iperf-ETH"))
        self.lab_dc1.setText(_translate("Form", "DC1"))
        self.btn_sense.setText(_translate("Form", "Sense"))
        self.res_tp28.setText(_translate("Form", "NA"))
        self.res_usb3.setText(_translate("Form", "NA"))
        self.res_ir12.setText(_translate("Form", "NA"))
        self.btn_vol.setText(_translate("Form", "VOLTAGE"))
        self.res_wifipower.setText(_translate("Form", "NA"))
        self.res_led.setText(_translate("Form", "NA"))
        self.res_hdmi.setText(_translate("Form", "NA"))
        self.btn_inforw.setText(_translate("Form", "Write_Info"))
        self.lab_ir11.setText(_translate("Form", "IR_11"))
        self.res_ir10.setText(_translate("Form", "NA"))
        self.lab_rs23226.setText(_translate("Form", "RS232_26"))
        self.res_rstbtn.setText(_translate("Form", "NA"))
        self.res_amp.setText(_translate("Form", "NA"))
        self.res_usb2.setText(_translate("Form", "NA"))
        self.label.setText(_translate("Form", "SC300 PCBA ATE"))
        self.lab_poe1.setText(_translate("Form", "POE1"))
        self.lab_sense4.setText(_translate("Form", "Sense_4"))
        self.lab_ir4.setText(_translate("Form", "IR_4"))
        self.res_ir5.setText(_translate("Form", "NA"))
        self.res_sense1.setText(_translate("Form", "NA"))
        self.res_rs23215.setText(_translate("Form", "NA"))
        self.lab_ir3.setText(_translate("Form", "IR_3"))
        self.lab_sense2.setText(_translate("Form", "Sense_2"))
        self.res_ir3.setText(_translate("Form", "NA"))
        self.lab_ir7.setText(_translate("Form", "IR_7"))
        self.res_rs23248.setText(_translate("Form", "NA"))
        self.lab_ir12.setText(_translate("Form", "IR_12"))
        self.res_thd.setText(_translate("Form", "NA"))
        self.lab_ir1.setText(_translate("Form", "IR_1"))
        self.res_dc1.setText(_translate("Form", "NA"))
        self.btn_usb2.setText(_translate("Form", "USB2.0"))
        self.btn_rs485.setText(_translate("Form", "RS485"))
        self.lab_amp.setText(_translate("Form", "SPK_AMP"))
        self.lab_sense3.setText(_translate("Form", "Sense_3"))
        self.res_ir6.setText(_translate("Form", "NA"))
        self.res_sense4.setText(_translate("Form", "NA"))
        self.res_ir4.setText(_translate("Form", "NA"))
        self.lab_ir5.setText(_translate("Form", "IR_5"))
        self.label_15.setText(_translate("Form", "Nortek  Control | Version: 20201201"))
        self.res_rs23237.setText(_translate("Form", "NA"))
        self.res_rs23226.setText(_translate("Form", "NA"))
        self.btn_usb3.setText(_translate("Form", "USB3.0"))
        self.btn_auto.setText(_translate("Form", "Auto"))
        self.res_ir8.setText(_translate("Form", "NA"))
        self.res_inforw.setText(_translate("Form", "NA"))
        self.btn_login.setText(_translate("Form", "Login"))
        self.lab_sense1.setText(_translate("Form", "Sense_1"))
        self.res_ir7.setText(_translate("Form", "NA"))
        self.lab_rs23237.setText(_translate("Form", "RS232_37"))
        self.res_relay.setText(_translate("Form", "NA"))
        self.lab_rs23215.setText(_translate("Form", "RS232_15"))
        self.btn_submit.setText(_translate("Form", "Submit"))
        self.res_rs485.setText(_translate("Form", "NA"))
        self.btn_relay.setText(_translate("Form", "Relay"))
        self.res_ir2.setText(_translate("Form", "NA"))
        self.btn_printer.setText(_translate("Form", "Label_Printer"))
        self.btn_rs232.setText(_translate("Form", "RS232"))
        self.res_login.setText(_translate("Form", "NA"))
        self.lab_ir9.setText(_translate("Form", "IR_9"))
        self.res_powbtn.setText(_translate("Form", "NA"))
        self.res_sense2.setText(_translate("Form", "NA"))
        self.res_ir9.setText(_translate("Form", "NA"))
        self.btn_audio.setText(_translate("Form", "AUDIO"))
        self.lab_thd.setText(_translate("Form", "SPK_THD"))
        self.btn_conf.setText(_translate("Form", "Configuration"))
        self.btn_cri.setText(_translate("Form", "Critieria"))
        self.lab_scansn.setText(_translate("Form", "Serial Num"))
        self.lab_ethmac.setText(_translate("Form", "ETHMAC"))
        self.lab_wifimac.setText(_translate("Form", "WIFIMAC"))
        self.lab_sn.setText(_translate("Form", "SN"))
        self.btn_uic.setText(_translate("Form", "UIC"))
        self.lab_led.setText(_translate("Form", "LED"))
        self.lab_hdmi.setText(_translate("Form", "HDMI"))
        self.lab_rstbtn.setText(_translate("Form", "RSTBTN"))
        self.lab_powbtn.setText(_translate("Form", "POWBTN"))
        self.lab_sensever.setText(_translate("Form", "SENSEVER"))
        self.lab_bspver.setText(_translate("Form", "BSPVER"))
        self.res_bspver.setText(_translate("Form", "NA"))
        self.res_sensever.setText(_translate("Form", "NA"))
        self.res_irver.setText(_translate("Form", "NA"))
        self.lab_irver.setText(_translate("Form", "IRVER"))

