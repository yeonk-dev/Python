1.
sentence="way a is there will a is there Where"
def reverse_sentence(sentence):
    # string 연산자를 이용하여 저 리스트의 단어를 끈어야함.
    right_stence=sentence.split(' ')
    print(right_stence)
    # ['way', 'a', 'is', 'there', 'will', 'a', 'is', 'there', 'where']
    j=len(right_stence) #10개 9번

    for i in range(j-1,-1,-1): #초기값>마지막값 for(초기값, 마지막값-1,감소값)
        #초기값<마지막값 for(초기값, 마지막값+1,증가값)
        print(right_stence[i],end=' ')
reverse_sentence(sentence)

2.
def reverse_sentence(sentence):
    # TODO
    sentence_list = sentence.split()
    return ' '.join(sentence_list[::-1])


3.
# def reverse_sentence(sentence):
#   return " ".join(sentence.split(" ")[::-1])

# print(reverse_sentence(sentence))

4.
sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
  return " ".join(sentence.split(" ")[::-1])

print(reverse_sentence(sentence))





