import sys
import queue
import multiprocessing
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from MainWindow import Ui_MainWindow

from AddUser import AddUserWindow
from UpdatePassword import UpdatePasswordWindow

from DBDriver import DBDriver

from mainProgram.functionA import main  # 示例主程序


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    继承界面布局类Ui_MainWindow，实现Ui_MainWindow的各种功能，避免对布局ui的修改影响功能代码，
    该类实现基本功能如下：
    1. 启动3个线程：
    （1）process_pool_thread：运行进程池的线程，使用进程池并发运行多个主程序，
                             示例主程序效果：在睡眠2~3秒后返回一个1~10的随机整数
    （2）data_process_thread：运行数据处理程序的线程，通过队列从线程（1）中获取数据，通过信号在主界面实时显示
    （3）running_time_thread：运行耗时统计程序的线程，通过信号在主界面实时显示当前耗时
    """

    def __init__(self):
        """
        初始化函数
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.labelCurrentUser = QLabel(self)  # 当前登录用户，在底部状态栏中显示
        self.setup_statusbar()  # 装载主界面底部状态栏

        self.username = ""  # 用户名，在主界面显示当前登录用户
        self.db_driver = None  # 数据库实例，负责各种增删改查操作
        self.queue = queue.Queue()  # 队列，在进程之间传递数据
        self.process_pool_size = 10  # 进程池大小，即同时运行的进程个数
        self.main_program_batch_size = 100  # 主程序批大小，即主程序的运行个数，如需要处理100张图，每张图需要1个主程序进行处理，则将100个主程序加入进程池
        self.process_pool_thread = None  # 进程池运行线程，在进程池中并发运行多个主程序
        self.data_process_thread = None  # 数据处理线程，用以实时接收进程池运行线程中每一个主程序进程返回的数据，并加以处理
        self.running_time_thread = None  # 耗时统计线程，用以统计显示进程池运行线程的运行时间

        self.add_user_window = AddUserWindow()  # 添加用户界面
        self.update_password_window = UpdatePasswordWindow()  # 更新密码界面

        self.pushButtonStart.clicked.connect(self.start)  # 程序开始运行按钮

        self.actionAddUser.triggered.connect(self.add_user_window.show)  # 添加用户菜单
        self.actionUpdatePassword.triggered.connect(self.update_password_window.show)  # 更新密码菜单

    def setup_statusbar(self):
        """
        装载主界面底部状态栏
        Returns:

        """
        labelCurrentUserTag = QLabel(self)
        labelCurrentUserTag.setText("当前登录用户：")

        # 在主界面底部状态栏从左至右依次挂载两个label，
        # 例如：当前登录用户：admin
        self.statusbar.addWidget(labelCurrentUserTag)
        self.statusbar.addWidget(self.labelCurrentUser)

    def start(self):
        """
        运行程序
        启动三个线程分别运行数据处理程序、耗时统计程序、进程池
        Returns:

        """
        self.start_data_process_thread()
        self.start_running_time_thread()
        self.start_process_pool_thread()

    def start_process_pool_thread(self):
        """
        启动进程池运行线程
        Returns:

        """
        self.process_pool_thread = ProcessPoolThread(self.queue, self.main_program_batch_size, self.process_pool_size)
        self.process_pool_thread.start()

        # 线程启动后改变开始运行按钮样式，设置为不可用、文本设置为"运行中..."
        self.pushButtonStart.setDisabled(True)
        self.pushButtonStart.setText("运行中...")

        # 监听进程池运行完毕信号，收到此信号后交由进程池运行完毕槽函数处理
        self.process_pool_thread.trigger_finished.connect(self.process_pool_finished_handle)

    def start_data_process_thread(self):
        """
        启动数据处理程序线程
        实时接收进程池运行线程中每一个主程序进程返回的数据，并加以处理，实时将处理后的结果通过信号发送至主界面显示
        Returns:

        """
        self.data_process_thread = DataProcessThread(self.queue, self.main_program_batch_size)
        self.data_process_thread.start()

        # 监听当前一个主程序输出结果信号，在主界面的当前结果显示栏中显示
        self.data_process_thread.trigger_current.connect(self.display_in_current)

        # 监听当前已运行完毕的主程序累计输出结果信号，在主界面的总结果显示栏中显示
        self.data_process_thread.trigger_total.connect(self.display_in_total)

        # 监听当前循环次数信号，在主界面运行进度条中显示
        self.data_process_thread.trigger_loops.connect(self.display_in_progress_bar)

    def start_running_time_thread(self):
        """
        启动耗时统计程序线程
        Returns:

        """
        self.running_time_thread = RunningTimeThread()
        self.running_time_thread.start()

        # 监听运行时间信号，在主界面的"运行时间"lcd中显示
        self.running_time_thread.trigger_running_time.connect(self.display_in_lcd)

    def process_pool_finished_handle(self, flag):
        """
        进程池运行完毕槽函数
        Args:
            flag: 进程池运行完毕后返回True

        Returns:

        """
        # 进程池运行完毕后改变开始运行按钮样式，设置为可用、文本设置为"开始运行"
        self.pushButtonStart.setEnabled(True)
        self.pushButtonStart.setText("开始运行")

        # 进程池运行完毕后关闭运行耗时统计程序的线程
        self.running_time_thread.stop()

    def display_in_current(self, current_result):
        """
        在主界面中实时显示当前一个主程序的输出结果
        Args:
            current_result: 当前一个主程序的输出结果

        Returns:

        """
        self.textBrowserCurrentResult.setText(current_result)

    def display_in_total(self, total_result):
        """
        在主界面中实时显示当前已运行完毕的所有主程序的累计输出结果
        Args:
            total_result:当前已运行完毕的所有主程序的累计输出结果

        Returns:

        """
        self.textBrowserTotalResult.setText(total_result)

    def display_in_progress_bar(self, loops):
        """
        在主界面中以进度条的方式实时显示程序运行进度
        Args:
            loops: 已运行完毕的主函数的个数

        Returns:

        """
        # 进度（百分比） = 已运行完毕的主程序个数 / 主程序批大小（需要运行的主程序总个数）
        progress = int(loops / self.main_program_batch_size * 100)
        self.progressBar.setValue(progress)
        self.label_progress.setText(str(progress) + "%")

    def display_in_lcd(self, running_time):
        """
        在主界面的lcd中实时显示程序运行时间
        Args:
            running_time: 程序运行时间

        Returns:

        """
        self.lcdNumber.setProperty("value", running_time)

    def set_username(self, username):
        """
        设置当前登录用户的用户名
        Args:
            username: 用户名

        Returns:

        """
        self.username = username
        self.labelCurrentUser.setText(username)

        # 在更新密码界面中设置username，因为更新密码界面中更新密码时需要根据用户名查询旧密码和设置新密码
        self.update_password_window.set_username(self.username)

    def set_db_driver(self, db_driver):
        """
        设置sqlite数据库驱动
        Args:
            db_driver: sqlite数据库驱动

        Returns:

        """
        self.db_driver = db_driver

        # 在添加用户界面和更新密码界面中设置sqlite数据库驱动，因为这两个界面均涉及数据库操作
        self.add_user_window.set_db_driver(db_driver)
        self.update_password_window.set_db_driver(db_driver)


