"""
版本：4.0
时间：2018.10.8
功能：程序3.0增加的功能为程序一直运行，直到用户选择退出
4.0增加功能：将汇率封装到函数中
"""

def value_rate_exchange(str, rate):
    if str[-3:] == 'CNY':
        str_value = str[:-3]
        value = eval(str_value)
        exchange_rate = 1 / rate
        output_value = output(value, exchange_rate)
        print("美元：", output_value)
    elif str[-3:] == 'USD':
        str_value = str[:-3]
        value = eval(str_value)
        exchange_rate = rate
        output_value = output(value, exchange_rate)
        print("人民币：", output_value)
    else:
        exchange_rate = -1
    return exchange_rate

def output(value, rate):
    output_value = value * rate
    return output_value


RATE = 6.77
currency_str_value = input("请输带单位的货币金额：")

exchange_rate = value_rate_exchange(currency_str_value, RATE)
if exchange_rate == -1:
    print("该程序目前版本不支持该种货币")















# rmb_value = eval(rmb_str_value)
# dollar = rmb_value / rate
# print("美元：", dollar,rmb_str_value)
