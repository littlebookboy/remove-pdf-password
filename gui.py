#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import os
from pathlib import Path
from dotenv import load_dotenv
import pymupdf as fitz

# 載入環境變數
load_dotenv()


def remove_pdf_password(input_pdf, output_pdf, password):
    """移除 PDF 密碼，回傳 (成功, 訊息)"""
    if not os.path.exists(input_pdf):
        return False, f"檔案不存在：{input_pdf}"

    output_dir = os.path.dirname(output_pdf)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    doc = fitz.open(input_pdf)

    if not doc.needs_pass:
        doc.save(output_pdf)
        doc.close()
        return True, f"此 PDF 無密碼保護，已直接複製至：\n{output_pdf}"

    if doc.authenticate(password):
        doc.save(output_pdf)
        doc.close()
        return True, f"密碼已移除，輸出檔案：\n{output_pdf}"
    else:
        doc.close()
        return False, "密碼錯誤，無法解密 PDF！"


def generate_output_path(input_pdf):
    """產生輸出檔案路徑"""
    input_path = Path(input_pdf)
    script_dir = Path(__file__).parent
    output_dir = script_dir / "output"
    output_filename = f"{input_path.stem}-unlock{input_path.suffix}"
    return str(output_dir / output_filename)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF 密碼移除工具")
        self.root.resizable(False, False)
        self.selected_file = None

        # 密碼檢查
        self.password = os.getenv("PDF_PASSWORD")

        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack()

        # 標題
        tk.Label(frame, text="PDF 密碼移除工具", font=("", 16, "bold")).pack(pady=(0, 15))

        # 選擇檔案按鈕
        tk.Button(frame, text="選擇 PDF 檔案", command=self.choose_file, width=20).pack()

        # 檔案路徑顯示
        self.file_label = tk.Label(frame, text="尚未選擇檔案", fg="gray", wraplength=350)
        self.file_label.pack(pady=(5, 15))

        # 移除密碼按鈕
        self.run_btn = tk.Button(
            frame, text="移除密碼", command=self.run, width=20, state=tk.DISABLED
        )
        self.run_btn.pack()

        # 狀態顯示
        self.status_label = tk.Label(frame, text="", wraplength=350, justify=tk.LEFT)
        self.status_label.pack(pady=(15, 0))

        # 若無密碼，顯示錯誤
        if not self.password:
            self.set_status("請在 .env 檔案中設定 PDF_PASSWORD", "red")

    def choose_file(self):
        path = filedialog.askopenfilename(filetypes=[("PDF 檔案", "*.pdf")])
        if path:
            self.selected_file = path
            self.file_label.config(text=path, fg="black")
            if self.password:
                self.run_btn.config(state=tk.NORMAL)
            self.set_status("", "black")

    def run(self):
        if not self.selected_file:
            return

        self.run_btn.config(state=tk.DISABLED)
        self.set_status("處理中...", "blue")
        self.root.update()

        output_pdf = generate_output_path(self.selected_file)

        try:
            success, msg = remove_pdf_password(self.selected_file, output_pdf, self.password)
            color = "green" if success else "red"
            self.set_status(msg, color)
        except Exception as e:
            self.set_status(f"處理錯誤：{e}", "red")

        self.run_btn.config(state=tk.NORMAL)

    def set_status(self, text, color="black"):
        self.status_label.config(text=text, fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
