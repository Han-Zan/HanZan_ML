from soynlp.hangle import jamo_levenshtein
import re, sys
def nlpfunction(mode, inputstring) :
    hangul = re.compile('[^가-힣+]')
    drink_list = []
    if mode == "food" :
        with open('./food.txt', 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                drink_list.append(line)
    elif mode == "drink" :
        with open('./drink.txt', 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                drink_list.append(line)


    input = inputstring



    ## 한글만 추출한 input text
    input_kor = hangul.sub('', input)

    print(input_kor)

    returnstr = None;
    dist_min = [2.0, '']
    for drink in drink_list:
        drink_kor = hangul.sub('', drink)
        if drink_kor in input_kor:
            returnstr = drink;
        dist = jamo_levenshtein(input_kor, drink_kor)
        if dist < dist_min[0]:
            dist_min = [dist, drink]


    if dist_min[0] > 1.8:
        if returnstr == None :
            returnstr = "None"
    else:
        returnstr = dist_min[1]

    if returnstr == None:
        return "None"


    return returnstr

