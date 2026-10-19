# RSA／Outseer FraudAction Learning Lab

目前包含 95 題自主練習題，其中 57 題以使用者提供的 FraudAction 教材整理，38 題為明確標記的通用資安知識補充。**不是 RSA／Outseer 官方考題，也不代表原廠逐題認證。**

教材範圍：FraudAction 一般使用者操作手冊、系統維護與管理手冊，以及 2026 年 10 月 v13.5 升版說明。舊版操作與當前平台可能不同；一般資安補充題不應被視為原廠功能宣稱。

可使用題庫搜尋、分類測驗、錯題複習、累積學習紀錄與 JSON 匯入／匯出。紀錄保存在目前瀏覽器的本機儲存空間，**不會自動跨裝置同步**；清除瀏覽資料前請先匯出備份。

詳細導覽：[LEARNING_GUIDE.md](LEARNING_GUIDE.md)。

在本資料夾執行 `python3 -m http.server 8082`，瀏覽 `http://localhost:8082/`。

公開網站：https://tiffany871205.github.io/rsa-quiz-web/

部署方式：GitHub Pages，`main` 分支的 `/(root)` 目錄。執行 `python3 validate.py` 可檢查題庫基本結構。
