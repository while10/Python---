rmb_str_value = input("请输入人民币金额：")
rate = 6.77
rmb_value = eval(rmb_str_value)
dollar = rmb_value / rate
print("美元：", dollar,rmb_str_value)
