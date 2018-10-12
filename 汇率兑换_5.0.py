"""
版本：5.0
时间：2018.10.8
功能：程序3.0增加的功能为程序一直运行，直到用户选择退出
4.0增加功能：将汇率封装到函数中
5.0增加功能：函数结构化/实现简单函数的定义
"""

def value_rate_exchange(str, rate):
    if str[-3:] == 'CNY':
        str_value = str[:-3]
        value = eval(str_value)
        exchange_rate = 1 / rate
        #lambda 函数的使用
        function_name = lambda x : x *exchange_rate
        output_value = function_name(value)

        # output_value = output(value, exchange_rate)
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
    """
    汇率兑换函数
    :param value:输入的原始值
    :param rate: 汇率
    :return: 返回汇率兑换结果
    """
    output_value = value * rate
    return output_value

def main():
    RATE = 6.77
    currency_str_value = input("请输带单位的货币金额：")

    exchange_rate = value_rate_exchange(currency_str_value, RATE)
    if exchange_rate == -1:
        print("该程序目前版本不支持该种货币")

if __name__ == '__main__':
    main()


