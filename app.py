import gradio as gr
import pyshorteners as ps
def do(url):
    return ps.Shortener().clckru.short(url)
iface=gr.Interface(fn=do,title='縮網址工具',description='只要輸入一個網址我們就會幫你縮短。[縮短後進去那個網址可能會有小廣告(不一定)]',inputs='text',outputs='text')
iface.launch(share=True)
