import res_rc
from ui_ui_init import Ui_MainWindow
from ui_reroll import Ui_Form
from city_wea import *
from qt_material import apply_stylesheet
class Loading(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.account=[]
        self.setFixedSize(680,500)
        self.myenroll = enroll()
        self.total_city=city_wea()
        self.pushButton_2.clicked.connect(self.change_01)
        self.pushButton.clicked.connect(self.change_03)
        self.total_city.back.clicked.connect(self.change_04)
        self.sta.insertWidget(1, self.myenroll)
        self.myenroll.pushButton_2.clicked.connect(self.change_02)
        self.myenroll.pushButton.clicked.connect(self.change_02)

    def paintEvent(self, event):
        self.dd=QPixmap(":/image/res/new_load.jpg") #前缀+相对目录
        self.dd.scaled(self.width(),self.height())
        self.setWindowIcon(self.dd)
    def change_01(self):
        """
        loading->enroll
        """
        self.sta.setCurrentIndex(1)

    def change_03(self):
        """
        loading->city_wea
        用于判断账号密码是否正确
        """
        for i in self.myenroll.mem.keys():  #提取所有的账号
            self.account.append(i)
        if self.lineEdit.text() in self.account and self.lineEdit.text()!="" and self.lineEdit_2.text()!="":
            if self.lineEdit_2.text()==self.myenroll.mem[self.lineEdit.text()]:
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.close()
                self.total_city.show()
            else:
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
        else:
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')

    def change_02(self):
        """
        enroll->loading
        用于判断账号密码是否注册正确
        """
        if self.myenroll.lineEdit_2.text() == self.myenroll.lineEdit_3.text():  # 两次输入的密码一致
            self.myenroll.mem[self.myenroll.lineEdit.text()] = self.myenroll.lineEdit_2.text()
            self.myenroll.lineEdit.setText('')
            self.myenroll.lineEdit_2.setText('')
            self.myenroll.lineEdit_3.setText('')
            self.sta.setCurrentIndex(0)
        else:
            self.myenroll.lineEdit.setText('')
            self.myenroll.lineEdit_2.setText('')
            self.myenroll.lineEdit_3.setText('')

    def change_04(self):
        self.total_city.close()
        self.show()

class enroll(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(680,500)
        self.mem=dict()


def half(x):
    return 0.5*x


if __name__=='__main__':
    app=QApplication([])
    win=Loading()
    apply_stylesheet(app,'dark_blue.xml')
    win.show()
    app.exec()