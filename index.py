#!/usr/bin/env python3
import pymupdf as fitz
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

def remove_pdf_password(input_pdf, output_pdf, password):
    """移除 PDF 密碼"""
    try:
        # 檢查輸入檔案是否存在
        if not os.path.exists(input_pdf):
            print(f"❌ 檔案不存在：{input_pdf}")
            return False

        # 確保輸出目錄存在
        output_dir = os.path.dirname(output_pdf)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
            print(f"📁 建立輸出目錄：{output_dir}")

        # 打開加密的 PDF
        print(f"📄 正在處理：{input_pdf}")
        doc = fitz.open(input_pdf)

        # 檢查是否需要密碼
        if not doc.needs_pass:
            print("ℹ️  此 PDF 沒有密碼保護，直接複製...")
            doc.save(output_pdf)
            doc.close()
            print(f"✅ PDF 已複製至：{output_pdf}")
            return True

        # 嘗試解鎖 PDF
        if doc.authenticate(password):
            print("🔓 密碼驗證成功，正在移除密碼...")
            doc.save(output_pdf)
            doc.close()
            print(f"✅ PDF 密碼已移除，輸出檔案：{output_pdf}")
            return True
        else:
            doc.close()
            print("❌ 密碼錯誤，無法解密 PDF！")
            return False

    except Exception as e:
        print(f"❌ 處理過程中發生錯誤：{e}")
        return False

# 從環境變數取得密碼
PDF_PASSWORD = os.getenv('PDF_PASSWORD')
if not PDF_PASSWORD:
    print("❌ 請在 .env 檔案中設定 PDF_PASSWORD")
    sys.exit(1)

def get_user_input():
    """取得使用者輸入"""
    print("=== PDF 密碼移除工具 ===\n")

    # 取得輸入檔案路徑
    while True:
        input_pdf = input("請輸入加密 PDF 檔案路徑：").strip().strip('"\'')
        if os.path.exists(input_pdf):
            break
        print("❌ 檔案不存在，請重新輸入")

    return input_pdf

def generate_output_path(input_pdf):
    """產生輸出檔案路徑，固定放在 output 目錄"""
    input_path = Path(input_pdf)
    script_dir = Path(__file__).parent
    output_dir = script_dir / "output"
    output_filename = f"{input_path.stem}-unlock{input_path.suffix}"
    return str(output_dir / output_filename)

def main():
    """主程式"""
    # 檢查命令列參數
    if len(sys.argv) == 2:
        # 使用命令列參數：檔案路徑
        input_pdf = sys.argv[1]
    else:
        # 使用互動式輸入
        input_pdf = get_user_input()

    # 使用環境變數密碼
    password = PDF_PASSWORD

    # 自動產生輸出路徑
    output_pdf = generate_output_path(input_pdf)

    # 執行密碼移除
    success = remove_pdf_password(input_pdf, output_pdf, password)

    if success:
        print("\n🎉 處理完成！")
    else:
        print("\n💥 處理失敗！")
        sys.exit(1)

if __name__ == "__main__":
    main()