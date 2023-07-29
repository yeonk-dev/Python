string_a="{}".format(10)

print(string_a)
print(type(string_a))
#format 함수로 숫자를 문자열로 변환
format_a="{}만 원".format(5000)
format_b="{}{}{}".format(3000, 4000, 5000)
print(format_a)
print(format_b)

#정수출력
output_a="{:5d}".format(52)  #기본 
print("#기본")
print(output_a) #   52
#특정칸에 출력
output_b="{:5d}".format(52) #5칸
output_c="{:10d}".format(52) #10칸
#빈칸을 0으로 채우기
output_d="{:05d}".format(52) #양수 #00052
output_e="{:05d}".format(-52) #음수 #-0052
#기호와 함께 출력
output_f="{:+d}".format(52) #양수#+52
output_g="{:+d}".format(-52)#음수 #-52
output_h="{: d}".format(52)#양수:기호공백 #52
output_i="{: d}".format(-52)#음수:기호공백 #-52
#조합하기
output_h="{:+5d}".format(52) #기호를 뒤로 밀기 #  +52
output_i="{:+5d}".format(-52) #  -52
output_j="{:=+5d}".format(52) #기호를 앞으로 밀기 #+  52
output_k="{:=+5d}".format(-52)#-  52
output_l="{:+05d}".format(52) #0으로 채우기 #+0052
output_m="{:+05d}".format(-52)#-0052