#zodiac_name = (u'魔羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',
#               u'巨蟹座',u'狮子座',u'处女座',u'天枰座',u'天蝎座',u'射手座')
##u是为了不出现乱码
#zodiac_days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),                 #元组
#               (7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
#
#(month,day) = (2,15)
#zodiac_day = filter(lambda x:x<=(month,day),zodiac_days)
#
#zodiac_len = len(list(zodiac_day)) % 12
#print(zodiac_name[zodiac_len])#

a_list = ['abc','xyz']
a_list.append('X')   #给列表增加一个元素
print(a_list)
a_list.remove('xyz') #移除一个元素
print(a_list)
