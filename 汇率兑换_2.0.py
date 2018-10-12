currency_str_value = input("请输带单位的货币金额：")
RATE = 6.77
if currency_str_value[-3:] == 'CNY':
    rmb_str_value = currency_str_value[:-3]
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value / RATE
    print("美元：", usd_value)
elif currency_str_value[-3:] == 'USD':
    usd_str_value = currency_str_value[:-3]
    usd_value = eval(usd_str_value)
    rmb_value = usd_value * RATE
    print("人民币：", rmb_value)
else:
    except_else = '改程序目前版本不支持该种货币'
    print(except_else)







# rmb_value = eval(rmb_str_value)
# dollar = rmb_value / rate
# print("美元：", dollar,rmb_str_value)
