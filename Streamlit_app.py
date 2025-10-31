import streamlit as st

st.set_page_config(page_title="📖 나의 공개 글 페이지", layout="centered")

st.title("📝 내 실시간 글 페이지")
st.caption("이 페이지는 GitHub에서 파일이 업데이트되면 자동으로 최신 내용으로 갱신됩니다.")

# data.txt 파일 읽기
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    text = "(아직 글이 없습니다. data.txt 파일을 만들어 보세요.)"

# 화면에 표시
st.markdown("---")
st.markdown(f"### 📜 현재 내용\n\n{text}")
st.markdown("---")

st.info("이 글은 GitHub 저장소의 `data.txt`에서 불러옵니다. 파일을 수정 후 commit & push 하면 자동 반영됩니다.")