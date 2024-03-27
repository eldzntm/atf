#region 파일경로
common_countries = "./common/countries"
common_countries_colors_txt = "./common/countries/colors.txt"
common_country_tags_txt = "./common/country_tags/CW_countries.txt"#모드마다 직접바꿔줘야함
history_countries = "./history/countries"
gfx_flags = "./gfx/flags"
gfx_flags_example = "tools/example_flags"
localisation_countries = "localisation/CW_countries_l_english.yml"#모드마다 직접바꿔줘야함
#endregion

#region 입력
Country_CODE = str(input("국가 코드를 입력하세요.")).upper()
Country_NAME = str(input("국가 영어이름을 입력하세요.")).title()
Country_Korean_NAME = str(input("국가 한글이름을 입력하세요."))
Country_Color_CODE_list = list(map(str, input("국가 색깔코드를 입력하세요.(기본값: 0 0 0 )").split(' ')))
#endregion

#region 국가 색코드 검열, 준비
def Country_Color_CODE_Sub(a):
    try:
        return Country_Color_CODE_list[a-1]
    except:
        return 0

Country_Color_CODE_1 = Country_Color_CODE_Sub(1)
Country_Color_CODE_2 = Country_Color_CODE_Sub(2)
Country_Color_CODE_3 = Country_Color_CODE_Sub(3)
#endregion

#region gfx 국기
l = ["communism", "democratic", "fascism", "neutrality"]

def Flag_Copy(pre_root, post_root):
    with open(pre_root,'rb') as f:
        readFile = f.readline()
    for i in l:
        with open(post_root+"/"+Country_CODE+"_"+i+".tga", 'wb') as f:
            f.write(readFile)

Flag_Copy(gfx_flags_example+"/example.tga", gfx_flags)
Flag_Copy(gfx_flags_example+"/medium/example.tga", gfx_flags+"/medium")
Flag_Copy(gfx_flags_example+"/small/example.tga", gfx_flags+"/small")
#endregion

#region common/countries에 국가 텍스트 파일
with open(common_countries+"/"+Country_NAME+".txt",'w') as f:
    f.write("""
graphical_culture = western_european_gfx
graphical_culture_2d = western_european_2d

color = { %s %s %s }
    """ % (Country_Color_CODE_1, Country_Color_CODE_2, Country_Color_CODE_3))
#endregion

#region colors에 색코드 추가
with open(common_countries_colors_txt,'a') as f:
    f.write("\n")
    f.write(("""
%s = {
    color = rgb { %s %s %s }
    color_ui = rgb { %s %s %s }
}
""" % (Country_CODE, Country_Color_CODE_1, Country_Color_CODE_2, Country_Color_CODE_3, Country_Color_CODE_1, Country_Color_CODE_2, Country_Color_CODE_3)).strip('\n'))
#endregion

#region 국가태그
with open(common_country_tags_txt,'a') as f:
    f.write("\n")
    f.write(("""
%s = "countries/%s.txt"
    """ % (Country_CODE, Country_NAME)).strip('\n'))
#endregion

#region 국가 히스토리
with open(history_countries+"/"+Country_CODE+" - "+Country_NAME+".txt",'w') as f:
    f.write("""
capital = 1

set_research_slots = 3
set_stability = 0.8
set_war_support = 0.3
set_convoys = 80

set_technology = {
	infantry_weapons = 1
	infantry_weapons1 = 1
	tech_support = 1
	tech_recon = 1
	tech_engineers = 1
	tech_trucks = 1
	motorised_infantry = 1
	trench_warfare = 1
	fuel_silos = 1
	fuel_refining = 1
	basic_train = 1
}

set_politics = {
	ruling_party = neutrality
	last_election = "1933.3.5"
	election_frequency = 48
	elections_allowed = no
}

set_popularities = {
	neutrality = 100
}
    """)

with open(localisation_countries,'a', encoding="UTF-8") as f:
    f.write("\n")
    f.write("""
 %s_fascism:0 "%s"
 %s_fascism_DEF:0 "%s"
 %s_democratic:0 "%s"
 %s_democratic_DEF:0 "%s"
 %s_neutrality:1 "%s"
 %s_neutrality_DEF:1 "%s"
 %s_communism:0 "%s"
 %s_communism_DEF:0 "%s"
 %s_fascism_ADJ:0 "%s"
 %s_democratic_ADJ:0 "%s"
 %s_neutrality_ADJ:0 "%s"
 %s_communism_ADJ:0 "%s"
 %s:0 "%s"
 %s_DEF:0 "%s"
 %s_ADJ:0 "%s"
    """ % (Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME,
Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, 
Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, 
Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, Country_CODE, Country_Korean_NAME, ))#15
#endregion