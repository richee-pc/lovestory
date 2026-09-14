import os
import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정: 와이드 레이아웃 및 브라우저 타이틀 지정
st.set_page_config(
    page_title="Closer (클로저) - AI 관계 심리 코칭",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit 기본 상단 바, 패딩 및 여백을 제거하여 전체 화면 웹앱처럼 표시
hide_streamlit_style = """
    <style>
        /* 상단 헤더, 푸터 및 메인 여백 제거 */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* 뷰포트 여백 초기화 */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        /* iframe 컨테이너 테두리 제거 */
        iframe {
            border: none !important;
            width: 100% !important;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 현재 스크립트 실행 위치 기준 'htmls/index.html' 절대/상대 경로 탐색
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "htmls", "index.html")

# 만약 루트에 바로 있거나 경로 구조가 다를 경우를 대비한 fallback 탐색
if not os.path.exists(html_path):
    fallback_path = os.path.join(current_dir, "index.html")
    if os.path.exists(fallback_path):
        html_path = fallback_path

if os.path.exists(html_path):
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # iframe 높이를 충분히 확보(960px)하고 스크롤을 활성화하여 완벽히 구동되도록 렌더링
        components.html(html_content, height=980, scrolling=True)

    except Exception as e:
        st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")
else:
    st.error(
        f"🚨 'htmls/index.html' 파일을 찾을 수 없습니다.\n\n"
        f"현재 프로젝트 폴더 구조를 확인해 주세요:\n"
        f"- app.py\n"
        f"- htmls/\n"
        f"   └── index.html"
    )
