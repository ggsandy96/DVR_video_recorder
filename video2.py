#version 3
#dorun this file at startup
#19th june 2016
#the automatic file deletion of videos feature included
#forced video capture added
#clock speed change

import subprocess
import numpy as np
import csv
import datetime
import os
import signal


def signal_handler(signal, frame):
	os.system("sudo /home/linaro/App/cameraapp/ect_setupclock_high.sh")
	os.system("echo instant start `date` >> /home/linaro/user/camera/cam2/cam2_log_`date +'%m_%d_%y'`.txt")
	cmd_instant  = "ffmpeg -rtsp_transport tcp -y -i rtsp://admin:admin@192.168.1.12 -vcodec copy -t 00:00:15 /home/linaro/user/camera/cam2/cam2_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".mp4"
	os.system(cmd_instant)
	os.system("echo instant stop `date` >> /home/linaro/user/camera/cam2/cam2_log_`date +'%m_%d_%y'`.txt")
	os.system("sudo /home/linaro/App/cameraapp/ect_setupclock_low.sh")

def signal_handler2(signal, frame):
	os.system("sudo /home/linaro/App/cameraapp/ect_setupclock_high.sh")
	os.system("echo event start `date` >> /home/linaro/user/camera/cam2/cam2_log_`date +'%m_%d_%y'`.txt")
	cmd_instant  = "ffmpeg -rtsp_transport tcp -y -i rtsp://admin:admin@192.168.1.12 -vcodec copy -t 00:00:15 /home/linaro/user/camera/cam2/cam2_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".mp4"
	os.system(cmd_instant)
	cmd_instant = "cp /home/linaro/user/camera/cam2/cam2_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".mp4 /home/linaro/user/camera/cam2/event/"
	os.system(cmd_instant)
	os.system("echo event stop `date` >> /home/linaro/user/camera/cam2/cam2_log_`date +'%m_%d_%y'`.txt")
	os.system("sudo /home/linaro/App/cameraapp/ect_setupclock_low.sh")
	
signal.signal(signal.SIGUSR1, signal_handler)
signal.signal(signal.SIGUSR2, signal_handler2)

def read():
        f1 = file('/home/linaro/user/camera/cam2/video2.csv', 'r')
        c1 = csv.reader(f1)
        return c1
try:
	c1 = read()
	c1=list(c1)
	arr1 = np.asarray(c1)
	arr1 = arr1.astype(int)
	a1 = len(arr1)
	old = str(arr1[0][0])
        rem = "find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.mp4' -exec rm -rf {} \;"
        os.system(rem)
	rem = "find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.txt' -exec rm -rf {} \;"
        os.system(rem)
except:
	try:
		os.system("cp /home/linaro/user/camera/cam2/video2.bak /home/linaro/user/camera/cam2/video2.csv")
        	c1= read()
        	c1=list(c1)
        	arr1 = np.asarray(c1)
        	arr1 = arr1.astype(int)
        	a1 = len(arr1)
		old = str(arr1[0][0])
        	rem = "find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.mp4' -exec rm -rf {} \;"
	        os.system(rem)
		rem = "find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.txt' -exec rm -rf {} \;"
	        os.system(rem)

	except:
		arr1 = [[15,10,10],[0,0,0]]
		arr1=list(arr1)
		arr1 = np.asarray(arr1)
		arr1 = arr1.astype(int)
		a1 = len(arr1)
		old = str(arr1[0][0])
        	rem = "find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.mp4' -exec rm -rf {} \;"
	        os.system(rem)
		rem = "find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.txt' -exec rm -rf {} \;"
	        os.system(rem)
day1=int(0)
print arr1
while(1):
	if (os.path.isfile("/home/linaro/user/camera/cam2/video2_new.csv") == True ):
		out = subprocess.check_output("ps aux | grep ftpd", shell=True)
		if 'video2_new.csv' in out:
       			print "csv file is being uploaded"
		else:
		       	print "video2 csv upload complete"
			try:
				os.system("mv /home/linaro/user/camera/cam2/video2.csv /home/linaro/user/camera/cam2/video2.bak")
	                        os.system("mv /home/linaro/user/camera/cam2/video2_new.csv /home/linaro/user/camera/cam2/video2.csv")
				c1= read()
                        	c1=list(c1)
                	        arr1 = np.asarray(c1)
        	                arr1 = arr1.astype(int)
				try:
					old = str(arr1[0][0])
                                        rem = "sudo find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.mp4' -exec rm -rf {} \;"
                                        os.system(rem)
					rem = "sudo find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.txt' -exec rm -rf {} \;"
                                        os.system(rem)
				except:
					continue

			except:
				try:
			                os.system("cp /home/linaro/user/camera/cam2/video2.bak /home/linaro/user/camera/cam2/video2.csv")
                			c1= read()
                			c1=list(c1)
			                arr1 = np.asarray(c1)
        			        arr1 = arr1.astype(int)
                			a1 = len(arr1)
					try:
                                        	old = str(arr1[0][0])
                                        	rem = "sudo find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.mp4' -exec rm -rf {} \;"
                                        	os.system(rem)
						rem = "sudo find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.txt' -exec rm -rf {} \;"
                                        	os.system(rem)
		                	except:
                                        	continue

        			except:
                			arr1 = [[15,0,0],[0,0,0]]
                			arr1=list(arr1)
                			arr1 = np.asarray(arr1)
               				arr1 = arr1.astype(int)
					try:
                	                        old = str(arr1[0][0])
	                                        rem = "sudo find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.mp4' -exec rm -rf {} \;"
        	                                os.system(rem)
						rem = "sudo find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.txt' -exec rm -rf {} \;"
        	                                os.system(rem)
                                	except:
                                        	continue
	now = datetime.datetime.now()
        day = str(now.day)
	year = str(now.year)
        month = str(now.month)
        hour = str(now.hour)
        minute = str(now.minute)
        second = str(now.second)
	if(int(day) != day1):
		rem = "sudo find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.mp4' -exec rm -rf {} \;"
		os.system(rem)
		rem = "sudo find /home/linaro/user/camera/cam2 -type f -mtime +" +old+ " -name '*.txt' -exec rm -rf {} \;"
        	os.system(rem)
		day1 = int(day)
	try:
		f = open('/home/linaro/user/camera/cam2/status.txt', 'r')
		y=int(f.read())
	except:
		y=0
	if(y==1):
		os.system("sudo /home/linaro/App/cameraapp/ect_setupclock_high.sh")
		os.system("echo motion start `date` >> /home/linaro/user/camera/cam2/cam2_log_`date +'%m_%d_%y'`.txt")
        	cmd_instant  = "ffmpeg -rtsp_transport tcp -y -i rtsp://admin:admin@192.168.1.12 -vcodec copy -t 00:00:15 /home/linaro/user/camera/cam2/cam2_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".mp4"
		os.system(cmd_instant)
		os.system("echo motion stop `date` >> /home/linaro/user/camera/cam2/cam2_log_`date +'%m_%d_%y'`.txt")
		os.system("sudo /home/linaro/App/cameraapp/ect_setupclock_low.sh")
