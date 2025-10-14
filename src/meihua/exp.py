'''
@File    :   exp.py
@Time    :   2025/10/11 17:20:57
@Author  :   glx 
@Version :   1.0
@Contact :   18095542g@connect.polyu.hk
@Desc    :   None
'''

# here put the import lib

from datetime import datetime

# 梅花易数起卦法，以时间为基础
# 公历时间: 2025年7月31日 16:51
time = datetime(2025, 7, 31, 16, 51)

# 转化为阴历的干支
import sxtwl

lunar = sxtwl.Lunar()
day = lunar.getDayBySolar(time.year, time.month, time.day)

# 获取年、月、日、时的天干地支
gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

year_gan = gan[day.Lyear2.tg]
year_zhi = zhi[day.Lyear2.dz]

month_gan = gan[day.Lmonth2.tg]
month_zhi = zhi[day.Lmonth2.dz]

day_gan = gan[day.Lday2.tg]
day_zhi = zhi[day.Lday2.dz]

# 时辰计算
hour_zhi = zhi[(time.hour + 1) // 2 % 12]

# 根据梅花易数方法起卦（年月日时相加取卦）
# 以年月日之和取上卦，以年月日时之和取下卦，取动爻为总和 % 6

# 天干地支对应数值
gan_num = {"甲":1, "乙":2, "丙":3, "丁":4, "戊":5, "己":6, "庚":7, "辛":8, "壬":9, "癸":10}
zhi_num = {"子":1, "丑":2, "寅":3, "卯":4, "辰":5, "巳":6, "午":7, "未":8, "申":9, "酉":10, "戌":11, "亥":12}

upper_sum = (gan_num[year_gan] + zhi_num[year_zhi] +
             gan_num[month_gan] + zhi_num[month_zhi] +
             gan_num[day_gan] + zhi_num[day_zhi]) % 8
lower_sum = (upper_sum + zhi_num[hour_zhi]) % 8
changing_line = (upper_sum + lower_sum + zhi_num[hour_zhi]) % 6
changing_line = 6 if changing_line == 0 else changing_line

# 卦象数组
gua = ["坤", "艮", "坎", "巽", "震", "离", "兑", "乾"]
upper_gua = gua[upper_sum]
lower_gua = gua[lower_sum]

upper_gua, lower_gua, changing_line
