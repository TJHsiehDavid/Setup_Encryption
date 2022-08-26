1、需要安裝python3-dev，gcc，Cython
2、要先安裝Cython， 才能執行加密程式碼

指令：
linux上安裝 
$ sudo apt install python3-dev gcc
$ pip3 install cython

[使用方法]
1.將想要加密的專案放到build底下
2.將專案在build底下的路徑寫到ini設定中
3.透過cmd進入Setup_Encryption下：python3.8 setup.py build_ext
4.完成檔案就會有一樣的專案名稱只是裡面的py都換成so
