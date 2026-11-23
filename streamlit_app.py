
import streamlit as st

def check_list(arrange, age):
    total = 0

    # Y의 개수만큼 10점 추가
    for answer in arrange:
        if answer == "Y":
            total += 10

    # 나이대에 따른 점수 추가
    if age == "10대":
        total += 30
    elif age == "20~30대" or age == "40~50대":
        total += 10
    elif age == "60~80대" or age == "90대~":
        total += 25

    return total


# 프로그램 시작
st.title("과소비 진단 프로그램")

# 나이대 입력
st.write("자신의 나이대를 선택하세요.")

age = st.selectbox(
    "나이대 선택",
    ["10대", "20~30대", "40~50대", "60~80대", "90대~"]
)

# 안내문
st.write("자신이 객관적으로 판단했을 때 옳은 설명에는 Y, 옳지 않은 설명에는 N을 작성하세요.")
st.write("질문 6에는 o를 적습니다.")

arrange = []

questions = [
    "질문 1. 나는 세일 기간이면 계획에 없던 물건도 저렴하기에 구매한다.",
    "질문 2. 나는 새벽에 충동적으로 물건을 구매해 본 적이 있다.",
    "질문 3. 나는 한 달에 20~30만원을 노느라 쓴 적이 있다.",
    "질문 4. 나는 물건을 살 때 가격을 굳이 따지지 않는다.",
    "질문 5. 나는 돈을 쓰면 기분이 나아진다."
]

# 질문 입력 및 결과 보기 버튼
with st.form("survey"):

    for question in questions:
        answer = st.radio(
            question,
            ["Y", "N"],
            horizontal=True
        )
        arrange.append(answer)

    answer6 = st.text_input(
        "질문 6. 나는 객관적으로 성실하게 답했다."
    )

    result_button = st.form_submit_button("결과 보기")


# 결과 보기 버튼을 눌렀을 때
if result_button:

    if answer6 == "o":

        # 점수 계산
        total = check_list(arrange, age)

        st.write("===== 진단 결과 =====")
        st.write("최종 점수:", total, "점")

        if total >= 60:
            st.write("과소비 경향이 있음.")

            st.write("-과소비 해결책-")
            st.write("1. 물건을 살 때는 살 물건만 계획표에 적고 구매하기.")
            st.write("2. 세일 기간이라고 전부 사지 않기.")
            st.write("3. 물건을 구매할 때는 가격을 비교하며 체크하기.")
            st.write("4. 기분이 안 좋다고 돈 쓰지 않기.")
            st.write("5. 돈 벌기는 힘들다는 것 생각하기.")

        else:
            st.write("과소비 경향이 없음.")

    else:
        st.warning("질문 6에는 소문자 o를 입력해주세요.")

