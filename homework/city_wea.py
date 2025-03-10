from PySide6.QtWidgets import QWidget,QApplication,QPushButton,QMainWindow,QGroupBox
from PySide6.QtGui import *
from PySide6.QtCore import Qt,QSize,QRect
from ui_wea import Ui_MainWindow01
from get_data import get_data,get_pm
import res_rc
from ui_cho_pro import Ui_MainWindow02
from pro_wea import pro_wea
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import *
class city_wea(QMainWindow,Ui_MainWindow01):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1027,685)
        self.init_icon()
        self.sta.setCurrentIndex(0)
        self.sta.setGeometry(0,0,1027,685)
        self.background.setFixedSize(self.width(),self.height())
        self.background.setGeometry(0,0,850,641)
        self.background.setStyleSheet(u"background-image: url(:/image/res/china.jpg);")
        self.pushButton.clicked.connect(lambda: self.change01("北京"))
        self.pushButton_2.clicked.connect(lambda: self.change01("上海"))
        self.pushButton_3.clicked.connect(lambda: self.change01("广州"))
        self.pushButton_4.clicked.connect(lambda: self.change01("成都"))
        self.back.setGeometry(20,20,70,60)
        self.setWindowTitle("天气预报")


    def init_icon(self):
        self.icon=QIcon()
        self.icon.addFile(":/image/res/BeiJingIcon.png")
        self.pushButton.setGeometry(630,265,45,40)
        self.setWindowIcon(self.icon)
        self.pushButton_2.setGeometry(715,400,40,40)
        self.pushButton_3.setGeometry(600,575,30,40)
        self.pushButton_4.setGeometry(463,436,40,35)

    def change01(self,name):
        """
        :return:
        """
        self.city=ui_city(name)
        self.city.go.clicked.connect(self.change03)
        self.sta.insertWidget(1,self.city)
        self.city.pushButton.clicked.connect(self.change02)
        self.sta.setCurrentIndex(1)

    def change02(self):
        self.sta.setCurrentIndex(0)

    def change03(self):
        self.sta.insertWidget(2,self.city.bro)
        if self.city.go.text()!="请选择市区":
            self.sta.setCurrentIndex(2)

        self.city.bro.back.clicked.connect(lambda: self.sta.setCurrentIndex(1))
