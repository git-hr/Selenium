import function

print('请输入合成次数')
compose_times = int(input())
if compose_times >= 100:
    compose_marks = compose_times // 20
else:
    compose_marks = compose_times
compose_gold = 0

for t in range(0,compose_times):
    compose_gold += function.compose_l6()
    if t % compose_marks == 0:
        print(str(t // compose_marks * 5) + '%')
print('100%')
compose_gold_average = compose_gold / compose_times

if compose_gold < function.market_price:
    print('合成石头划算，平均费用为' + str(compose_gold_average))
else:
    print('直接购买划算，平均费用为' + str(compose_gold_average))