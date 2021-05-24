import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
import multiprocessing

from AddUser import AddUserWindow
from UpdatePassword import UpdatePasswordWindow

from MainWindow import Ui_MainWindow

from functions.functionA import main
import queue


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    继承界面布局类Ui_MainWindow，实现Ui_MainWindow的各种功能，避免对布局ui的修改影响功能代码；
    该类实现基本功能如下：
    1. 启动2个线程，一个线程运行程序A，一个线程运行程序B，其中，程序A用一个进程池处理高耗时程序，
    程序B通过队列实时接收程序A的数据并进行二次处理，最终通过自定义信号在主界面展示；
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.username = ""
        self.add_user_window = AddUserWindow()
        self.update_password_window = UpdatePasswordWindow()
        self.queue = queue.Queue()
        self.processA_number = 100
        self.threadA = None
        self.threadB = None
        self.pushButton.clicked.connect(self.processA_th)
        self.actionAddUser.triggered.connect(self.add_user_window.show)
        self.actionUpdatePassword.triggered.connect(self.update_password_window.show)

    def processA_th(self):
        self.processB_th()
        self.threadA = ThreadA(self.queue, self.processA_number)
        self.threadA.start()

    def processB_th(self):
        """
        实时处理程序A的回传数据。
        从程序A中接收数据进行二次处理，通过信号交由展示程序进行展示
        :return:
        """
        self.threadB = ThreadB(self.queue, self.processA_number)
        self.threadB.start()
        self.threadB.trigger_value.connect(self.display_in_value)
        self.threadB.trigger_total.connect(self.display_in_total)
        self.threadB.trigger_loops.connect(self.display_in_progress_bar)

    def display_in_value(self, value):
        self.textBrowserCurrentResult.setText(value)

    def display_in_total(self, total):
        self.textBrowserTotalResult.setText(total)

    def display_in_progress_bar(self, loops):
        progress = int(loops / self.processA_number * 100)
        self.progressBar.setValue(progress)
        self.label_progress.setText(str(progress) + "%")

    def set_username(self, username):
        self.username = username
        self.label_current_user.setText(username)
        self.update_password_window.set_username(self.username)
        self.update_password_window.label_username.setText(username)


class ThreadA(QThread):
    """
    线程A运行处理程序A，开起进程池以加快程序A的运行速度
    """

    def __init__(self, queue, number):
        # 初始化函数
        super(ThreadA, self).__init__()
        self.queue = queue
        self.number = number
        self.pool = multiprocessing.Pool(processes=10)

    def run(self):
        for i in range(self.number):
            self.queue.put(self.pool.apply_async(main))
        self.pool.close()
        self.pool.join()


class ThreadB(QThread):
    """
    线程B运行处理程序B
    """

    trigger_value = pyqtSignal(str)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger_total = pyqtSignal(str)
    trigger_loops = pyqtSignal(int)

    def __init__(self, queue, number):
        # 初始化函数
        super(ThreadB, self).__init__()
        self.queue = queue
        self.number = number

    def run(self):
        # 触发自定义信号
        total = 0
        loops = 0
        while True:
            value = self.queue.get().get()
            total += value
            loops += 1
            self.trigger_total.emit(str(total))  # 通过自定义信号把待显示的字符串传递给槽函数
            self.trigger_value.emit(str(value))
            self.trigger_loops.emit(loops)
            if loops == self.number:
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
