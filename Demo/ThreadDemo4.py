# 创建一个类调用它的某个函数就是新建立一个线程
# 线程只做一件事情：更新类中的某个参数
import threading
import time


class MyClass:
    def __init__(self):
        self.seconds = 0
        self.print_seconds()
        self.t1 = threading.Thread(target=self.play_voice)
        self.t1.daemon = True
        self.t1.start()

    def play_voice(self):
        while True:
            self.seconds += 1
            time.sleep(1)
            print('playVideo', self.seconds)

    def print_seconds(self):
        print(self.seconds)
