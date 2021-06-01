import shutil
import psutil

def disk_usage():
	du = shutil.disk_usage("/")
	print(du)
	print("Free Space",du.free/du.total * 100)
def cpu_usage():
	usage = psutil.cpu_percent(1)
	print(usage)

disk_usage()
cpu_usage()
