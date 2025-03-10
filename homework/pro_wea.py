from PySide6.QtWidgets import QWidget,QApplication,QPushButton
from PySide6.QtCore import Qt,QSize,QRect
from get_data import get_data,get_pm,get_rh
from PySide6.QtGui import *
import res_rc
from pyecharts.charts import Line
from pyecharts.options import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_pro_wea import Ui_Form

class pro_wea(QWidget,Ui_Form):
    def __init__(self,city_name,pro_name):
        super().__init__()
        self.setupUi(self)
        self.city_name=city_name
        self.pro_name=pro_name
        self.setFixedSize(1027,685)
        self.init_tem()
        self.init_label()

    def init_tem(self):
        self.line=Line()
        high_tem=[]
        low_tem=[]
        l1=[]
        l=get_data(self.city_name,self.pro_name)["forecasts"][0]["casts"][0]["date"][5:7]
        # print(get_data(self.city_name,self.pro_name)["forecasts"][0]["casts"][1]["daytemp"])
        for i in range(0,4):
            l1.append(get_data(self.city_name,self.pro_name)["forecasts"][0]["casts"][i]["date"][8:10])
            high_tem.append(get_data(self.city_name,self.pro_name)["forecasts"][0]["casts"][i]["daytemp"])
            low_tem.append(get_data(self.city_name,self.pro_name)["forecasts"][0]["casts"][i]["nighttemp"])
        self.line.add_xaxis(l1)
        self.line.add_yaxis("当日最高温度",high_tem)
        self.line.add_yaxis("当日最低温度",low_tem)
        self.line.set_global_opts(title_opts=TitleOpts(title=f"{self.city_name}市{self.pro_name}区天气情况"),
                                  xaxis_opts=AxisOpts(name=f"{l}月"),
                                  yaxis_opts=AxisOpts(name="单位:℃"))
    def init_label(self):
        self.wind_icon.setPixmap(QPixmap(":/image/res/wind.jpg").scaled(75,21))
        self.wind.setText("风速")
        self.wind_pos_icon.setPixmap(QPixmap(":/image/res/wind_pos.jpg").scaled(75,21))
        self.wind_pos.setText("风向")
        #self.pm_icon.setPixmap(QPixmap(":/image/res/wet.jpg").scaled(75,41))
        self.pm.setText("湿度")
        self.wet_icon.setPixmap(QPixmap(":/image/res/rain.jpg").scaled(75,51))
        self.wet.setText("天气状况")
        self.label.setText(get_data(self.city_name,self.pro_name)["forecasts"][0]["casts"][0]["daypower"])
        self.label_2.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][1]["daypower"])
        self.label_3.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][2]["daypower"])
        self.label_4.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][3]["daypower"])
        self.label_5.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][0]["daywind"])
        self.label_6.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][1]["daywind"])
        self.label_7.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][2]["daywind"])
        self.label_8.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][3]["daywind"])

        self.label_9.setText(f"{get_rh(self.city_name, self.pro_name)}%")

        self.label_13.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][0]["dayweather"])
        self.label_14.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][1]["dayweather"])
        self.label_15.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][2]["dayweather"])
        self.label_16.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][3]["dayweather"])
        self.label_17.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][0]["date"][5:10])
        self.label_18.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][1]["date"][5:10])
        self.label_19.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][2]["date"][5:10])
        self.label_20.setText(get_data(self.city_name, self.pro_name)["forecasts"][0]["casts"][3]["date"][5:10])
        pm25=str(get_pm(self.city_name, self.pro_name))
        self.PM25.setText(pm25)


if __name__=="__main__":
    app=QApplication([])
    mywin=pro_wea("广州","天河区")
    mywin.show()
    app.exec()