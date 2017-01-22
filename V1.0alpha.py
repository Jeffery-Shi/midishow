
import urllib.request
import sys
import os
import threading
fileid=input("""
MiDishow下载器V1.0
Powered by Jeffery
请输入作品编号
""")

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    global url
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    downsize=blocknum * blocksize
    if downsize >= totalsize:
    	downsize=totalsize
    s ="%.2f%%"%(percent)+"====>"+"%.2f"%(downsize/1024/1024)+"M/"+"%.2f"%(totalsize/1024/1024)+"M \r\n"
    sys.stdout.write(s)
    sys.stdout.flush()
    if percent == 100:
        print('')
        print('下载完成!')
        print("按回车键写入midi文件并退出程序")
def downimg():
    url='http://www.midishow.com/midi/file/'+fileid+'.mid'
    filename=os.path.basename(url)
    urllib.request.urlretrieve(url, filename, callbackfunc)
#启动线程下载
threading.Thread(target=downimg,args=('')).start()


