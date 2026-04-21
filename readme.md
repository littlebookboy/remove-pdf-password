# PDF 密碼移除工具

PDF 密碼移除工具，就是這樣。

## 🚀 快速開始

### 1. 環境準備
```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境 (macOS/Linux)
source venv/bin/activate

# 安裝相依套件
pip install -r requirements.txt
```

### 2. 環境變數設定
需建立 `.env` 設定檔：
```env
PDF_PASSWORD=pw
```

### 3. 執行方式

#### CLI 模式
```bash
python index.py "被加密的 pdf 檔案絕對路徑 (包含檔案名)"

# 例如
python index.py "/Users/user/Downloads/target.pdf"

# 🗂 含空格檔案路徑
python index.py "~/Desktop/target file.pdf"
```

#### GUI 模式
```bash
python gui.py
```
開啟圖形介面，點擊「選擇 PDF 檔案」→「移除密碼」即可。

### 📤 輸出範例
| 輸入檔案 | 輸出位置 |
|---------|---------|
| `pdf.pdf` | `output/pdf-unlock.pdf` |

## 📦 相依套件
- **PyMuPDF** `1.26.5` - PDF 操作核心引擎
- **python-dotenv** `1.0.0` - 環境變數載入工具

## 📁 專案結構
```
remove_pdf_password/
├── 📄 index.py        # CLI 模式
├── 🖥 gui.py          # GUI 模式
├── 📝 requirements.txt 
├── 📖 readme.md
├── 🔒 .env 
├── 🚫 .gitignore  
└── 📂 output/
```