class ProcessPoolThread(QThread):
    """
    进程池运行线程
    在新线程中运行进程池，在实现多进程并行运行主程序的同时，不会阻塞主窗口进程
    """
    trigger_finished = pyqtSignal(bool)  # 线程池运行完毕信号

    def __init__(self, queue, batch_size, process_pool_size):
        """
        初始化函数
        Args:
            queue: 队列，将运行在进程池中每个进程上的主程序的输出结果存入队列中，在数据处理线程中读取循环读取此队列以实时获取数据
            batch_size: 主程序批大小，需要运行的主程序数量
            process_pool_size: 进程池大小，同时开启的进程数量
        """
        super(ProcessPoolThread, self).__init__()
        self.queue = queue
        self.batch_size = batch_size
        self.pool = multiprocessing.Pool(processes=process_pool_size)

    def run(self):
        """
        重写QThread的run方法，在该线程上开启的进程池
        Returns:

        """
        for i in range(self.batch_size):
            # main为主函数，循环将主函数加入进程池中，并将运行结果存入队列
            self.queue.put(self.pool.apply_async(main))
        self.pool.close()
        self.pool.join()

        # 进程池运行完毕后发出结束信号
        self.trigger_finished.emit(True)


class DataProcessThread(QThread):
    """
    数据处理线程
    """
    trigger_current = pyqtSignal(str)  # 当前一个主程序输出结果信号
    trigger_total = pyqtSignal(str)  # 已运行完毕的主程序累计输出结果信号
    trigger_loops = pyqtSignal(int)  # 当前循环次数信号

    def __init__(self, queue, batch_size):
        """
        初始化函数
        Args:
            queue: 队列，循环从此队列中读取数据
            batch_size: 主函数批大小，用以确定循环读取次数
        """
        super(DataProcessThread, self).__init__()
        self.queue = queue
        self.batch_size = batch_size

    def run(self):
        """
        重写QThread的run方法，在该线程上运行数据处理程序：读取、累计求和、发送
        Returns:

        """
        total = 0
        loops = 0
        while True:
            value = self.queue.get().get()  # 从队列中获取数据，队列为空时阻塞
            total += value
            loops += 1
            self.trigger_total.emit(str(total))
            self.trigger_current.emit(str(value))
            self.trigger_loops.emit(loops)
            if loops == self.batch_size:  # 当循环次数等于主函数批大小时跳出循环
                break


class RunningTimeThread(QThread):
    """
    耗时统计线程
    """
    trigger_running_time = pyqtSignal(float)

    def __init__(self):
        super(RunningTimeThread, self).__init__()
        self.stop_flag = False

    def run(self):
        """

        Returns:
        重写QThread的run方法，在该线程上运行耗时统计程序：
        该程序每隔0.01秒发出一次当前耗时信号，当进程池运行完毕后，调用stop函数以跳出计时循环
        """
        start_time = time.time()
        while True:
            current_time = time.time()
            running_time = current_time - start_time
            self.trigger_running_time.emit(running_time)
            time.sleep(0.01)
            if self.stop_flag:
                break

    def stop(self):
        self.stop_flag = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    db_driver = DBDriver("project")  # 新建sqlite数据库驱动
    main_window.set_db_driver(db_driver)  # 在主窗口程序中安装sqlite数据库驱动
    main_window.show()
    sys.exit(app.exec_())
