from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout # Бібліотеки

menu_win = QWidget()            #  вікно
menu_win.resize(550, 450)       #  розмір вікна
 
lb_quest = QLabel('Введіть запитання:')                                 # запитання
lb_right_ans = QLabel('Введіть правильну відповідь:')                   # відповідi
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь:')                # no
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь:')                # no
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь:')                # no
 
le_question = QLineEdit()       #лінія
le_right_ans = QLineEdit()      #лінія
le_wrong_ans1 = QLineEdit()     # лінія
le_wrong_ans2 = QLineEdit()     #лінія
le_wrong_ans3 = QLineEdit()     #лінія

lb_header_stat = QLabel('Статистика')                                #
lb_header_stat.setStyleSheet('font-size: 19px; font_weight: bold;')  # Розмір шрифта " Статистика "

lb_statistic = QLabel('')

btn_back = QPushButton('Назад')
btn_add_question = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')

vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)      # вертикальний
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)        # горизонтально
hl_question.addLayout(vl_lineEdits)     # поеднаня

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statistic)
vl_res.addWidget(btn_back)

menu_win.setLayout(vl_res)