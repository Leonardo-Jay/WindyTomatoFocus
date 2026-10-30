# coding:utf-8
        
import sys
import winreg as reg 
from PyQt5.QtWidgets import QApplication, QWidget, QDialog,QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import Qt,QTimer,pyqtSignal,QTime
from PyQt5.QtGui import QIcon
from datetime import datetime, timedelta
import jianku
import winsound
from keshihua import Ui_Form
from demo import Ui_Dialog,settingDialog 
from os import startfile,path,chdir
from plyer import notification
if getattr(sys, 'frozen', False):  
    # 打包后的环境  
    exe_path = path.dirname(sys.executable)  
else:  
    # 非打包环境，使用__file__获取脚本路径  
    exe_path = path.dirname(path.realpath(__file__))
# pathl=sys.argv[0].replace("zhuchengxu.py","")
chdir(exe_path)
# print(pathl,"pathl")
db_path = path.join(exe_path, 'shujuku', 'schedule.db')
filename = path.join(exe_path, 'shujuku', 'defaultdata.json')
nowtime = datetime.now()  #获取年月日小时分钟
nowdate = nowtime.date()# 注意这里使用了 .date() 方法来获取日期对象
#****初始化设置界面
class SetDialog(QDialog, settingDialog):  
    signal_to_quit = pyqtSignal(bool,int)
    def __init__(self, parent=None):  
        super(SetDialog, self).__init__(parent)  
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)#不显示帮助按钮
        self.frame_4.setGeometry(self.frame_3.geometry())  # 复制位置和大小  
        self.frame_5.setGeometry(self.frame_3.geometry())  # 复制位置和大小  
        self.frame_4.hide()  # Initially hide frame_3  
        self.frame_5.hide()  # Initially hide frame_4
        self.listWidget.itemClicked.connect(self.on_item_clicked) 
        self.setAttribute(Qt.WA_DeleteOnClose, True)#最关键的一点,实现当此窗口关闭时释放这个类的资源。
        self.duihao3.hide()
        self.app_path = path.join( exe_path, "风中番茄专注.exe")
        data = jianku.tiqujson(filename)
        if data["setaim1"] == 1:
            self.radioButton2.setChecked(True) 
        else:
            self.radioButton.setChecked(True) 
        if data["setaim2"] == 1:
            self.duihao2.setCheckState(Qt.Checked)
        if data["setaim3"] == 1:
            self.duihao4.setCheckState(Qt.Checked)
        if data["setaim4"] == 1:
            self.duihao4_2.setCheckState(Qt.Checked)
        if data["setaim5"] == 1:
            self.duihao3.setCheckState(Qt.Checked)
    def closeEvent(self, event):  
    #     # 自定义关闭逻辑
        #print("进入closeEvent函数")
        # QTimer.singleShot(400, self.close)  # 隐藏对话框而不是关闭
        self.close()
        #return event.ignore()  # 阻止关闭
    def on_item_clicked(self,item):
        #print(item,item.text(),type(item))
        if item.text() == "计时设置":  
            #print("Item 1 was clicked")  
            # 在这里添加处理 Item 1 被点击的逻辑  z
            # 例如，显示或隐藏某个界面元素  
            self.frame_3.hide()  # 假设点击 Item 1 时显示 frame_3
            self.frame_5.hide()  # 假设点击 Item 2 时隐藏 frame_3
            self.frame_4.show()  # 假设点击 Item 1 时显示 frame_3  
        elif item.text() == "基础设置":  
            #print("Item 2 was clicked")
            # 在这里添加处理 Item 2 被点击的逻辑  
            # 例如，执行其他操作  
            self.frame_4.hide()  # 假设点击 Item 2 时隐藏 frame_3
            self.frame_5.hide()  # 假设点击 Item 2 时隐藏 frame_3
            self.frame_3.show()  # 假设点击 Item 1 时显示 frame_3  
        elif item.text() == "  关于  ":  
            #print("Item 2 was clicked")
            # 在这里添加处理 Item 2 被点击的逻辑  
            # 例如，执行其他操作  
            self.frame_4.hide()  # 假设点击 Item 2 时隐藏 frame_3
            self.frame_3.hide()  # 假设点击 Item 2 时隐藏 frame_3
            self.frame_5.show()  # 假设点击 Item 1 时显示 frame_3  
    def searchquit(self,nothing):
        self.signal_to_quit.emit(self.radioButton2.isChecked(),1)
        jianku.xiugaijson(filename,int(self.radioButton2.isChecked()),2)
    def startup(self,isstartup):
        #print(isstartup,type(isstartup))
        jianku.xiugaijson(filename,int(isstartup),3)
        self.set_startup(bool(isstartup))
    def setwarmming(self,iswarmming):
        self.signal_to_quit.emit(iswarmming,2)
        jianku.xiugaijson(filename,int(iswarmming),4)
        
    def setsinging(self,issinging):
        self.signal_to_quit.emit(issinging,3)
        jianku.xiugaijson(filename,int(issinging),5)
    def deteledatabiao(self):
        jianku.clear_day_notetime_table(db_path,nowdate)
    def openvisionnote(self):
        file_path = path.join('.\\shujuku\\版本日志.txt')  
  
        if path.exists(file_path):  
            try:  
                startfile(file_path) 
            except Exception as e:  
                print('错误', f'无法打开文件: {e}')  
        else:  
            print( '警告', f'文件不存在: {file_path}')
    def opencopyright(self):
        file_path = path.join('.\\shujuku\\风中番茄专注软件版权声明.txt')  
        if path.exists(file_path):  
            try:  
                startfile(file_path) 
            except Exception as e:  
                print('错误', f'无法打开文件: {e}')  
        else:  
            print('警告', f'文件不存在: {file_path}')
    def set_startup(self,isstartup):  
        try:  
            # 打开注册表项（写权限）  
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_SET_VALUE)  
            if isstartup:
                # 设置开机自启动  
                reg.SetValueEx(key, "风中番茄专注.exe", 0, reg.REG_SZ, self.app_path)  
                #print(f"Success: {self.app_path} will start on boot.")  
            else:  
                # 删除开机自启动  
                reg.DeleteValue(key, "风中番茄专注.exe")  
                #print(f"Success: {self.app_path} will not start on boot.")  
  
            # 关闭注册表项  
            reg.CloseKey(key)  
  
        except Exception as e:  
            print(f"没有成功设置自启动,Error: {e}")  
