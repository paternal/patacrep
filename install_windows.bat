setx path "%path%;C:\Python27;C:\Python27\Scripts;"

setx pathext "%pathext%;.py"

cscript /nologo windows/wget.js https://raw.github.com/pypa/pip/master/contrib/get-pip.py > get-pip.py

C:\Python27\Python.exe get-pip.py

C:\Python27\Scripts\pip install -r Requirements.txt

C:\Python27\Python.exe setup.py install