import tkinter as tk
import time

def create_silent_app():
    # メインウィンドウの作成
    root = tk.Tk()
    root.title("4'33\"")
    
    # フルスクリーン設定
    root.attributes('-fullscreen', True)
    
    # 背景を白に設定
    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill="both", expand=True)
    
    # 4分33秒（273秒）後にアプリケーションを終了する関数
    def close_app():
        root.destroy()
    
    # 4分33秒後に終了するようにスケジュール
    root.after(273000, close_app)
    
    # アプリケーションの実行
    root.mainloop()

if __name__ == "__main__":
    create_silent_app()