class MyDialog(QDialog, Ui_Dialog):  
    closedWithIndex = pyqtSignal(int) 
    def __init__(self, parent=None):  
        super(MyDialog, self).__init__(parent)  
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)#不显示帮助按钮
        items = ('1小时', '2小时','3小时','3小时30分钟','4小时','5小时',
                 '6小时','7小时','8小时','9小时')#从零开始
        self.ComboBox.addItems(items)
        self.ComboBox.setCurrentIndex(6)
        self.ComboBox.currentIndexChanged.connect(lambda index: print(self.ComboBox.currentText()))
        
        self.TimePicker.setTime(QTime(0, 0))
        self.setAttribute(Qt.WA_DeleteOnClose, True)#最关键的一点,实现当此窗口关闭时释放这个类的资源。
    def savesettime(self):
        #print("save_success:",self.ComboBox.currentText())
        self.closedWithIndex.emit(self.ComboBox.currentIndex()) 
        self.close()
    def notsavesettime(self):
        #print("save_not:",self.ComboBox.currentText())
        self.close()
    def saveaddtime(self):
        #print("save_add_success:",self.TimePicker.time,type(self.TimePicker.time))
        backtime = self.TimePicker.time.hour() *60 +self.TimePicker.time.minute()
        if backtime != 0:
            self.closedWithIndex.emit(backtime)
        self.close()
        return
    def notaddtime(self):
        #print("save_not_add:",self.TimePicker.time)
        self.close()
        return
        
