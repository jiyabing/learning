#此实例示意条件表达式if_else的用法
#商场促销，满100 减20
money = int(input('输入商品金额：'))
pay = (money - 20) if money >=100 else money
print(pay)
