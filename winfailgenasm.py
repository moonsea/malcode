#! /usr/bin/python

import os
import threading

idalPath = "//usr//local//src//ida-pro-6.4//idal"
idcPath = "//usr//local//src//ida-pro-6.4//idc//analysis_fullname.idc"
PATH = './/resource//vxheaven//class//virus.win//compress//compress/'
# PATH = './/resource//vxheaven//class//test/'
# PATH = '..//resource//vxheaven//vl//virus.win/'
ThreadMax = 2


class MyThread(threading.Thread):
    """docstring for MyThread"""

    def __init__(self, filename, filepath):
        super(MyThread, self).__init__()
        self.name = filename
        self.filepath = filepath

    def run(self):
        print "Starting " + self.filename
        genAsm(self.ilepath)
        print "Exiting " + self.name


def genAsm(filepath):
    ExecStr = idalPath + " -c -A -S" + idcPath + " " + filepath
    # print ExecStr
    os.system(ExecStr)


def multiGenAsm(filepath):
    count = threading.active_count()
    print '[+]count:', count

    # while (count >= ThreadMax):
    #     count = threading.active_count()
    #     print '[+]Threadcount:', count

    my_thread = threading.Thread(target=genAsm, args=(filepath, ))
    my_thread.start()
    # my_thread.join()

    if (count == ThreadMax):
        my_thread.join()


def traveseFile(path):
    # thread1 = ''
    # thread2 = ''

    for parent, dirnames, filenames in os.walk(path):

        for filename in filenames:
            parenttype = parent.split('/')[-1]

            if(parenttype != 'fail'):
                continue

            filepath = os.path.join(parent, filename)
            print parent


            if (cleanFile(filename, filepath)):
                continue

            filepath = filepath.replace(' ', '\ ').replace('(', '\(').replace(')', '\)')
            # print filepath

            genAsm(filepath)

            # multiGenAsm(filepath)

            # my_thread = threading.Thread(target=genAsm, args=(filepath, ))
            # my_thread.start()

            # thread1 = MyThread(filename, filepath)
            # thread2 = MyThread(2, "Thread-2", 2)
            #
            # thread1.start()
            # thread2.start()
            #
            # thread1.join()
            # thread2.join()


def cleanFile(filename, filepath):
    filetype = filename.split('.')[-1]
    if (filetype == 'asm' or filetype == 'idb'):
        os.remove(filepath)
        print '[-] Clean ', filename
        return True

    return False


if __name__ == '__main__':
    # print filetype('.//FirstClass//8f84a46017151d935c34878ad4c53293')

    traveseFile(PATH)
