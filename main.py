from PyQt5.QtWidgets import QApplication   # Бібліотеки
from random import shuffle, choice
from time import sleep
app = QApplication([]) # 

from main_window import* # імрорт (main_window)
from menu_window import*

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):      #
        self.question = question                                                            #
        self.answer = answer                                                                #   Створення запитання і відповідей
        self.wrong_answer1 = wrong_answer1                                                  #
        self.wrong_answer2 = wrong_answer2                                                  #
        self.wrong_answer3 = wrong_answer3                                                  #
        self.is_active = True                                                           
        self.count_ask = 0
        self.count_right = 0                
        
    def got_right(self):                    # Правельні відповіді
        self.count_ask += 1
        self.count_right += 1
    
    def got_wrong(self):                    # відповіді
        self.count_ask += 1
        
q1 = Question('Яблуко', 'apple', 'apply', 'pineapple', 'application')       #
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')                     # Питання
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')                   #
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')              #

questions = [q1, q2, q3, q4]                        #
                                                    # Списки
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]    #

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_Question.setText(cur_q.question)
    lb_Corect.setText(cur_q.answer)
    
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.answer)                  #
    radio_buttons[1].setText(cur_q.wrong_answer1)           # прикріплення питань до кнопок
    radio_buttons[2].setText(cur_q.wrong_answer2)           #
    radio_buttons[3].setText(cur_q.wrong_answer3)           #
    
    RadioGroup.setExclusive(False)
    for button in radio_buttons:
        button.setChecked(False)
    RadioGroup.setExclusive(True)

    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')

def check():                                            #
    RadioGroup.setExclusive(False)                      #
    for button in radio_buttons:                        #
        if button.isChecked():                          #
            if button.text() == lb_Corect.text():       #
                cur_q.got_right()                       # перевірка відповіді
                lb_Result.setText('Вірно!')             #
            else:                                       #    Вірно
                cur_q.got_wrong()                       #    Невірно
                lb_Result.setText('Невірно!')           #
        break                                           #
    
    RadioGroup.setExclusive(True)
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')
##############################################################################################
def click_ok():                             #
    if btn_OK.text() == 'Відповісти':       # кнопкa Відповісти i переход до слідущого питання
        check()                             #
    else:                                   #
        new_question()                      #
        
def rest():                                 # кнопка відпочинку
    win_card.hide()                         #
    n = box_Minutes.value() * 60            # множення секунд
    sleep(n)                                #
    win_card.show()                         #
##########################
def menu_generation():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right/cur_q.count_ask)*100

    text = f'Разів відповіли: {cur_q.count_ask}\n' \
           f'Вірних відповідей: {cur_q.count_right}\n' \
           f'Успішність: {round(c, 2)}%'
    lb_statistic.setText(text)
    menu_win.show()
    win_card.hide()
################################################################################################
def clear():                            #  кнопка очистити запитання
    le_question.clear()                 #
    le_right_ans.clear()                # 
    le_wrong_ans1.clear()               #
    le_wrong_ans2.clear()               #
    le_wrong_ans3.clear()               #
    
btn_clear.clicked.connect(clear)

def add_question():                                                              #
    new_q = Question(le_question.text(), le_right_ans.text(),                    #   кнопка додає запитання
                     le_wrong_ans1.text(), le_wrong_ans2.text(),                 #
                     le_wrong_ans3.text())                                       #
    
    questions.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)
    
def back_menu():
    menu_win.hide()        #  menu clous
    win_card.show()


btn_Menu.clicked.connect(menu_generation)
btn_back.clicked.connect(back_menu)
btn_Sleep.clicked.connect(rest)
btn_OK.clicked.connect(click_ok)

new_question()

app.exec_() # виконує код