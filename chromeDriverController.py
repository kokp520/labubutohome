import threading
import subprocess

# 定義開啟 Chrome 的函數
def open_chrome_debugger():
    # 使用 subprocess 來執行 shell 指令，啟動 Chrome 並連接開發者工具
    subprocess.run(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", 
                    "--remote-debugging-port=9527", 
                    "--user-data-dir=~/selenium/AutomationProfile"])

# 創建一個新的 thread 來執行開啟 Chrome 的函數
chrome_thread = threading.Thread(target=open_chrome_debugger)

# 開始執行 thread
chrome_thread.start()

# 主線程繼續執行其他任務
print("Chrome is opening in a separate thread for debugging.")