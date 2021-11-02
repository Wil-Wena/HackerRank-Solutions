#Checking the disk usage
'''
import shutil
du  =  shutil.disk_usage("/")
print(du)
b = du.free/du.total * 100
print(b)
'''
'''
import psutil
m = psutil.cpu_percent(0.1)
print(m)
'''
import shutil, psutil
def check_disk_usage(disk):
    du  =  shutil.disk_usage(disk)
    b = du.free/du.total * 100
    return b > 20
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print('Everything is fine!') 