from django.shortcuts import render
import re
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import os

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['text']
    
    #특수문자, 숫자 제거
    text=text.translate(str.maketrans('', '', string.punctuation))
    
    text_lsit=text.split()
    
    # 영어 소문자로 변환 
    for eng in range(len(text_lsit)):
        if text_lsit[eng].isalpha():
            text_lsit[eng]=text_lsit[eng].lower()
    
    text_dic={}
    for word in text_lsit:
        if word in text_dic:
            text_dic[word] +=1
        else:
            text_dic[word] = 1
    
    text_dic2={}
    for k, v in text_dic.items():
        if v>2:
            text_dic2[k]=v
                                
    wc = WordCloud(width=1000, height=600, background_color="white", random_state=0, font_path=r'c:\Windows\Fonts\malgun.ttf')
    plt.imshow(wc.generate_from_frequencies(text_dic2))
    plt.axis("off")
    plt.show()    
    plt.savefig(BASE_DIR + '\\static\\img\\wc.png')        
    words = sorted(text_dic2.items(), key= lambda x: x[1], reverse=True)
    # print(text_dic)
    return render(request, 'result.html', {'words': words})