import matplotlib.font_manager as fm

# 日本語フォントを指定
font_path = fm.findfont(fm.FontProperties(family='Meiryo'))
fm.fontManager.addfont(font_path)
