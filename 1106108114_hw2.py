from math import ceil

PRICE_WEEKDAYS_NOON_ADULTS = 468
PRICE_WEEKDAYS_NOON_CHILDREN = 220

PRICE_HOLIDAY_AND_NIGHT_ADULTS = 568
PRICE_HOLIDAY_AND_NIGHT_CHILDREN = 250
SERVICE_ADDITION = 0.1

DISCOUNT_FOLD = 0.95
def price_count(weekdays_noon_or_holiday_and_night, discount, adults, children):
    if(weekdays_noon_or_holiday_and_night==1):
        return ceil(price_weekdays_noon(discount, adults, children))
    elif(weekdays_noon_or_holiday_and_night==2):
        return ceil(price_weekdays_night_or_holiday(discount, adults, children))

def price_weekdays_noon(discount, adults, children):
    if(discount):
        return (discount_three_for_two(adults, children)[0] * PRICE_WEEKDAYS_NOON_ADULTS + discount_three_for_two(adults, children)[1] * PRICE_WEEKDAYS_NOON_CHILDREN) * discount_ten_people(adults, children)  * (1 + SERVICE_ADDITION)
    else:
        return PRICE_WEEKDAYS_NOON_ADULTS * adults + PRICE_WEEKDAYS_NOON_CHILDREN * children  * (1 + SERVICE_ADDITION)


def price_weekdays_night_or_holiday(discount, adults, children):
    if(discount):
        return (discount_three_for_two(adults, children)[0] * PRICE_HOLIDAY_AND_NIGHT_ADULTS + discount_three_for_two(adults, children)[1] * PRICE_HOLIDAY_AND_NIGHT_CHILDREN)  * discount_ten_people(adults, children) * (1 + SERVICE_ADDITION)
    else:
        return PRICE_HOLIDAY_AND_NIGHT_ADULTS * adults + PRICE_HOLIDAY_AND_NIGHT_CHILDREN * children  * (1 + SERVICE_ADDITION)

def discount_three_for_two(adults, children):
    discount_amt = (adults + children) // 3
    children -= discount_amt
    if( children < 0 ):
        adults += children
        return (adults, 0)
    else:
        return (adults, children)

def discount_ten_people(adults, children):
    if((adults + children)>10):
        return DISCOUNT_FOLD
    else :
        return 1

weekdays_noon_or_holiday_and_night = int(input("平日中午請選1, 假日或平日晚上請選2\n"))
discount_time = True if int(input("促銷期間請選1, 非促銷期間請選0\n")) == 1 else False
adults_num = int(input("請輸入成人數\n"))
children_num = int(input("請輸入小孩數\n"))

notice = '時間：{}\n'.format( '平日中午' if( weekdays_noon_or_holiday_and_night ==1) else '假日或平日晚上')
notice += '促銷期間：{}\n'.format(discount_time)
notice += '成人{}位，小孩{}位'.format(adults_num, children_num)

print(notice)
print('共{}元'.format(price_count(weekdays_noon_or_holiday_and_night, discount_time, adults_num, children_num)))