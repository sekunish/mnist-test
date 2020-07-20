import sys
import tkinter as tk


class TKApp(tk.Frame):
    def __init__(self, master=None):
        '''
        コンストラクタ
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        self.btnReadImg = tk.Button(self)
        self.btnReadImg['text'] = 'image...'
        self.btnReadImg['command'] = self.btnReadImg_click

    def btnReadImg_click(self):
        print("test")


def main():
    # トップレベルのインスタンス作成
    root = tk.Tk()
    root.minsize(width=1024, height=768)
    root.title('number hit')
    # フォーム作成
    app = TKApp(master=root)
    # 処理開始    
    app.mainloop()


if __name__ == '__main__':
    main()
