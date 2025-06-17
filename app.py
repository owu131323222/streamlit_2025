import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import font_config  # フォント設定をインポート


# 日本語フォントを設定
rcParams['font.family'] = 'Meiryo'  # Windowsの場合は「Meiryo」を指定

# タイトルを中央揃え
st.markdown(
    "<h1 style='text-align: center;'>模試結果分析アプリ</h1>",
    unsafe_allow_html=True
)

subjects = ["国語", "数学", "英語", "理科", "社会"]
scores = {}

# セクションヘッダーを中央揃え
st.markdown(
    "<h2 style='text-align: center;'>模試の点数を入力してください</h2>",
    unsafe_allow_html=True
)

# 各科目ごとに色を設定
colors = {
    "国語": "#FF6F61",  # 赤っぽいピンク
    "数学": "#4A90E2",  # きれいな青
    "英語": "#A461D8",  # きれいな紫
    "理科": "#50C878",  # きれいな緑
    "社会": "#FFA500"   # きれいなオレンジ
}

for subject in subjects:
    # 色付きのラベルを表示
    st.markdown(
        f'<h4 style="color: {colors[subject]};">{subject} の点数入力</h4>',
        unsafe_allow_html=True
    )
    # スライダーを表示
    scores[subject] = st.slider("", min_value=0, max_value=100, value=50, key=f"slider_{subject}")

# 目標点の入力
st.markdown("<h4>目標点を入力</h4>", unsafe_allow_html=True)  # 大きな文字で表示
target_score = st.slider("", min_value=0, max_value=100, value=100)

# 過去のデータを保存
if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.append(scores)

# データフレーム作成
df = pd.DataFrame(scores.items(), columns=["科目", "得点"])
df["目標点との差"] = target_score - df["得点"]

# 成績のグラフ表示（横軸ラベルを科目名に修正）
st.subheader("模試結果の分析")

fig, ax = plt.subplots()
ax.bar(df["科目"], df["得点"], color="blue", label="得点")

# 目標点の赤い点線
ax.axhline(target_score, color='red', linestyle="--", label="目標点")

# 科目名を横軸ラベルとして設定
ax.set_xticks(range(len(df["科目"])))
ax.set_xticklabels(df["科目"], rotation=0)

ax.set_ylabel("点数")
ax.set_xlabel("科目")
ax.legend()
st.pyplot(fig)

# 苦手科目のリストアップ
st.subheader("苦手科目のリスト")
weak_subjects = df[df["得点"] < target_score]["科目"].tolist()
if weak_subjects:
    # 「もっと勉強が必要な科目」の文字色を赤く強調
    st.markdown(
        f"<span style='color: #FF0000; font-weight: bold; font-size: 20px;'>もっと勉強が必要な科目:</span> "
        f"<span style='font-size: 20px;'>{', '.join(weak_subjects)}</span>",
        unsafe_allow_html=True
    )
else:
    # 「すべての科目で目標達成！」の文字色を緑で強調
    st.markdown(
        "<span style='color: #008000; font-weight: bold; font-size: 20px;'>すべての科目で目標達成！</span>",
        unsafe_allow_html=True
    )
