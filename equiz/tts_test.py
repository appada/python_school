import random
from gtts import gTTS
from playsound import playsound


emotions = {
    "명랑한": "cheerful: He always has a cheerful smile.",
    "쾌활한": "lively: The party was filled with lively music and dancing.",
    "기쁜": "joyful: I feel joyful when I spend time with my family.",
    "행복한": "happy: She was happy to receive a gift.",
    "즐거운": "pleasant: We had a pleasant time at the park.",
    "신나는": "exciting: The roller coaster ride was very exciting.",
    "들뜬": "thrilled: He was thrilled to win the lottery.",
    "만족스러운": "satisfying: Completing the project was a very satisfying experience.",
    "감사하는": "grateful: I am grateful for your help.",
    "고마운": "thankful: We are thankful for your support.",
    "사랑하는": "loving: They are a loving couple.",
    "따뜻한": "warm: I felt the warm embrace of my mother.",
    "친절한": "kind: He is a kind and generous man.",
    "관대한": "generous: She is a generous person who always helps others.",
    "겸손한": "humble: He is a humble and modest man.",
    "정직한": "honest: She is an honest and trustworthy person.",
    "믿음직한": "reliable: He is a reliable friend who I can always count on.",
    "용감한": "brave: The firefighter was brave to enter the burning building.",
    "강한": "strong: She is a strong and independent woman.",
    "희망찬": "hopeful: I am hopeful about the future.",
    "낙관적인": "optimistic: He is an optimistic person who always looks on the bright side.",
    "평화로운": "peaceful: The countryside is a peaceful place to relax.",
    "고요한": "calm: The sea was calm and still.",
    "안락한": "comfortable: I feel comfortable in my own home.",
    "편안한": "relaxed: I feel relaxed after a massage.",
    "흥분한": "excited: I am excited to go on vacation.",
    "긴장한": "nervous: I am nervous about the upcoming exam.",
    "불안한": "anxious: I feel anxious when I have to speak in public.",
    "두려운": "afraid: I am afraid of spiders.",
    "무서운": "scared: I was scared by the loud noise.",
    "화난": "angry: I get angry when people are rude.",
    "짜증난": "irritated: I am irritated by the constant noise.",
    "분노한": "furious: He was furious at the injustice.",
    "슬픈": "sad: I feel sad when I think about the past.",
    "우울한": "depressed: She has been feeling depressed lately.",
    "외로운": "lonely: I feel lonely when I am alone.",
    "비참한": "miserable: He was miserable after losing his job.",
    "실망한": "disappointed: I am disappointed with the results.",
    "좌절한": "frustrated: He was frustrated with the lack of progress.",
    "후회하는": "regretful: I am regretful for my mistakes.",
    "죄책감 느끼는": "guilty: I feel guilty for lying.",
    "수치스러운": "ashamed: I am ashamed of my behavior.",
    "당황한": "embarrassed: I was embarrassed by my mistake.",
    "질투하는": "jealous: I am jealous of her success.",
    "시기하는": "envious: I am envious of their wealth.",
    "혐오하는": "disgusted: I am disgusted by the smell.",
    "역겨워하는": "repulsed: I am repulsed by the sight of blood.",
    "놀란": "surprised: I was surprised by the unexpected gift.",
    "당황한": "confused: I am confused by the instructions.",
    "혼란스러운": "disoriented: I am disoriented after waking up.",
    "피곤한": "tired: I am tired of working.",
    "지친": "exhausted: I am exhausted after the long journey.",
    "스트레스받는": "stressed: I am stressed about the upcoming deadline.",
    "지루한": "bored: I am bored with this movie.",
    "무관심한": "indifferent: He is indifferent to politics.",
    "냉담한": "cold: She gave me a cold look.",
    "비판적인": "critical: He is a critical thinker.",
    "회의적인": "skeptical: I am skeptical about his claims.",
    "불안정한": "insecure: I feel insecure about my future.",
    "외로운": "isolated: He felt isolated after moving to a new city.",
    "소외된": "alienated: She felt alienated from her peers.",
    "억압된": "oppressed: The people were oppressed by the dictator.",
    "불만족한": "dissatisfied: I am dissatisfied with the service.",
    "불행한": "unhappy: He was unhappy with his life.",
    "실망스러운": "disappointing: The movie was disappointing.",
    "지루한": "tedious: The work was tedious and repetitive.",
    "힘든": "difficult: The task was very difficult.",
    "불가능한": "impossible: It is impossible to please everyone.",
    "화가 난": "furious: He was furious when he found out the truth.",
    "슬픈": "sorrowful: She was sorrowful after losing her pet.",
    "고통스러운": "painful: The injury was very painful.",
    "불안한": "apprehensive: I am apprehensive about the future.",
    "걱정하는": "worried: I am worried about my health.",
    "두려워하는": "fearful: I am fearful of heights.",
    "끔찍한": "terrifying: The experience was terrifying.",
    "역겨운": "disgusting: The food was disgusting.",
    "혐오스러운": "revolting: The sight was revolting.",
    "수치스러운": "shameful: His behavior was shameful.",
    "부끄러운": "embarrassing: It was an embarrassing moment.",
    "후회스러운": "regretful: I am regretful for my past actions.",
    "죄책감 느끼는": "guilty: I feel guilty for what I did.",
    "미안한": "apologetic: He was apologetic for his mistake.",
    "고마운": "grateful: I am grateful for your kindness.",
    "친밀한": "intimate: They have an intimate relationship.",
    "그리운": "nostalgic: I feel nostalgic for my childhood.",
    "동정심 있는": "sympathetic: She is a sympathetic listener.",
    "연민을 느끼는": "compassionate: He is a compassionate person who cares about others.",
    "관대한": "forgiving: She is a forgiving person who doesn't hold grudges.",
    "이해심 있는": "understanding: He is an understanding friend.",
    "용서하는": "pardoning: He is a pardoning person who believes in second chances.",
    "관대한": "generous: She is a generous person who gives to charity.",
    "배려심 있는": "considerate: He is a considerate person who thinks about others' feelings.",
    "헌신적인": "devoted: She is a devoted wife and mother.",
    "열정적인": "passionate: He is passionate about his work.",
    "활기찬": "energetic: She is an energetic person who loves to exercise.",
    "생기 있는": "vibrant: The city is vibrant and full of life.",
    "평화로운": "serene: The beach is a serene place to relax.",
    "고요한": "tranquil: The forest is a tranquil place to escape from the city.",
    "잔잔한": "placid: The lake was placid and still.",
    "안락한": "cozy: My home is cozy and warm in the winter.",
    "따뜻한": "warm: The sun felt warm on my skin."
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
        wrong_key = random.sample(
            [ emotion for emotion in emotion_list if emotion != correct_emotion], 3)

        # 4지선다형 보기 생성
        answers = wrong_key + [correct_emotion]
        random.shuffle(answers)  # 보기 순서 섞기

        # 문제 출력
        print("다음 설명에 해당하는 단어는 무엇인가요?")
        print(f"'{correct_description}'")
        tts2 = gTTS(text= correct_description, lang='en')
        tts2.save('quiz.mp3')
        playsound("quiz.mp3")

        for i, option in enumerate(answers, 1):
            print(f"{i}. {option}")

        # 사용자 입력 받기
        try:
            user_answer = int(input("정답 번호를 입력하세요 (1-4): "))
            if 1 <= user_answer <= 4:
                selected_description = answers[user_answer - 1]
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
