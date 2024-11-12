import pyto_ui as ui

web_view = ui.WebView()

with open("jb/index.html", encoding="utf-8") as htmlf:
    htmlstr = htmlf.read()
    web_view.load_html(htmlstr)

ui.show_view(web_view, mode=ui.PRESENTATION_MODE_FULLSCREEN)