
# 範例
# 開啟 Google Chrome 並啟用開發者工具
# 開啟瀏覽器後，在網址列輸入 chrome://inspect/#devices 開啟開發者工具
# 點選左上角的齒輪按鈕，選擇要連接的裝置，然後點選連接按鈕
# 開啟自動化測試工具，點選左上角的齒輪按鈕，選擇要連接的裝置，然後點選連接按鈕
# 點選自動化測試工具中的開始按鈕，開始自動化測試

# 範例 Makefile

# 定義 Makefile 規則

# .PHONY: baseserver

# 定義 baseserver 規則

baseserver:
	./Google\ Chrome --remote-debugging-port=9527 --user-data-dir="~/selenium/AutomationProfile"

debuggerserver:
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9527


#  ./Google\ Chrome --remote-debugging-port=9527 --user-data-dir="~/selenium/AutomationProfile"  

# 正於現有瀏覽器工作階段中開啟。