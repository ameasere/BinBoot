ECHO OFF
ECHO This will install python and it's requirements. Continue?
PAUSE
curl "https://www.python.org/ftp/python/3.8.6/python-3.8.6rc1-amd64.exe" --output python3.exe
python3.exe
where pip3 > pippath.txt
set /p pathuse=<pippath.txt
set pathuse2=%pathuse:\pip3.exe= %
del pippath.txt
del python3.exe
cd /d %pathuse2%
pip3 install pyarmor requests
ECHO Finished installation! Now run BinBoot either in IDLE Python or from double clicking the file (harder to stop loops)
PAUSE
