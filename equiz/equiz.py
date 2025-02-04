import random

# 감정과 설명이 포함된 딕셔너리
emotions = {
    "joyful": "기쁜, I feel joyful when I spend time with my family.",
    "happy": "행복한, She was happy to receive a gift.",
    "excited": "신난, We are excited about our upcoming vacation.",
    "delighted": "매우 기쁜, He was delighted with the results.",
    "elated": "환희에 찬, She felt elated after winning the competition.",
    "cheerful": "명랑한, He always has a cheerful smile.",
    "content": "만족하는, I am content with my life.",
    "satisfied": "만족한, She was satisfied with her performance.",
    "grateful": "감사하는, I am grateful for your help.",
    "thankful": "고마워하는, We are thankful for your support.",
    "sad": "슬픈, I feel sad when I think about the past.",
    "unhappy": "불행한, He was unhappy with the situation.",
    "depressed": "우울한, She has been feeling depressed lately.",
    "lonely": "외로운, I feel lonely when I am alone.",
    "miserable": "비참한, He was miserable after losing his job.",
    "heartbroken": "상심한, She was heartbroken after the breakup.",
    "disappointed": "실망한, I am disappointed with the results.",
}

# 퀴즈 함수
def emotion_quiz():
    # 감정 리스트
    emotion_list = list(emotions.keys())
    
    while True:
        # 랜덤으로 정답 감정 선택
        correct_emotion = random.choice(emotion_list)
        correct_description = emotions[correct_emotion]
        
        # 오답 후보 3개 선택 (정답과 중복되지 않도록)
        wrong_descriptions = random.sample([emotions[emotion] for emotion in emotion_list if emotion != correct_emotion], 3)
        
        # 4지선다형 보기 생성
        options = wrong_descriptions + [correct_description]
        random.shuffle(options)  # 보기 순서 섞기
        
        # 문제 출력
        print(f"다음 설명에 해당하는 감정은 무엇인가요?")
        print(f"'{correct_emotion}'")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        # 사용자 입력 받기
        try:
            user_answer = int(input("정답 번호를 입력하세요 (1-4): "))
            if 1 <= user_answer <= 4:
                selected_description = options[user_answer - 1]
                if selected_description == correct_description:
                    print("정답입니다! 🎉\n")
                    #break  # 정답이면 퀴즈 종료
                else:
                    print("틀렸습니다. 다시 시도해보세요.\n")
            else:
                print("1에서 4 사이의 숫자를 입력하세요.\n")
        except ValueError:
            print("숫자를 입력하세요.\n")

# 퀴즈 실행
emotion_quiz()