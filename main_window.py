from PyQt5.QtCore import Qt                                                                         
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, \
    QRadioButton, QSpinBox, QGroupBox, QButtonGroup                                                 # Бібліотеки

card_width, card_height = 600, 500 # Вертикаль и горезанталь
win_card = QWidget() # Вікно
win_card.resize(card_width, card_height) # ширина и висота

win_card.move(300, 300) # росположення на екрані
win_card.setWindowTitle("Memory card") # назва вікна

btn_Menu = QPushButton('Меню') # кнопка Меню
btn_Sleep = QPushButton('Відпочити') # кнопка Відпочити
btn_OK = QPushButton('Відповісти') # кнопка Відповісти
box_Minutes = QSpinBox() # кнопка Барабан 
box_Minutes.setValue(30) # Количиство минут відпочинку
lb_Question = QLabel('Запитання') # друк тексту

RadioGroupBox = QGroupBox("Варіанти відповідей") # Варіанти відповідей
RadioGroup = QButtonGroup()# додає кнопки

rbtn_1 = QRadioButton('1')# кругла кнопка 1
rbtn_2 = QRadioButton('2')# кругла кнопка 2
rbtn_3 = QRadioButton('3')# кругла кнопка 3
rbtn_4 = QRadioButton('4')# кругла кнопка 4

RadioGroup.addButton(rbtn_1)# додає кнопку 1
RadioGroup.addButton(rbtn_2)# додає кнопку 2
RadioGroup.addButton(rbtn_3)# додає кнопку 3
RadioGroup.addButton(rbtn_4)# додає кнопку 4

AnsGroupBox = QGroupBox('Результат тесту')# Результат тесту
lb_Result = QLabel('Правильно')#  текст Правильно
lb_Corect = QLabel('Відповідь')#  текст Відповідь

layout_ans1 = QHBoxLayout() # розміщує у горизонтального ряд
layout_ans2 = QVBoxLayout() # розміщує у вертикальний ряд
layout_ans3 = QVBoxLayout() # розміщує у вертикальний ряд

layout_ans2.addWidget(rbtn_1)# додає кнопку 1 Вертикальну лінію 2
layout_ans2.addWidget(rbtn_2)# додає кнопку 2 Вертикальну лінію 2
layout_ans3.addWidget(rbtn_3)# додає кнопку 3 Вертикальну лінію 3
layout_ans3.addWidget(rbtn_4)# додає кнопку 4 Вертикальну лінію 3

layout_ans1.addLayout(layout_ans2) # об'єднує дві Вертикальні лінії в горезантальу (1 2)
layout_ans1.addLayout(layout_ans3) # об'єднує дві Вертикальні лінії в горезантальу (3 4)

RadioGroupBox.setLayout(layout_ans1)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Corect, alignment = Qt.AlignHCenter, stretch = 2 )
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu) # додає кнопку Меню
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)# додає кнопки Відпочинку
layout_line1.addWidget(box_Minutes)# 
layout_line1.addWidget(QLabel('хвилини'))
layout_line2.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch = 2)
layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

win_card.setLayout(layout_card)

win_card.show()