class ui_city(QMainWindow,Ui_MainWindow02):
    def __init__(self,name):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1027,685)
        self.label.setPixmap(QPixmap(":/image/res/three.jpg").scaled(20,20))
        self.go.setText("请选择市区")
        self.init_pic(name)


    def init_pic(self,city_name):
        """
        根据传入的城市名称进行初始化
        :param city_name: str,城市名称
        """
        if city_name=="广州":
            data01=["天河区","荔湾区","越秀区","海珠区","白云区","黄埔区","番禺区","花都区","南沙区","从化区","增城区"]
            self.total=11
            self.q1=QPushButton(self)
            self.q1.setText(data01[0])
            self.q1.setGeometry(10,90,90,30)
            self.q1.clicked.connect(lambda: self.init_pro(city_name,data01[0]))
            self.q1.clicked.connect(lambda: self.change_go(city_name,data01[0]))

            self.q2=QPushButton(self)
            self.q2.setText(data01[1])
            self.q2.setGeometry(10,90+1*35,90,30)
            self.q2.clicked.connect(lambda: self.init_pro(city_name,data01[1]))
            self.q2.clicked.connect(lambda: self.change_go(city_name,data01[1]))

            self.q3=QPushButton(self)
            self.q3.setText(data01[2])
            self.q3.setGeometry(10,90+2*35,90,30)
            self.q3.clicked.connect(lambda: self.init_pro(city_name,data01[2]))
            self.q3.clicked.connect(lambda: self.change_go(city_name,data01[2]))

            self.q4 = QPushButton(self)
            self.q4.setText(data01[3])
            self.q4.setGeometry(10, 90 + 3 * 35, 90, 30)
            self.q4.clicked.connect(lambda: self.init_pro(city_name,data01[3]))
            self.q4.clicked.connect(lambda: self.change_go(city_name,data01[3]))

            self.q5 = QPushButton(self)
            self.q5.setText(data01[4])
            self.q5.setGeometry(10, 90 + 4 * 35, 90, 30)
            self.q5.clicked.connect(lambda: self.init_pro(city_name,data01[4]))
            self.q5.clicked.connect(lambda: self.change_go(city_name,data01[4]))

            self.q6 = QPushButton(self)
            self.q6.setText(data01[5])
            self.q6.setGeometry(10, 90 + 5 * 35, 90, 30)
            self.q6.clicked.connect(lambda: self.init_pro(city_name,data01[5]))
            self.q6.clicked.connect(lambda: self.change_go(city_name,data01[5]))

            self.q7 = QPushButton(self)
            self.q7.setText(data01[6])
            self.q7.setGeometry(10, 90 + 6 * 35, 90, 30)
            self.q7.clicked.connect(lambda: self.init_pro(city_name,data01[6]))
            self.q7.clicked.connect(lambda: self.change_go(city_name,data01[6]))

            self.q8 = QPushButton(self)
            self.q8.setText(data01[7])
            self.q8.setGeometry(10, 90 + 7 * 35, 90, 30)
            self.q8.clicked.connect(lambda: self.init_pro(city_name,data01[7]))
            self.q8.clicked.connect(lambda: self.change_go(city_name,data01[7]))

            self.q9 = QPushButton(self)
            self.q9.setText(data01[8])
            self.q9.setGeometry(10, 90 + 8 * 35, 90, 30)
            self.q9.clicked.connect(lambda: self.init_pro(city_name,data01[8]))
            self.q9.clicked.connect(lambda: self.change_go(city_name,data01[8]))

            self.q10 = QPushButton(self)
            self.q10.setText(data01[9])
            self.q10.setGeometry(10, 90 + 9 * 35, 90, 30)
            self.q10.clicked.connect(lambda: self.init_pro(city_name,data01[9]))
            self.q10.clicked.connect(lambda: self.change_go(city_name,data01[9]))

            self.q11 = QPushButton(self)
            self.q11.setText(data01[10])
            self.q11.setGeometry(10, 90 + 10 * 35, 90, 30)
            self.q11.clicked.connect(lambda: self.init_pro(city_name,data01[10]))
            self.q11.clicked.connect(lambda: self.change_go(city_name,data01[10]))
            self.pic.setPixmap(QPixmap(":/image/res/GuangZhou.jpg").scaled(self.pic.size()))


        if city_name=="北京":
            data01=["东城区","西城区","朝阳区","丰台区","石景山区","海淀区","门头沟区","房山区","通州区","顺义区","昌平区","大兴区","怀柔区","平谷区","密云区","延庆区"]
            self.total=16
            self.q1=QPushButton(self)
            self.q1.setText(data01[0])
            self.q1.setGeometry(10,90,90,30)
            self.q1.clicked.connect(lambda: self.init_pro(city_name,data01[0]))
            self.q1.clicked.connect(lambda: self.change_go(city_name,data01[0]))

            self.q2=QPushButton(self)
            self.q2.setText(data01[1])
            self.q2.setGeometry(10,90+1*35,90,30)
            self.q2.clicked.connect(lambda: self.init_pro(city_name,data01[1]))
            self.q2.clicked.connect(lambda: self.change_go(city_name,data01[1]))

            self.q3=QPushButton(self)
            self.q3.setText(data01[2])
            self.q3.setGeometry(10,90+2*35,90,30)
            self.q3.clicked.connect(lambda: self.init_pro(city_name,data01[2]))
            self.q3.clicked.connect(lambda: self.change_go(city_name,data01[2]))

            self.q4 = QPushButton(self)
            self.q4.setText(data01[3])
            self.q4.setGeometry(10, 90 + 3 * 35, 90, 30)
            self.q4.clicked.connect(lambda: self.init_pro(city_name,data01[3]))
            self.q4.clicked.connect(lambda: self.change_go(city_name,data01[3]))

            self.q5 = QPushButton(self)
            self.q5.setText(data01[4])
            self.q5.setGeometry(10, 90 + 4 * 35, 90, 30)
            self.q5.clicked.connect(lambda: self.init_pro(city_name,data01[4]))
            self.q5.clicked.connect(lambda: self.change_go(city_name,data01[4]))

            self.q6 = QPushButton(self)
            self.q6.setText(data01[5])
            self.q6.setGeometry(10, 90 + 5 * 35, 90, 30)
            self.q6.clicked.connect(lambda: self.init_pro(city_name,data01[5]))
            self.q6.clicked.connect(lambda: self.change_go(city_name,data01[5]))

            self.q7 = QPushButton(self)
            self.q7.setText(data01[6])
            self.q7.setGeometry(10, 90 + 6 * 35, 90, 30)
            self.q7.clicked.connect(lambda: self.init_pro(city_name,data01[6]))
            self.q7.clicked.connect(lambda: self.change_go(city_name,data01[6]))

            self.q8 = QPushButton(self)
            self.q8.setText(data01[7])
            self.q8.setGeometry(10, 90 + 7 * 35, 90, 30)
            self.q8.clicked.connect(lambda: self.init_pro(city_name,data01[7]))
            self.q8.clicked.connect(lambda: self.change_go(city_name,data01[7]))

            self.q9 = QPushButton(self)
            self.q9.setText(data01[8])
            self.q9.setGeometry(10, 90 + 8 * 35, 90, 30)
            self.q9.clicked.connect(lambda: self.init_pro(city_name,data01[8]))
            self.q9.clicked.connect(lambda: self.change_go(city_name,data01[8]))

            self.q10 = QPushButton(self)
            self.q10.setText(data01[9])
            self.q10.setGeometry(10, 90 + 9 * 35, 90, 30)
            self.q10.clicked.connect(lambda: self.init_pro(city_name,data01[9]))
            self.q10.clicked.connect(lambda: self.change_go(city_name,data01[9]))

            self.q11 = QPushButton(self)
            self.q11.setText(data01[10])
            self.q11.setGeometry(10, 90 + 10 * 35, 90, 30)
            self.q11.clicked.connect(lambda: self.init_pro(city_name,data01[10]))
            self.q11.clicked.connect(lambda: self.change_go(city_name,data01[10]))

            self.q12 = QPushButton(self)
            self.q12.setText(data01[11])
            self.q12.setGeometry(10, 90 + 11 * 35, 90, 30)
            self.q12.clicked.connect(lambda: self.init_pro(city_name,data01[11]))
            self.q12.clicked.connect(lambda: self.change_go(city_name,data01[11]))

            self.q13 = QPushButton(self)
            self.q13.setText(data01[12])
            self.q13.setGeometry(10, 90 + 12 * 35, 90, 30)
            self.q13.clicked.connect(lambda: self.init_pro(city_name,data01[12]))
            self.q13.clicked.connect(lambda: self.change_go(city_name,data01[12]))

            self.q14 = QPushButton(self)
            self.q14.setText(data01[13])
            self.q14.setGeometry(10, 90 + 13 * 35, 90, 30)
            self.q14.clicked.connect(lambda: self.init_pro(city_name,data01[13]))
            self.q14.clicked.connect(lambda: self.change_go(city_name,data01[13]))

            self.q15 = QPushButton(self)
            self.q15.setText(data01[14])
            self.q15.setGeometry(10, 90 + 14 * 35, 90, 30)
            self.q15.clicked.connect(lambda: self.init_pro(city_name,data01[14]))
            self.q15.clicked.connect(lambda: self.change_go(city_name,data01[14]))

            self.q16 = QPushButton(self)
            self.q16.setText(data01[15])
            self.q16.setGeometry(10, 90 + 15 * 35, 90, 30)
            self.q16.clicked.connect(lambda: self.init_pro(city_name,data01[15]))
            self.q16.clicked.connect(lambda: self.change_go(city_name,data01[15]))
            self.pic.setPixmap(QPixmap(":/image/res/BeiJing.png").scaled(self.pic.size()))

        if city_name=="上海":
            data01 = ["黄浦区","徐汇区","长宁区","静安区","普陀区","虹口区","杨浦区","闵行区","宝山区","嘉定区","浦东新区","金山区","松江区","青浦区","奉贤区","崇明区"]
            self.total=16
            self.q1=QPushButton(self)
            self.q1.setText(data01[0])
            self.q1.setGeometry(10,90,90,30)
            self.q1.clicked.connect(lambda: self.init_pro(city_name,data01[0]))
            self.q1.clicked.connect(lambda: self.change_go(city_name,data01[0]))

            self.q2=QPushButton(self)
            self.q2.setText(data01[1])
            self.q2.setGeometry(10,90+1*35,90,30)
            self.q2.clicked.connect(lambda: self.init_pro(city_name,data01[1]))
            self.q2.clicked.connect(lambda: self.change_go(city_name,data01[1]))

            self.q3=QPushButton(self)
            self.q3.setText(data01[2])
            self.q3.setGeometry(10,90+2*35,90,30)
            self.q3.clicked.connect(lambda: self.init_pro(city_name,data01[2]))
            self.q3.clicked.connect(lambda: self.change_go(city_name,data01[2]))

            self.q4 = QPushButton(self)
            self.q4.setText(data01[3])
            self.q4.setGeometry(10, 90 + 3 * 35, 90, 30)
            self.q4.clicked.connect(lambda: self.init_pro(city_name,data01[3]))
            self.q4.clicked.connect(lambda: self.change_go(city_name,data01[3]))

            self.q5 = QPushButton(self)
            self.q5.setText(data01[4])
            self.q5.setGeometry(10, 90 + 4 * 35, 90, 30)
            self.q5.clicked.connect(lambda: self.init_pro(city_name,data01[4]))
            self.q5.clicked.connect(lambda: self.change_go(city_name,data01[4]))

            self.q6 = QPushButton(self)
            self.q6.setText(data01[5])
            self.q6.setGeometry(10, 90 + 5 * 35, 90, 30)
            self.q6.clicked.connect(lambda: self.init_pro(city_name,data01[5]))
            self.q6.clicked.connect(lambda: self.change_go(city_name,data01[5]))

            self.q7 = QPushButton(self)
            self.q7.setText(data01[6])
            self.q7.setGeometry(10, 90 + 6 * 35, 90, 30)
            self.q7.clicked.connect(lambda: self.init_pro(city_name,data01[6]))
            self.q7.clicked.connect(lambda: self.change_go(city_name,data01[6]))

            self.q8 = QPushButton(self)
            self.q8.setText(data01[7])
            self.q8.setGeometry(10, 90 + 7 * 35, 90, 30)
            self.q8.clicked.connect(lambda: self.init_pro(city_name,data01[7]))
            self.q8.clicked.connect(lambda: self.change_go(city_name,data01[7]))

            self.q9 = QPushButton(self)
            self.q9.setText(data01[8])
            self.q9.setGeometry(10, 90 + 8 * 35, 90, 30)
            self.q9.clicked.connect(lambda: self.init_pro(city_name,data01[8]))
            self.q9.clicked.connect(lambda: self.change_go(city_name,data01[8]))

            self.q10 = QPushButton(self)
            self.q10.setText(data01[9])
            self.q10.setGeometry(10, 90 + 9 * 35, 90, 30)
            self.q10.clicked.connect(lambda: self.init_pro(city_name,data01[9]))
            self.q10.clicked.connect(lambda: self.change_go(city_name,data01[9]))

            self.q11 = QPushButton(self)
            self.q11.setText(data01[10])
            self.q11.setGeometry(10, 90 + 10 * 35,90, 30)
            self.q11.clicked.connect(lambda: self.init_pro(city_name,data01[10]))
            self.q11.clicked.connect(lambda: self.change_go(city_name,data01[10]))

            self.q12 = QPushButton(self)
            self.q12.setText(data01[11])
            self.q12.setGeometry(10, 90 + 11 * 35, 90, 30)
            self.q12.clicked.connect(lambda: self.init_pro(city_name,data01[11]))
            self.q12.clicked.connect(lambda: self.change_go(city_name,data01[11]))

            self.q13 = QPushButton(self)
            self.q13.setText(data01[12])
            self.q13.setGeometry(10, 90 + 12 * 35, 90, 30)
            self.q13.clicked.connect(lambda: self.init_pro(city_name,data01[12]))
            self.q13.clicked.connect(lambda: self.change_go(city_name,data01[12]))

            self.q14 = QPushButton(self)
            self.q14.setText(data01[13])
            self.q14.setGeometry(10, 90 + 13 * 35, 90, 30)
            self.q14.clicked.connect(lambda: self.init_pro(city_name,data01[13]))
            self.q14.clicked.connect(lambda: self.change_go(city_name,data01[13]))

            self.q15 = QPushButton(self)
            self.q15.setText(data01[14])
            self.q15.setGeometry(10, 90 + 14 * 35, 90, 30)
            self.q15.clicked.connect(lambda: self.init_pro(city_name,data01[14]))
            self.q15.clicked.connect(lambda: self.change_go(city_name,data01[14]))

            self.q16 = QPushButton(self)
            self.q16.setText(data01[15])
            self.q16.setGeometry(10, 90 + 15 * 35, 90, 30)
            self.q16.clicked.connect(lambda: self.init_pro(city_name,data01[15]))
            self.q16.clicked.connect(lambda: self.change_go(city_name,data01[15]))
            #self.pic.setPixmap(QPixmap("C:/Users/86134/Desktop/res/BeiJing.png").scaled(self.pic.size()))
            self.pic.setPixmap(QPixmap(":/image/res/ShangHai.jpg").scaled(self.pic.size()))

        if city_name=="成都":
            data01 = ["锦江区","青羊区","金牛区","武侯区","成华区","龙泉驿区","青白江区","新都区","温江区","双流区","郫都区","金堂县","大邑县","蒲江县","新津区","都江堰市","彭州市","邛崃市","崇州市"]
            self.total=19
            self.q1=QPushButton(self)
            self.q1.setText(data01[0])
            self.q1.setGeometry(10,90,90,25)
            self.q1.clicked.connect(lambda: self.init_pro(city_name,data01[0]))
            self.q1.clicked.connect(lambda: self.change_go(city_name,data01[0]))

            self.q2=QPushButton(self)
            self.q2.setText(data01[1])
            self.q2.setGeometry(10,90+1*25,90,25)
            self.q2.clicked.connect(lambda: self.init_pro(city_name,data01[1]))
            self.q2.clicked.connect(lambda: self.change_go(city_name,data01[1]))

            self.q3=QPushButton(self)
            self.q3.setText(data01[2])
            self.q3.setGeometry(10,90+2*25,90,25)
            self.q3.clicked.connect(lambda: self.init_pro(city_name,data01[2]))
            self.q3.clicked.connect(lambda: self.change_go(city_name,data01[2]))

            self.q4 = QPushButton(self)
            self.q4.setText(data01[3])
            self.q4.setGeometry(10, 90 + 3 * 25, 90, 25)
            self.q4.clicked.connect(lambda: self.init_pro(city_name,data01[3]))
            self.q4.clicked.connect(lambda: self.change_go(city_name,data01[3]))

            self.q5 = QPushButton(self)
            self.q5.setText(data01[4])
            self.q5.setGeometry(10, 90 + 4 * 25, 90, 25)
            self.q5.clicked.connect(lambda: self.init_pro(city_name,data01[4]))
            self.q5.clicked.connect(lambda: self.change_go(city_name,data01[4]))

            self.q6 = QPushButton(self)
            self.q6.setText(data01[5])
            self.q6.setGeometry(10, 90 + 5 * 25, 90, 25)
            self.q6.clicked.connect(lambda: self.init_pro(city_name,data01[5]))
            self.q6.clicked.connect(lambda: self.change_go(city_name,data01[5]))

            self.q7 = QPushButton(self)
            self.q7.setText(data01[6])
            self.q7.setGeometry(10, 90 + 6 * 25, 90, 25)
            self.q7.clicked.connect(lambda: self.init_pro(city_name,data01[6]))
            self.q7.clicked.connect(lambda: self.change_go(city_name,data01[6]))

            self.q8 = QPushButton(self)
            self.q8.setText(data01[7])
            self.q8.setGeometry(10, 90 + 7 * 25, 90, 25)
            self.q8.clicked.connect(lambda: self.init_pro(city_name,data01[7]))
            self.q8.clicked.connect(lambda: self.change_go(city_name,data01[7]))

            self.q9 = QPushButton(self)
            self.q9.setText(data01[8])
            self.q9.setGeometry(10, 90 + 8 * 25, 90, 25)
            self.q9.clicked.connect(lambda: self.init_pro(city_name,data01[8]))
            self.q9.clicked.connect(lambda: self.change_go(city_name,data01[8]))

            self.q10 = QPushButton(self)
            self.q10.setText(data01[9])
            self.q10.setGeometry(10, 90 + 9 * 25, 90, 25)
            self.q10.clicked.connect(lambda: self.init_pro(city_name,data01[9]))
            self.q10.clicked.connect(lambda: self.change_go(city_name,data01[9]))

            self.q11 = QPushButton(self)
            self.q11.setText(data01[10])
            self.q11.setGeometry(10, 90 + 10 * 25, 90, 25)
            self.q11.clicked.connect(lambda: self.init_pro(city_name,data01[10]))
            self.q11.clicked.connect(lambda: self.change_go(city_name,data01[10]))

            self.q12 = QPushButton(self)
            self.q12.setText(data01[11])
            self.q12.setGeometry(10, 90 + 11 * 25, 90, 25)
            self.q12.clicked.connect(lambda: self.init_pro(city_name,data01[11]))
            self.q12.clicked.connect(lambda: self.change_go(city_name,data01[11]))

            self.q13 = QPushButton(self)
            self.q13.setText(data01[12])
            self.q13.setGeometry(10, 90 + 12 * 25, 90, 25)
            self.q13.clicked.connect(lambda: self.init_pro(city_name,data01[12]))
            self.q13.clicked.connect(lambda: self.change_go(city_name,data01[12]))

            self.q14 = QPushButton(self)
            self.q14.setText(data01[13])
            self.q14.setGeometry(10, 90 + 13 * 25, 90, 25)
            self.q14.clicked.connect(lambda: self.init_pro(city_name,data01[13]))
            self.q14.clicked.connect(lambda: self.change_go(city_name,data01[13]))

            self.q15 = QPushButton(self)
            self.q15.setText(data01[14])
            self.q15.setGeometry(10, 90 + 14 * 25, 90, 25)
            self.q15.clicked.connect(lambda: self.init_pro(city_name,data01[14]))
            self.q15.clicked.connect(lambda: self.change_go(city_name,data01[14]))

            self.q16 = QPushButton(self)
            self.q16.setText(data01[15])
            self.q16.setGeometry(10, 90 + 15 * 25, 90, 25)
            self.q16.clicked.connect(lambda: self.init_pro(city_name,data01[15]))
            self.q16.clicked.connect(lambda: self.change_go(city_name,data01[15]))

            self.q17 = QPushButton(self)
            self.q17.setText(data01[16])
            self.q17.setGeometry(10, 90 + 16 * 25, 90, 25)
            self.q17.clicked.connect(lambda: self.init_pro(city_name, data01[16]))
            self.q17.clicked.connect(lambda: self.change_go(city_name, data01[16]))

            self.q18 = QPushButton(self)
            self.q18.setText(data01[17])
            self.q18.setGeometry(10, 90 + 17 * 25, 90, 25)
            self.q18.clicked.connect(lambda: self.init_pro(city_name, data01[17]))
            self.q18.clicked.connect(lambda: self.change_go(city_name, data01[17]))

            self.q19 = QPushButton(self)
            self.q19.setText(data01[18])
            self.q19.setGeometry(10, 90 + 18 * 25, 90, 25)
            self.q19.clicked.connect(lambda: self.init_pro(city_name, data01[18]))
            self.q19.clicked.connect(lambda: self.change_go(city_name, data01[18]))
            self.pic.setPixmap(QPixmap(":/image/res/ChengDu.jpg").scaled(self.pic.size()))

    def init_pro(self,x,y):
        self.bro=pro_wea(x,y)
        self.bro.temp.setHtml(self.bro.line.render_embed())
        self.bro.temp.show()

    def change_go(self,name01,name02):
        self.go.setText(f"前往{name01}市{name02}")

if __name__=='__main__':
    app=QApplication([])
    mywin=city_wea()
    mywin.show()
    app.exec()