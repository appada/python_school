import random


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
    "frustrated": "좌절한, He was frustrated with the lack of progress.",
    "guilty": "죄책감을 느끼는, She felt guilty for lying.",
    "ashamed": "부끄러워하는, He was ashamed of his behavior.",
    "angry": "화난, I get angry when people are rude.",
    "furious": "격분한, He was furious at the injustice.",
    "irritated": "짜증난, I am irritated by the noise.",
    "annoyed": "귀찮은, She was annoyed by his constant questions.",
    "resentful": "원망하는, She felt resentful towards her ex-boyfriend.",
    "bitter": "쓰라린, He felt bitter about his past failures.",
    "jealous": "질투하는, She was jealous of her friend's success.",
    "envious": "부러워하는, He was envious of their wealth.",
    "vengeful": "복수심에 불타는, She felt vengeful after being betrayed.",
    "afraid": "두려워하는, I am afraid of spiders.",
    "scared": "무서워하는, She was scared by the loud noise.",
    "frightened": "겁먹은, He was frightened by the dark alley.",
    "terrified": "공포에 질린, She was terrified of public speaking.",
    "anxious": "불안한, I feel anxious before exams.",
    "nervous": "긴장한, He was nervous about the interview.",
    "worried": "걱정하는, I am worried about my health.",
    "apprehensive": "불안해하는, She felt apprehensive about the future.",
    "panicked": "당황한, He panicked when he realized he was lost.",
    "insecure": "불안정한, She felt insecure about her appearance.",
    "surprised": "놀란, I was surprised by the unexpected gift.",
    "amazed": "놀라운, She was amazed by his talent.",
    "astonished": "깜짝 놀란, He was astonished by the news.",
    "stunned": "멍한, She was stunned into silence.",
    "shocked": "충격받은, He was shocked by the accident.",
    "dumbfounded": "어리둥절한, She was dumbfounded by his behavior.",
    "awestruck": "경외로운, He was awestruck by the beauty of the landscape.",
    "overwhelmed": "압도된, She was overwhelmed by the amount of work.",
    "confused": "혼란스러운, I am confused by the instructions.",
    "disoriented": "방향 감각을 잃은, He was disoriented after waking up.",
    "disgusted": "역겨운, I am disgusted by the smell.",
    "repulsed": "혐오감을 느끼는, She was repulsed by the sight of blood.",
    "nauseated": "메스꺼운, I feel nauseated after eating too much.",
    "sickened": "진저리 쳐지는, He was sickened by the violence.",
    "revolted": "분개하는, She was revolted by the injustice.",
    "appalled": "경악하는, He was appalled by the living conditions.",
    "horrified": "공포에 질린, She was horrified by the accident scene.",
    "outraged": "격분한, He was outraged by the decision.",
    "disapproving": "못마땅한, She gave him a disapproving look.",
    "skeptical": "회의적인, I am skeptical about his claims.",
    "hopeful": "희망적인, I am hopeful about the future.",
    "optimistic": "낙관적인, She is optimistic about the project.",
    "pessimistic": "비관적인, He is pessimistic about the economy.",
    "curious": "호기심 많은, I am curious about the world.",
    "interested": "관심 있는, She is interested in learning new things.",
    "bored": "지루한, I am bored with this movie.",
    "tired": "피곤한, I am tired of working.",
    "exhausted": "기진맥진한, She was exhausted after the long journey.",
    "stressed": "스트레스받는, I am stressed about the upcoming deadline.",
    "proud": "자랑스러운, She was proud of her accomplishments.",
    "confident": "자신감 있는, He was confident in his abilities.",
    "successful": "성공적인, He felt successful after closing the deal.",
    "accomplished": "성취감 있는, She felt accomplished after finishing the project.",
    "important": "중요한, He felt important when he was giving the speech.",
    "respected": "존경받는, She felt respected by her colleagues.",
    "admired": "존경받는, He was admired by his students.",
    "honored": "영광스러운, She was honored to receive the award.",
    "dignified": "위엄 있는, He maintained a dignified silence.",
    "humiliated": "모욕적인, She felt humiliated by the public criticism.",
    "mortified": "창피한, He was mortified by his embarrassing moment.",
    "disgraced": "불명예스러운, She felt disgraced by the scandal.",
    "regretful": "후회하는, He felt regretful for his actions.",
    "remorseful": "뉘우치는, She was remorseful for her mistakes.",
    "contrite": "뉘우치는, He was contrite for his wrongdoing.",
    "penitent": "회개하는, She was penitent for her sins.",
    "peaceful": "평화로운, I feel peaceful when I am in nature.",
    "calm": "침착한, She was calm despite the chaos.",
    "relaxed": "편안한, I feel relaxed after a massage.",
    "serene": "고요한, The lake was serene and beautiful.",
    "tranquil": "평온한, The forest was tranquil and peaceful.",
    "loving": "사랑하는, I feel loving towards my family.",
    "caring": "배려심 많은, She is a caring and compassionate person.",
    "compassionate": "동정심 많은, He felt compassion for the suffering people.",
    "affectionate": "애정 어린, She was affectionate towards her children.",
    "passionate": "열정적인, He is passionate about his work."
}

emotion_key = list(emotions.keys())
emotion_values = list(emotions.values())
print(emotion_key)
print(emotion_values)

#점수세기
score = 0
total = 0

#퀴즈반복
while True:
    정답감정 = random.choice(emotion_key)
    정답설명 = emotions[정답감정]

    #정답으로 사용하지 않을 3개의 지문, 밸류값만 가져온다.
    다른지문들 = []
    for emotion in emotion_key:
        if emotion != 정답감정:
            다른지문들.append(emotions[emotion])
    #
    print(다른지문들)
    #3개를 랜덤으로 고른다.
    정답말고들 = random.sample(다른지문들, 3)
    
    print(정답말고들)
    
    모든설명 = 정답말고들 + [정답설명]
    #섞어
    random.shuffle(모든설명)

    #문제를 화면에 출력
    print(" 다음 설명 중 맞는 단어를 선택하세요 :")
    print(f"[  {정답감정}   ]")
    for index, description in enumerate(모든설명):
        print(f"{index +1} , {description}")

    #답변 입력받기
    user_answer = int(input("정답 번호를 입력하세요 (1-4): "))

    # 정답 확인
    if 모든설명[user_answer - 1] == 정답설명:
        print("정답입니다! 🎉\n")
    else:
        print(f"오답입니다. = > '{정답설명}'입니다. \n")

    # 0 입력하면 종료
    if user_answer == 0 :
         break
    


