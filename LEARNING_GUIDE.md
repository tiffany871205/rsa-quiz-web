# RSA／Outseer FraudAction 學習導覽

> 根據使用者提供的 Dashboard 操作手冊及 v13.5 升版教材整理。版本、權限及契約可能影響實際畫面；此文件不是原廠官方操作指南。

## 一、先分清三個資料層級

| 層級 | 說明 | 查找方式 |
| --- | --- | --- |
| Case（案件） | 用於統整事件及其關聯元素 | SEARCH → Cases → Case ID |
| Element（元素） | 案件中的個別 URL 或其他受追蹤元素；可查看狀態與再上線次數 | SEARCH → Elements → Element ID |
| Finding（事證） | 例如釣魚工具包、畫面截圖、Whois 資訊等調查證據 | SEARCH → Findings → Finding ID |

**常見誤解：** 一個 Case 不必然等於一個 Element；也不能把 Finding 當成獨立下架案件。

## 二、判讀下架狀態

教材將 Phishing、Brand Abuse 的下架計次描述為依 Element 處理，而 Trojan 依 Case 計次；這是**教材所載規則**，實際服務計費應以契約為準。

| 欄位 | 研讀重點 |
| --- | --- |
| Status | Element 目前 Online 或 Offline |
| #Reopens | 曾關閉後再度上線的偵測次數 |
| Duration | 教材所述從發現到 AFCC 關閉的期間；某些自行離線情況可能沒有值 |
| Shutdown Activity | 不應只憑 Shutdown Complete 判斷是由 AFCC 親自完成下架 |
| Shutdown Information | 查看 Detected、Pending Approval、Shutdown Approved、Authorities Notified、Completed 等處理節點 |

**案例：** 客戶看到 `Shutdown Complete`，正確做法是查閱歷程及實際離線情況，不應立即承諾「一定由服務團隊下架成功」。

## 三、Intelligence Feeds

教材提到 IOC、Credential Recovery 等情資類別。舊版手冊記載的 CSV 匯出上限為十萬筆、Excel 為一萬筆；這些數字是**舊版教材規格**，不代表當前版本一定相同。

2026 年 10 月的 v13.5 升版教材指出：`SEARCH → Intelligence Feeds → Credential Recovery` 增加 `Corporate Emails – Combolist` 子分類。

## 四、Advanced Notifications 與 AFCC DESK

Advanced Notifications 的 `User Action` 包含 Approved、Pending、Denied、Discard；分別表示同意、待處理、拒絕與放棄執行關閉下架。

教材記載 AFCC DESK 在 Dashboard v10.0 加入，使用 `+ Service Request` 提出服務請求。實際可用權限依客戶帳號與服務內容而定。

## 五、推薦練習順序

先讀「品牌與服務」及「事件類型」，接著練習「SEARCH 搜尋」「下架計次」「下架流程」，最後再挑戰「客戶情境」。每題解析標明教材名稱及頁碼，請用對應版本交叉查核。

## 來源版本

- FraudAction Dashboard 一般使用者操作手冊（使用者提供；部分為舊版畫面）。
- FraudAction Dashboard 系統維護與管理手冊（使用者提供；部分為舊版畫面）。
- FraudAction Dashboard v13.5 升版說明（教材記載 2026 年 10 月）。

**不包含原始手冊、客戶機密、帳密或內部截圖。**
