from soynlp.hangle import jamo_levenshtein
import re, sys
def nlpfunction(mode, inputstring) :
    drink_list = []
    if mode == "food" :
        with open('./food.txt', 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                drink_list.append(line)
        print(drink_list)
    elif mode == "drink" :
        with open('./drink.txt', 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                drink_list.append(line)
        print(drink_list)


    input = inputstring
    hangul = re.compile('[^가-힣+]')
    ## 한글만 추출한 input text
    input_kor = hangul.sub('', input)

    dist_min = [sys.maxsize, '']
    for drink in drink_list:
        drink_kor = hangul.sub('', drink)
        dist = jamo_levenshtein(input_kor, drink_kor)
        if dist < dist_min[0]:
            dist_min = [dist, drink]

    if dist_min[0] > 2:
        dist_min[1] = None

    return dist_min[1]

