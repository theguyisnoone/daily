import threading

class cthread(threading.Thread):
    def run(self):
        #import
        self.sing()
        self.dance()
        for i in range(5):
            print("run a bit")


    def sing(self):
        for i in range(0,2):
            print('sing')


    def dance(self):
        for i in range(0,3):
            print('dance')






if __name__ == "__main__":
    t=cthread()
    t.start()
    # t.sing()  still single thread
    # t.dance()
