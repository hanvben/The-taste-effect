import streamlit as st
import random

def ask_question(question):
    answer = st.radio(f"{question}", options=[1, 2, 3, 4, 5], index=2)
    return answer

def recommend_food(taste):
    food_options = {
        "단맛": ["초콜릿", "바나나", "고구마", "딸기 스무디", "허니브레드"],
        "쓴맛": ["다크 초콜릿", "커피", "녹차", "아몬드", "브로콜리"],
        "짠맛": ["김치찌개", "감자칩", "치즈", "훈제 연어", "된장국"],
        "신맛": ["레몬차", "요거트", "자몽", "식초 드레싱 샐러드", "오렌지"],
        "매운맛": ["떡볶이", "김치볶음밥", "핫치킨", "마라탕", "핫소스 버거"],
        "감칠맛": ["된장찌개", "미소된장국", "치킨 수프", "토마토 파스타", "파마산 치즈"]
    }
    return random.choice(food_options[taste])

def emotion_test():
    st.title("📝 감정 진단 테스트")
    st.write("각 질문에 1~5로 응답해주세요. (1-전혀 아니다, 5-매우 그렇다)")

    questions = [
        "지금 기분이 전반적으로 즐겁다.",
        "오늘 하루 동안 웃는 일이 많았다.",
        "주변 사람들과 긍정적인 관계를 유지하고 있다.",
        "이유 없이 불안하거나 초조한 기분이 든다.",
        "집중이 잘되지 않거나 산만하다.",
        "몸이 긴장되어 있거나 근육이 뻣뻣하게 느껴진다.",
        "몸이 무겁거나 쉽게 피로감을 느낀다.",
        "최근 고민이 많고 압박감을 느낀다.",
        "쉬어도 피곤함이 해소되지 않는다.",
        "평소에 좋아하던 일에도 흥미가 없다.",
        "무기력하거나 아무것도 하고 싶지 않다.",
        "이유 없이 기분이 가라앉거나 슬프다.",
        "현재 집중이 잘 되고 있다.",
        "머리가 맑고 명확한 느낌이 든다.",
        "현재 에너지가 넘치고 활력이 느껴진다."
    ]

    scores = [ask_question(q) for q in questions]
    total_score = sum(scores)

    if total_score >= 60:
        emotion_state = "전반적으로 감정 상태가 긍정적이고, 활력이 넘침 😊"
        recommended_taste = "신맛"
    elif total_score >= 45:
        emotion_state = "감정이 비교적 안정적이지만, 일부 스트레스나 피로가 있음 🙂"
        recommended_taste = "단맛"
    elif total_score >= 30:
        emotion_state = "피로, 스트레스, 불안이 누적될 가능성이 있음 😐"
        recommended_taste = "짠맛"
    else:
        emotion_state = "감정 기복이 크거나, 스트레스·우울이 높은 상태 😞"
        recommended_taste = "매운맛"

    recommended_food = recommend_food(recommended_taste)

    if st.button("결과 보기"):
        st.subheader("📊 감정 진단 결과:")
        st.write(f"총점: {total_score}점")
        st.write(f"현재 상태: {emotion_state}")
        st.write(f"🍽️ 추천 맛: {recommended_taste}")
        st.write(f"🥘 추천 음식: {recommended_food}")

if __name__ == "__main__":
    emotion_test()
