from pythonping import ping
from datetime import datetime
import time
import os 
import colorama
from colorama import Fore, Style
colorama.init()

ipToPing = '1.1.1.1'

def main():
  while True:
    try:
      Ping = int(ping (ipToPing , size= 32, count= 1, verbose=False, out=False, timeout=1).rtt_avg_ms)
      if Ping < 200:
        print('Reply from '+ipToPing+': bytes=32 time=', Fore.GREEN+str(Ping)+Style.RESET_ALL)
      elif 900 > Ping > 200:
        print('Reply from '+ipToPing+': bytes=32 time=', Fore.YELLOW+str(Ping)+Style.RESET_ALL)
      elif Ping >= 1000:
        print(Fore.RED+'Request Timed Out.'+Style.RESET_ALL, gettime())
      time.sleep(1)
    except:
      print(Fore.RED+'Request Timed Out.'+Style.RESET_ALL, gettime())
 
def gettime():
  now = datetime.now()
  return now.strftime("%H:%M:%S")

if __name__ == '__main__':
  main()