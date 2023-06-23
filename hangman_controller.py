import sys
from PyQt5 import QtGui,QtWidgets
from hangman_logic import Hangman
from hangman_GUI import Ui_MainWindow

class Controller():
    def __init__(self, hangman, gui):
        self.hangman_instance = hangman
        self.gui = gui
        self.end_game = False
        self.gui.current_word.setText(self.hangman_instance.indicator)

    def update(self, letter):
        
        if letter == 'new_game':
            self.hangman_instance.new_game()
            self.gui.end_game_message.setText("Pressing a letter to start guessing!")
            self.gui.current_word.setText(self.hangman_instance.indicator)
            self.gui.hangman_pic.setPixmap(QtGui.QPixmap("h{}.png".format(self.hangman_instance.guess_times+1)))
            self.gui.show_result.setEnabled(True)
        elif letter == 'show_result':
            self.gui.end_game_message.setText('The word is')
            self.gui.current_word.setText(self.hangman_instance.word)
            self.gui.hangman_pic.setPixmap(QtGui.QPixmap("h{}.png".format(self.hangman_instance.guess_times+1)))
            self.gui.show_result.setEnabled(False)

        else:   
            self.hangman_instance.guess(letter)
            self.gui.current_word.setText(self.hangman_instance.indicator)
            self.gui.hangman_pic.setPixmap(QtGui.QPixmap("h{}.png".format(self.hangman_instance.guess_times+1)))
        
        #picture from https://github.com/en3rypt/HANGMAN-GAME
        self.check_endgame_condition()


    def check_endgame_condition(self):
        if self.hangman_instance.guess_times >=6:
            self.gui.end_game_message.setText('Better luck next time!')
            self.gui.current_word.setText(self.hangman_instance.word)
            self.gui.disable_letters()
            self.gui.show_result.setEnabled(False)
        elif len(self.hangman_instance.word_letters) == 0:
            self.gui.end_game_message.setText('Congratulations!')
            self.gui.disable_letters()
            self.gui.show_result.setEnabled(False)



if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    hangman = Hangman()
    controller = Controller(hangman, ui)
    ui.add_observer(controller)
    MainWindow.show()
    sys.exit(app.exec_())