class Tomatoleo(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        jianku.databaseinit(filename,db_path,nowdate)#初始化数据库
        self.setupUi(self)#UI所有界面的初始化
        #其他需要初始化的东西
        self.inittuopan()
        
        #初始化page2的进度环
        self.data = jianku.tiqusettime(nowdate,0)
        print("self.data:",self.data)
        self.daysettime.setText(str(self.data) )
        self.renwutiao.setMaximum(self.data*60)
        # #初始化page2的设置按钮的返回值
        # self.dialog_closed_index = self.on_dialog_closed_with_index
        #初始化窗口的内容
        self.setWindowTitle("风中番茄专注 0.6.1beta版")  # 设置窗口标题 Author:LeonardoJay
        self.setWindowIcon(QIcon('./assets/public/clock.ico')) # 设置窗口图标
        #初始化page2
        self.jindutiaoinit()#初始化每日的进度条
        sahngwu,zhongwu,xiawu = jianku.tiqusettime(nowdate- timedelta(days=1),1)#提取昨天的专注时间
        self.lastdayfinishtime.setText(str(round((sahngwu+zhongwu+xiawu)/60,1)))#初始化昨天专注时间
        #初始化连续达标天数
        if jianku.tiqusettime(nowdate- timedelta(days=1),2) == 0 +jianku.tiqusettime(nowdate,2) == 0:
            jianku.resetgoonday(filename)
        self.lianxitime.setText(str(jianku.page2search_goalday(nowdate))) 
        #c初始化三个进度条的颜色
        self.zhuanzhutiao.setCustomBarColor("#51c4d3", "#51c4d3") 
        self.renwutiao.setCustomBarColor("#51c4d3", "#51c4d3") 
        self.thattiao.setCustomBarColor("#51c4d3", "#51c4d3")
        #初始化定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        #确保窗口运行就能强制出现而不是最小化到任务栏
        self.setWindowState(Qt.WindowNoState)  # 设置窗口状态为无特殊状态 
        self.resize(785, 410)
        self.showNormal()
        self.kaishizhuanzhu.clicked.connect(self.changeTrayIcon)  # 连接信号到槽函数
        #接收菜单的数值
        self.guanbiswtich = bool(jianku.tiqujson(filename)["setaim1"])
        self.guanbiswtich2 = bool(jianku.tiqujson(filename)["setaim3"])
        self.guanbiswtich3 = bool(jianku.tiqujson(filename)["setaim4"])
        self.label_14.hide()
#*********************************************
#创建托盘的函数 
    def inittuopan(self):
        # 创建托盘图标  
        self.trayIcon = QSystemTrayIcon(QIcon('./assets/public/clock.png'), self)  
        self.trayIcon.setVisible(True)  
        self.trayIcon.setToolTip("风中番茄专注")  # 设置托盘图标的悬停提示
        # 创建托盘菜单  
        menu = QMenu()  
        quitAction = QAction("退出  ", self)  # 移除多余的空格使文本更紧凑  
        settingsAction = QAction("设置  ", self)  # 重命名变量以增加可读性  
        aboutAction = QAction("关于  ", self)  # 重命名变量以增加可读性  
        quitAction.triggered.connect(self.customQuit) 
        settingsAction.triggered.connect(self.setdialogshow)
        aboutAction.triggered.connect(self.aboutdialogshow) 
        menu.addAction(aboutAction)  #关于按钮
        menu.addAction(settingsAction)  #设置按钮
        menu.addAction(quitAction)  #关闭按钮
        # 设置样式表以调整菜单的外观  
        menu.setStyleSheet("""  
            QMenu {  
                background-color: white;  
                color: black; /* 设置文本颜色 */  
            }  
            QMenu::item {  
                padding: 4px 20px; /* 调整填充，这里的10px是水平填充，您可以根据需要减小它 */  
                font-size: 9pt; /* 调整字体大小 */  
            }  
            QMenu::item:selected {  
                background-color: #E5E5E5;  
            }  
        """)  
        self.trayIconMenu = menu  # 保存对菜单的引用以便稍后删除
        self.trayIcon.setContextMenu(menu)  
        # 连接托盘图标的激活信号到show方法  
        self.trayIcon.activated.connect(self.showFromTray)
        
    def customQuit(self):
        # 自定义的退出方法
        #print("进入了customQuit函数")
        self.trayIcon.setVisible(False)  # 隐藏托盘图标
        # 断开托盘图标的信号和槽连接（可选，但推荐）
        self.trayIcon.activated.disconnect(self.showFromTray)
        self.close()
        # 删除对菜单的引用（可选，但有助于垃圾回收）
        QApplication.quit()
        # return QTimer.singleShot(400, self.close)  
    def setdialogshow(self):
        setdialog = SetDialog(self) 
        setdialog.setWindowTitle("总设置页面")
        setdialog.signal_to_quit.connect(self.receive_signal)
        setdialog.exec_()  # 使用exec_()方法以非模态方式显示对话框
        #print("进入了setdialogshow函数")
    def showFromTray(self, reason):  
        # 如果点击托盘图标，显示主窗口  
        if reason == QSystemTrayIcon.Trigger:  
            self.showNormal()  
    def aboutdialogshow(self):
        setdialog = SetDialog(self) 
        setdialog.setWindowTitle("总设置页面")
        setdialog.listWidget.setCurrentRow(2)
        setdialog.signal_to_quit.connect(self.receive_signal)
        setdialog.frame_4.hide()  # 假设点击 Item 2 时隐藏 frame_3
        setdialog.frame_3.hide()  # 假设点击 Item 2 时隐藏 frame_3
        setdialog.frame_5.show()  # 假设点击 Item 1 时显示 frame_3  
        setdialog.exec_()  # 使用exec_()方法以非模态方式显示对话框
        #print("进入了aboutdialogshow函数")
    def closeEvent(self, event):  
        # 重写关闭事件以最小化到托盘  
        # if self.trayIcon.isVisible():  
        #     self.hide()  
        #     event.ignore()  # 阻止默认的关闭行为 
        self.close()
        if  self.guanbiswtich:
            # 断开托盘图标的信号和槽连接（可选，但推荐）
            self.setAttribute(Qt.WA_DeleteOnClose, True)#最关键的一点,实现当此窗口关闭时释放这个类的资源。
            QApplication.quit()
    def changeTrayIcon(self):  
        # 改变托盘图标的图标  
        newIcon = QIcon('./assets/public/clock-active.png')  # 新图标的路径 
        self.trayIcon.setToolTip("风中番茄专注\n正在专注")  # 设置托盘图标的悬停提示
        self.trayIcon.setIcon(newIcon)  
    def revertTrayIconToOriginal(self):  
        # 恢复托盘图标为原始图标  
        self.trayIcon.setIcon(QIcon('./assets/public/clock.png')) 
    def receive_signal(self,switch,axis):
        #print("axissssssss:",axis)
        #print(type(self.guanbiswtich),type(switch))
        if axis == 1:
            self.guanbiswtich = switch
        elif axis == 2:
            self.guanbiswtich2 = switch
        elif axis == 3:
            self.guanbiswtich3 = switch    
        #print(self.guanbiswtich,self.guanbiswtich2,self.guanbiswtich3)
#***********************************************          
#以下是两个额外窗口的函数      
        
    def open_dialog(self):  
        self.dialog = MyDialog(self) 
        self.dialog.setWindowTitle("设置目标时间")
        self.dialog.closedWithIndex.connect(self.on_dialog_closed_with_index) 
        self.dialog.frame2.hide()
        self.dialog.exec_()  # 使用exec_()方法以模态方式显示对话框
        
    def on_dialog_closed_with_index(self, index):  
        # 当 MyDialog 发射 closedWithIndex 信号时，这个槽函数会被调用
        itemsback = (1,2,3,3.5,4,5,6,7,8,9)
        jianku.xiugaijson(filename,itemsback[index],1)
        jianku.update_goal_setting_time(nowdate,itemsback[index])
        self.daysettime.setText(str(itemsback[index]) )
        self.renwutiao.setMaximum(itemsback[index]*60)#修改进度条的最大值
       # print("Received index from dialog:", itemsback[index]) 
        #↓用来判断有没有完成任务
        timehe = self.jindutiaoinit()
        #print("timehe:",timehe,"jianku:",jianku.tiqusettime(nowdate,0) * 60)
        if jianku.tiqusettime(nowdate,0) * 60 < timehe:
            jianku.update_time(nowdate,1,4)
        else :
            jianku.update_time(nowdate,0,4)
        self.lianxitime.setText(str(jianku.page2search_goalday(nowdate))) 
    def closed_with_addwiget_dialog(self,addtime):
        print(type(addtime),addtime)
        jianku.add_learnedtime(nowdate,nowtime,addtime)#addhour *60 + addmins)
        #↓用来判断有没有完成任务
        timehe = self.jindutiaoinit()
        if jianku.tiqusettime(nowdate,0) * 60 < timehe:
            jianku.update_time(nowdate,1,4)           
        else :
            jianku.update_time(nowdate,0,4)
        return
    def addwidget(self):##增加专注时间的页面生成
        dialog = MyDialog(self) 
        dialog.setWindowTitle("增加专注时间")
        dialog.closedWithIndex.connect(self.closed_with_addwiget_dialog) 
        dialog.frame2.setGeometry(dialog.frame.geometry())  # 复制位置和大小  
        dialog.frame2.show()
        dialog.frame.hide()
        dialog.exec_()  # 使用exec_()方法以模态方式显示对话框
#*****************************************************
#自定义的函数
    def jindutiaoinit(self):#这里并不是初始化进度条函数，而是查询时间设置值的函数。
        shangwu,xiawu,wanshang = jianku.tiqusettime(nowdate,1)
        timehe = shangwu+xiawu+wanshang
        if timehe >= 60:
            self.frame2_1.hide()
            self.frame2_2.show()
            
            self.dayfinishtime_xiaoshi.setText(str(int(timehe/60))+"小时  "+str(timehe%60)+" 分钟")
        else:
            self.dayfinishtime.setText(str(timehe))
        self.renwutiao.setValue(timehe)
        if jianku.tiqusettime(nowdate,0) * 60 < timehe:
            self.renwutiao.setValue(jianku.tiqusettime(nowdate,0) * 60)
        return timehe
    # setupUi
    def update_countdown(self):  
        # 更新剩余时间  
        self.remaining_minutes -= 1
        self.daojishi.setText(str(self.remaining_minutes))
        chazhi = self.byjisuantime-self.remaining_minutes
        self.zhuanzhutiao.setValue(chazhi)
        # 如果剩余时间小于0，停止计时器  
        if self.remaining_minutes <= 1:  
            self.timer.stop()
            self.timer60.start(1000)
            jianku.add_learnedtime(nowdate,nowtime,4)
        elif self.remaining_minutes % 5 == 0:
            jianku.add_learnedtime(nowdate,nowtime,5)
            self.jindutiaoinit()
            
    def update_last60(self):  
        # 更新剩余时间  
        self.last60s -= 1  
        self.miaoshudaojishi.setProperty("intValue", self.last60s)
        
        # 如果剩余时间小于0，停止计时器  
        if self.last60s == 60:
            self.zhuanzhutiao.setValue(self.byjisuantime)
            self.miaoshudaojishi.show()
        elif self.last60s <10:
            self.miaoshudaojishi.setDigitCount(1)
            if self.last60s < 0:
                self.timer60.stop()
                self.frame4.hide()
                self.miaoshudaojishi.hide()
                self.frame.show()
                self.revertTrayIconToOriginal()
                jianku.add_learnedtime(nowdate,nowtime,1)
                jianku.page2search_goalday(nowdate)
                #↓用来判断有没有完成任务
                timehe = self.jindutiaoinit()
                if jianku.tiqusettime(nowdate,0) * 60 < timehe:
                    jianku.update_time(nowdate,1,4)           
                else :
                    jianku.update_time(nowdate,0,4)
                if self.guanbiswtich2 == 1:
                    notification.notify(  
                        title='专注消息',  
                        message='您已完成一个时间段的专注，请劳逸结合，以便在下次专注中精力集中！',  
                        app_icon = path.join(exe_path, 'assets', 'public', 'clock.ico'),
                        app_name='风中番茄专注',  
                        timeout=10  # Notification timeout in seconds  
                    )
                if self.guanbiswtich3 == 1:
                    winsound.MessageBeep(winsound.MB_OK)
#*************************************                
#以下是UI界面信号连接的函数              
    def settimevalue(self,backtime):
        if backtime == 0:
            backtime = 1
        elif backtime == 1:
            backtime = 1
        elif backtime % 5 != 0:
            backtime -= backtime %5
        
        self.CompactSpinBox.setValue(backtime)
        self.remaining_minutes = backtime
        self.byjisuantime = backtime
        #print(self.remaining_minutes,type(backtime),"settimevalue函数")
    def openmenu(self):
        setdialog = SetDialog(self) 
        setdialog.setWindowTitle("总设置页面")
        setdialog.listWidget.setCurrentRow(0)
        setdialog.signal_to_quit.connect(self.receive_signal)
        setdialog.frame_4.hide()  # 假设点击 Item 2 时隐藏 frame_3
        setdialog.frame_5.hide()  # 假设点击 Item 2 时隐藏 frame_3
        setdialog.frame_3.show()  # 假设点击 Item 1 时显示 frame_3  
        setdialog.exec_()  # 使用exec_()方法以非模态方式显示对话框
    def jishistartpage4(self):
        #print("self.CompactSpinBox.value:",self.CompactSpinBox.value(),type(self.CompactSpinBox.value()))
        self.miaoshudaojishi.setDigitCount(2)
        self.byjisuantime =self.CompactSpinBox.value()
        self.remaining_minutes = self.CompactSpinBox.value()
        self.last60s = 62
        if self.byjisuantime == 1:
            self.zhuanzhutiao.setMaximum(self.byjisuantime)
            self.zhuanzhutiao.setValue(self.byjisuantime)
            self.timer60.start(1000)
            self.miaoshudaojishi.show()
            return
        self.zhuanzhutiao.setValue(0)
        self.zhuanzhutiao.setMaximum(self.byjisuantime)
        self.daojishi.setText(str(self.remaining_minutes))
        self.timer.start(60000)#每分钟计时60000
        
        #print("jishistartpage4函数运行")

    def stoptime(self):##暂停时间
        self.revertTrayIconToOriginal()
        if self.remaining_minutes > 1:
            self.timer.stop()
            #print("stoptime函数运行")
        else:
            self.timer60.stop()
            #print("stoptime60s函数运行") 
        
    def goontime(self):##继续时间
        self.changeTrayIcon()
        if self.remaining_minutes > 1:
            self.timer.start(60000)
        else:
            self.timer60.start(1000)
       # print("goontime函数运行",)
        
    def stopnote(self):##停止并重置计时
        self.timer.stop()
        self.timer60.stop()
        self.miaoshudaojishi.hide()
        self.revertTrayIconToOriginal()
        self.last60s = 62
       # print("stopnote函数运行")
        #↓用来判断有没有完成任务
        timehe = self.jindutiaoinit()
        if jianku.tiqusettime(nowdate,0) * 60 < timehe:
            jianku.update_time(nowdate,1,4)
        else :
            jianku.update_time(nowdate,0,4)
        stopzhi = (10 - (self.remaining_minutes %10))%5
        if stopzhi == 0:
            return
        jianku.add_learnedtime(nowdate,nowtime,stopzhi)
        self.jindutiaoinit()
    def setdatachange(self,backdate):#设置指定日期的页面专注条及标签
        backdate = backdate.toString("yyyy-MM-dd")
        self.setdate3.setText(backdate)#用于在点第1个时第3个能显示
        sahngwu,zhongwu,xiawu = jianku.tiqusettime(backdate,1)
        timehe = sahngwu+zhongwu+xiawu
        if timehe == 0:
            self.thatdaytime.setText("无")
            self.thatsettime.setText("无")
            self.thattiao.setValue(0)
            self.thatdaytime.setStyleSheet(u"color: rgb(255, 121, 123);")
            self.thatsettime.setStyleSheet(u"color: rgb(255, 121, 123);")
        else:
            self.thatdaytime.setStyleSheet(u"color: rgb(0,0,0);")
            self.thatsettime.setStyleSheet(u"color: rgb(0,0,0);")
            self.thatdaytime.setText(str(round((timehe)/60,1)))
            mubiaozhi = jianku.tiqusettime(backdate,0)
            self.thatsettime.setText(str(mubiaozhi))
            mubiaozhi *= 60
            if mubiaozhi < timehe:
                timehe = mubiaozhi
            self.thattiao.setMaximum(mubiaozhi)
            self.thattiao.setValue(timehe)
            
        #print("backdate:",backdate ,type(backdate))
    def changepage3(self):
        #↓3行用于重设一下日期选择器
        self.setdate1.reset()
        self.setdate2.reset()
        self.tongjishu1.setText(str(jianku.page3search_time(nowdate,1)))#
        self.tongjishu2.setText(str(jianku.page3search_time(nowdate,2)))
        self.tongjishu3.setText(str(jianku.page3search_time(nowdate,3)))
        self.tongjishu4.setText(str(jianku.page3search_goal(nowdate,1)))
        self.tongjishu5.setText(str(jianku.page3search_goal(nowdate,2)))
        self.tongjishu6.setText(str(jianku.page3search_goal(nowdate,3)))
        self.tongjishu7.setText(str(jianku.page3search_avg(nowdate,2))+"/"#上午
                                +str(jianku.page3search_avg(nowdate,3))+"/"#中午
                                +str(jianku.page3search_avg(nowdate,4)))#下午
        self.tongjishu8.setText(str(jianku.page3search_avg(nowdate,1)))
        self.tongjishu9.setText(str(round(jianku.page3search_time(nowdate,2)/4,1)))
        
    def changepage5(self):
        #↓3行用于重设一下日期选择器
        self.setdate1.reset()
        self.setdate2.reset()
        
        self.zhou1.setText(str(6))
        self.zhou2.setText(str(6))
        self.zhou3.setText(str(6))
        self.zhou4.setText(str(6))
        self.zhou5.setText(str(6))
        self.zhou6.setText(str(6))
        self.zhou7.setText(str(6))
        weekday_number = nowtime.weekday()+1  
        zhouword = getattr(self, f'zhouword{weekday_number}')
        zhouword.setStyleSheet(u"color: rgb(255, 121, 123);")
        for i in range(weekday_number, 0, -1):  
           #print(i,"iiii")
           progress_bar = getattr(self, f'zhoutiao{i}')
           zhoushuzhi = getattr(self, f'zhou{i}')
           zhoujindu = getattr(self, f'zhoujindu{i}')
           zhoujindu.show()
           sahngwu,zhongwu,xiawu = jianku.tiqusettime(nowdate- timedelta(days=weekday_number-i),1)
           mubiaotime = jianku.tiqusettime(nowdate- timedelta(days=weekday_number-i),0)
           value = sahngwu+zhongwu+xiawu  # 示例值，你可以根据需要调整  
           #print(value,nowdate- timedelta(days=weekday_number-i))
           progress_bar.setMaximum(mubiaotime * 60)
           zhoushuzhi.setText(str(mubiaotime))
           zhoujindu.setText(str(round(value/60,1)))
           if value >mubiaotime * 60:
               progress_bar.setValue(mubiaotime * 60)
               continue
           progress_bar.setValue(value)

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # 关键!!!!!!!设置应用程序在最后一个窗口关闭时不退出!!!!!!
    w = Tomatoleo()
    w.show()
    sys.exit(app.exec_())  # 使用sys.exit()确保QApplication.exec_()退出时程序也会退出
