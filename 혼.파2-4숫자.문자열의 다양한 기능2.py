
#float
output_a="{:f}".format(52.273)                                #52.273000
output_b="{:15f}".format(52.273) #15칸 만들기                  #      52.273000
output_c="{:+15f}".format(52.273)#15칸 +부호 추가              #     +52.273000
output_d="{:+015f}".format(52.273)#15칸에 부호 추가/0으로 채우기#+0000052.273000
print(output_a)
print(output_b)
print(output_c)
print(output_d)
#소수점 아래 자릿수 지정하기
output_a="{:15.3f}".format(52.273)#-------52.273
output_b="{:15.2f}".format(52.273)#--------52.27
output_c="{:15.1f}".format(52.273)#---------52.2
print(output_a)
print(output_b)
print(output_c)
#의미 없는 소수점 제거하기
output_a=52.0
output_b="{:g}".format(output_a)
print(output_a) #52.0
print(output_b) #52