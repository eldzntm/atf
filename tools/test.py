Country_CODE = str(input("국가코드를 입력하세요.")).upper().title() #앞에 upper가 작동한 후 title이 작동해 title을 따라감
print(Country_CODE)

#첫 예외처리문 간직
#Country_Color_CODE_1 = Country_Color_CODE_2 = Country_Color_CODE_3 = None
#try:
#    Country_Color_CODE_1, Country_Color_CODE_2, Country_Color_CODE_3 = map(str, input("국가색깔코드를 입력하세요. (기본값:0 0 0)").split(' '))
#except:
#    if Country_Color_CODE_1 == None:
#        Country_Color_CODE_1 = 0
#    if Country_Color_CODE_2 == None:
#        Country_Color_CODE_2 = 0
#    if Country_Color_CODE_3 == None:
#        Country_Color_CODE_3 = 0