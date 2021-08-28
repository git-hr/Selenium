import random
from value import *

def buy_l1():
    l1_gold = l1_value_gold + l1_value_diamond * diamond_to_gold
    return l1_gold

price_l1 = buy_l1()

def compose_l3():
    l3_gold = price_l1
    for a in range(0,l1_to_l3):
        l3_gold += price_l1
    l3_gold = l3_gold + l1_to_l3_gold + l1_to_l3_vit * vit_to_gold
    return l3_gold

def compose_l4():
    l4_gold_price_l1 = 0
    for b in range(0,l3_to_l4):
        l4_gold_price_l1 += price_l1
    compose_l4_price = l4_gold_price_l1 + l3_to_l4_gold
    l4_gold = compose_l3() + compose_l4_price + l3_to_l4_vit * vit_to_gold
    rate = random.randint(0,100) * 0.01
    while rate > l3_to_l4_rate:
        l4_gold += compose_l4_price
        rate = random.randint(0,100) * 0.01
    else:
        return l4_gold

def compose_l6():
    l6_gold = compose_l4()
    for c in range(0,l4_to_l6):
        l6_gold += compose_l4()
    l6_gold = l6_gold + l4_to_l6_gold + l4_to_l6_vit * vit_to_gold
    return l6_gold