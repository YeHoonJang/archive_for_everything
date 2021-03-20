




if __name__  == "__main__":
    # genres_set = [
    #     ['stunning drama', 'remarkable', 'extraordinary', 'staggering', 'incredible', 'outstanding', 'amazing'],
    #     ['motional', 'action-packed'],
    #     ['beautiful', 'attractive', 'pretty', 'charming', 'wonderful', 'fine', 'superb', 'terrific'],
    #     ['astounding', 'amazing', 'surprising', 'remarkable', 'staggering', 'breathtaking', 'extraordinary'],
    #     ['thrilling', 'exciting', 'stirring', 'rip-roaring', 'gripping'],
    #     ['fast-paced', 'quick-paced'],
    #     ['touching', 'moving', 'affecting', 'heartwarming', 'emotional', 'emotive', 'tender'],
    #     ['fanciful', 'visionary', 'fantastic', 'viewy', 'high-flown'],
    #     ['boring', 'tedious', 'bored', 'tiring', 'tiresome', 'weary'],
    #     ['awe-inspiring'],
    #     ['brilliant', 'shining', 'wonderful'],
    #     ['taut', 'strist']]
    # genres_set 내의 list는 하나의 장르에 대한 동의어들의 묶음으로 patent search expression 에서 or로 묶인 단어들의 set 입니다.

    # behavior_set = [['vanquish', 'win', 'beat', 'overcome', 'knead', 'mince'],
    #                 ['confront', 'face', 'challenge', 'accost', 'stand up to'],
    #                 ['pursue', 'follow', 'run after', 'chase', 'trail', 'stalk'],
    #                 ['redeem', 'save', 'vindicate', 'retrieve', 'regain', 'get back', 'reclaim', 'buy back'],
    #                 ['escape', 'getaway', 'breakout', 'jailbreak', 'bolt', 'flight', 'prolapse', 'evasion'],
    #                 ['fight', 'battle', 'quarrel', 'combat', 'wrestle', 'battle with'],
    #                 ['conquer', 'defeat', 'feat', 'trounce', 'constrain', 'repress', 'hold down', 'withhold',
    #                  'crucify'],
    #                 ['overcome', 'get the better', 'prevail over', 'control', 'get under control', 'master'],
    #                 ['find', 'discovery', 'acquisition', 'asset', 'detect'],
    #                 ['chase', 'pursuit', 'hunt', 'trail', 'follow up']]
    # behavior_set 내의 list는 주인공의 행동에 대한 동의어들의 묶음으로 patent search expression 에서 or로 묶인 단어들의 set 입니다.


    # 특허의 검색식 처럼 or로 묶일만한 동의어를 임의로 생성
    search_expression_1 = [['PMMA', 'phosphate', 'ammonia', 'nitrate', 'nitrite','silicate', 'nutrient', 'nutritive']]
    search_expression_2 = [['lab-on-a-chip', 'lab-on-chip', 'lab']]
    search_expression_3 = [['sensing', 'sensor', 'detect', 'analyze', 'measur', 'check']]
    # 임의로 하나의 특허동향보고서에서 추출한 검색식의 일부입니다. 하나의 list는 or로 묶인 단어들입니다.

    # genres_list = extract_validated_patent_id(genres_set)
    # behavior_list = extract_validated_patent_id(behavior_set)

    list_1 = extract_validated_patent_id(search_expression_1)
    list_2 = extract_validated_patent_id(search_expression_2)


    def intersect(a):
        return list(set(a) & set(b))

    # print(len(intersect(genres_list, behavior_list)))

