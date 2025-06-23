# 🐛 Issue 管理指南

## 📋 Issue 類型

### 🆕 Feature Request (功能請求)

**使用時機**: 提出新功能或功能改進建議

**模板**: [Feature Request Template](https://github.com/TobyWuNumOne/tutor-matching-platform/issues/new?template=feature_request.yml)

**必填內容**:

- 功能描述與目的
- 使用者價值說明  
- 技術實作建議
- 成功標準定義

### 🐛 Bug Report (錯誤回報)

**使用時機**: 發現系統錯誤或異常行為

**模板**: [Bug Report Template](https://github.com/TobyWuNumOne/tutor-matching-platform/issues/new?template=bug_report.yml)

**必填內容**:

- 問題描述與重現步驟
- 預期行為 vs 實際行為
- 環境資訊 (瀏覽器、OS等)
- 錯誤截圖或 log

### 📚 Documentation (文件)

**使用時機**: 文件缺失或需要更新

**內容包含**:

- 需要撰寫的文件類型
- 目標讀者群體
- 文件結構建議

### 🔧 Task (一般任務)

**使用時機**: 開發任務、環境設定、測試等

**內容包含**:

- 明確的任務描述
- 完成標準 (Acceptance Criteria)
- 技術需求說明
- 相關資源連結

## 🏷️ 標籤系統

### 按類型分類

```markdown
bug          - 錯誤回報
enhancement  - 功能增強
feature      - 新功能
documentation - 文件相關
task         - 一般任務
question     - 疑問討論
```

### 按優先級分類

```markdown
priority/high    - 🔴 高優先級
priority/medium  - 🟡 中優先級  
priority/low     - 🟢 低優先級
```

### 按功能模組分類

```markdown
auth         - 🔐 會員系統
matching     - 🛍️ 家教媒合
rating       - ⭐ 評價系統
payment      - 💳 交易系統
admin        - ⚙️ 後台管理
frontend     - 前端相關
backend      - 後端相關
ui/ux        - 設計相關
```

### 按狀態分類

```markdown
ready        - 準備開始
in-progress  - 進行中
blocked      - 被阻擋
needs-review - 需要審查
duplicate    - 重複問題
wontfix      - 不會修復
```

## ✍️ Issue 撰寫規範

### 📝 標題規範

```markdown
✅ 好的標題:
- "登入頁面密碼驗證失效"
- "新增老師評價功能"  
- "首頁載入速度過慢"

❌ 不好的標題:
- "有 bug"
- "功能不能用"
- "幫忙看一下"
```

### 📋 內容結構

```markdown
## 問題描述
清楚描述問題或需求

## 重現步驟 (Bug 專用)
1. 進入登入頁面
2. 輸入錯誤密碼
3. 點擊登入按鈕
4. 觀察錯誤訊息

## 預期行為
應該顯示「密碼錯誤」提示

## 實際行為  
頁面卡住沒有任何反應

## 環境資訊
- 瀏覽器: Chrome 91.0
- 作業系統: Windows 10
- 螢幕解析度: 1920x1080

## 其他資訊
錯誤發生在特定時間或條件下
```

## 🔄 Issue 生命週期

### 新建 Issue

```markdown
1. 選擇適當的模板
2. 填寫完整資訊
3. 設定適當標籤
4. 指派給對應人員 (如果確定)
5. 提交 Issue
```

### Issue 處理流程

```markdown
Open → Triaged → In Progress → Code Review → Testing → Closed
```

### 狀態說明

- **Open**: 新建立，等待處理
- **Triaged**: 已分類，等待指派
- **In Progress**: 正在處理中
- **Code Review**: 代碼審查階段
- **Testing**: 測試驗證階段  
- **Closed**: 已完成或已解決

## 🎯 Issue 指派原則

### 自動指派規則

```markdown
bug + frontend → 前端開發者
bug + backend → 後端開發者
enhancement + ui/ux → 設計師
documentation → 當前功能負責人
high priority → @TobyWuNumOne (PM)
```

### 手動指派考量

- **技能匹配**: 指派給最適合的開發者
- **工作負荷**: 考慮當前任務數量
- **學習機會**: 讓新成員參與適合的任務

## 📊 Issue 管理最佳實踐

### 📅 定期檢視

```markdown
每日 (PM):
- 檢視新 Issues
- 分類和標籤設定
- 緊急問題立即處理

每週 (團隊):
- Review 未解決的 Issues  
- 調整優先級
- 清理過期 Issues
```

### 🔗 關聯管理

```markdown
相關 Issues: 使用 "Related to #123"
重複 Issues: 關閉並標記 "Duplicate of #123"  
依賴關係: 使用 "Blocked by #123" 或 "Depends on #123"
PR 連結: 在 PR 中使用 "Closes #123"
```

### 📝 溝通規範

- **及時更新**: 有進展就留言更新
- **@mention**: 需要他人協助時明確標記
- **詳細記錄**: 重要決定和討論要記錄在 Issue 中
- **友善語氣**: 保持專業和友善的溝通語調

## 🆘 常見問題

**Q: Issue 太複雜該如何處理？**

>A: 拆分成多個子 Issues，用 Task List 連結

**Q: 不確定是 Bug 還是 Feature？**  

>A: 先開 Bug Report，討論後可以轉換類型

**Q: 如何追蹤 Issue 的處理進度？**

>A: 查看 GitHub Projects 或使用 Issue 的 Timeline

**Q: 可以關閉別人的 Issue 嗎？**

>A: 一般由 Issue 建立者或 PM 關閉，其他人建議留言說明
