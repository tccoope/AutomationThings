#!"C:\Program Files\Python312\python.exe"

from ftplib import FTP

ftp = FTP("10.1.100.100")

ftp.login()

print(ftp.getwelcome())

ftp.quit()