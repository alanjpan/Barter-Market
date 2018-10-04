# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:04:51 2018

@author: Alan Jerry Pan, CPA, CSC
@affiliation: Shanghai Jiaotong University

Program used for experimental study of (i) markets, (ii) consumer behavior, and (iii) information asymmetry in decision making (business) and risk-taking.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Barter Market [Computer software]. Github repository <https://github.com/alanjpan/Barter-Market>

Futher expansions may include a dynamic market, multiple markets, more products & descriptions, service offerings, competitor AI merchants, and interactive clients.

Note this software's license is GNU GPLv3.
"""


import random
import time

secure_random = random.SystemRandom()

time_start = 0
gold = 100

nondurablegoods = ['cherries', 'strawberries', 'oranges', 'apples', 'melons']
durablegoods = ['gen-seats', 'power desks', 'beds of pwr']

nondurableprices = [10, 30, 50, 70, 100]
durableprices = [10, 50, 100]

nondurabledescription = ['dark red tangy pair', 'bright red subtly sweet texture', 'refreshing tangy citrus', 'sweet crisp sharp flavor', 'sweet plump mellow splash']
durabledescription = ['you sit on this', 'you can get work done', 'a deep sleep']

nondurablesupply = ['med', 'med', 'med', 'med', 'med']
durablesupply = ['med', 'med', 'med']
supplierpatience = [1, 2, 3]

demandlevel = ['high', 'med', 'low']
high = [1.1, 1.25, 1.3, 1.5]
med = [.75, .85, .9, 1.1, 1.15, 1.25]
low = [.5, .6, .75, .8, .85, .9, 1.1]
custhigh = [3, 4, 5]
custmed = [2, 3, 4]
custlow = [1, 2, 3]


barterratio = [.1, .15, .2, .25, .3, .35]

barternondurable = ['You want fruit? I give you fruit.', 'Ahoy there, stranger!', 'What ye want?', 'Now where did I put my fruit?']
barterdurable = ['The finest furniture and selections.', 'Only the best.', 'Need something?', 'I just got this shipment in.']

playernondurablequantity = [0, 0, 0, 0, 0]
playernondurableprice = [0, 0, 0, 0, 0]
playerdurablequantity = [0, 0, 0]
playerdurableprice = [0, 0, 0]


def displaythegoods():
    print('o-|ITEM\t\tPRICE\tSUPPLY')
    for i in range(len(nondurablegoods)):
        print('o-|' + nondurablegoods[i] + '\t' + str(nondurableprices[i]) + '\t' + nondurablesupply[i] + '\t' + nondurabledescription[i])
    for i in range(len(durablegoods)):
        print('o-|' + durablegoods[i] + '\t' + str(durableprices[i]) + '\t' + durablesupply[i] + '\t' + durabledescription[i])

def displayyourinventory():
    print('oo-ITEM\tQUANTITY\tPRICE')
    for i in range(len(playernondurablequantity)):
        if playernondurablequantity[i] != 0:
            print('oo-' + nondurablegoods[i] + '\t' + str(playernondurablequantity[i]) + '\t' + str(playernondurableprice[i]))
    for i in range(len(playerdurablequantity)):
        if playerdurablequantity[i] != 0:
            print('oo-' + durablegoods[i] + '\t' + str(playerdurablequantity[i]) + '\t' + str(playerdurableprice[i]))

def checkpurchase(pur):
    key = pur[0]
    for i in range(len(nondurablegoods)):
        if nondurablegoods[i].startswith(key):
            return 'nondurable'
    for i in range(len(durablegoods)):
        if durablegoods[i].startswith(key):
            return 'durable'
    return 'nan'

def checkquantity(item):
    key = item[0]
    
    for i in range(len(nondurablegoods)):
        if nondurablegoods[i].startswith(key):
            if playernondurablequantity[i] != 0:
                return True
            else:
                return False
    for i in range(len(durablegoods)):
        if durablegoods[i].startswith(key):
            if playerdurablequantity[i] != 0:
                return True
            else:
                return False
    return False

def querynondurable(key):
    for i in range(len(nondurablegoods)):
        if nondurablegoods[i].startswith(key):
            return i
def querydurable(key):
    for i in range(len(durablegoods)):
        if durablegoods[i].startswith(key):
            return i
    
    
def PURCHASEYOURNONDURABLE(pur):
    global gold
    global playernondurablequantity
    global playernondurableprice
    
    key = pur[0]
    i = querynondurable(key)
    
    buyprice = int(nondurableprices[i] * secure_random.choice(eval(nondurablesupply[i])))
    patience = secure_random.choice(supplierpatience)

    k = 0
    for j in range(patience):
        if k == 0:
            print(secure_random.choice(barternondurable))
            print(nondurablegoods[i] + ' for ' + str(buyprice) + '. (ye/no)')
        elif k > 0:
            buyprice -= int(buyprice * secure_random.choice(barterratio))
            print('Okay, okay. ' + nondurablegoods[i] + ' for ' + str(buyprice) + '. (ye/no)')
        
        response = input().lower()
        
        if response.startswith('y'):
            maxquant = int(gold / buyprice)
            print('How many? (0-' + str(maxquant) + ')')    
            quant = int(input())
            if 0 < quant <= maxquant:
                print('We have an accord.')
                purchase = buyprice * quant
                print('You bought ' + str(quant) + ' ' + nondurablegoods[i] + ' for ' + str(purchase) + ' gold!!')
                playernondurablequantity[i] = quant
                playernondurableprice[i] = buyprice
                gold -= purchase
                return
            else:
                print('Buzz off. You don\'t have enough gold!')                
                return
        elif response.startswith('n'):
            k += 1
        else:
            print('Serious clients only.')
            return
    print('No deal.')

def PURCHASEYOURDURABLE(pur):
    global gold
    global playerdurablequantity
    global playerdurableprice
    
    key = pur[0]
    i = querydurable(key)
    
    buyprice = int(durableprices[i] * secure_random.choice(eval(durablesupply[i])))
    patience = secure_random.choice(supplierpatience)

    k = 0
    for j in range(patience):
        if k == 0:
            print(secure_random.choice(barterdurable))
            print(durablegoods[i] + ' for ' + str(buyprice) + '. (ye/no)')
        elif k > 0:
            buyprice -= int(buyprice * secure_random.choice(barterratio))
            print('Fine. ' + durablegoods[i] + ' for ' + str(buyprice) + '. (ye/no)')
        
        response = input().lower()
        
        if response.startswith('y'):
            maxquant = int(gold / buyprice)
            print('How many? (0-' + str(maxquant) + ')')    
            quant = int(input())
            if 0 < quant <= maxquant:
                print('Let\'t get your purchase concluded.')
                purchase = buyprice * quant
                print('You bought ' + str(quant) + ' ' + durablegoods[i] + ' for ' + str(purchase) + ' gold!!')
                playerdurablequantity[i] = quant
                playerdurableprice[i] = buyprice
                gold -= purchase
                return
            else:
                print('You can\'t afford this! I don\'t have time to talk to you.')                
                return
        elif response.startswith('n'):
            k += 1
        else:
            print('Go check over there.')
            return
    print('Good luck to you.')

def nondurmarketsim(n, demand, i):   
    global gold
    global playernondurablequantity
    
    for j in range(n):
        saleprice = int(nondurableprices[i] * secure_random.choice(eval(demand)))
        print(str(playernondurablequantity[i]) + ' ' + nondurablegoods[i] + ' for ' + str(saleprice) + ' each. (ye/no)')
        if input().lower().startswith('ye'):
            sale = saleprice * playernondurablequantity[i]
            print('Done. ' + str(sale) + ' gold gained!')
            gold += sale
            playernondurablequantity[i] = 0
            return
        else:
            print('Nevermind.')

def nondurmarkethigh(i):
    n = secure_random.choice(custhigh)
    nondurmarketsim(n, 'high', i)
def nondurmarketmed(i):
    n = secure_random.choice(custmed)
    nondurmarketsim(n, 'med', i)
def nondurmarketlow(i):
    n = secure_random.choice(custlow)
    nondurmarketsim(n, 'low', i)

def SELLYOURNONDURABLE(item):
    key = item[0]
    i = querynondurable(key)
    demand = secure_random.choice(demandlevel)
    
    print('Demand for this item is ' + demand.upper())
    
    if demand == 'high':
        nondurmarkethigh(i)
    elif demand == 'med':
        nondurmarketmed(i)
    elif demand == 'low':
        nondurmarketlow(i)
        
def durmarketsim(n, demand, i):   
    global gold
    global playerdurablequantity
    
    for j in range(n):
        saleprice = int(durableprices[i] * secure_random.choice(eval(demand)))
        print(str(playerdurablequantity[i]) + ' ' + durablegoods[i] + ' for ' + str(saleprice) + ' each. (ye/no)')
        if input().lower().startswith('ye'):
            sale = saleprice * playerdurablequantity[i]
            print('Done. ' + str(sale) + ' gold gained!')
            gold += sale
            playerdurablequantity[i] = 0
            return
        else:
            print('Nevermind.')    
    
def durmarkethigh(i):
    n = secure_random.choice(custhigh)
    durmarketsim(n, 'high', i)
def durmarketmed(i):
    n = secure_random.choice(custmed)
    durmarketsim(n, 'med', i)
def durmarketlow(i):
    n = secure_random.choice(custlow)
    durmarketsim(n, 'low', i)
    
def SELLYOURDURABLE(item):
    key = item[0]
    i = querydurable(key) 
    demand = secure_random.choice(demandlevel)
    
    print('Demand for this item is ' + demand.upper())
    
    if demand == 'high':
        durmarkethigh(i)
    elif demand == 'med':
        durmarketmed(i)
    elif demand == 'low':
        durmarketlow(i)

def UPDATETHEMARKET(turn):
    for i in range(len(nondurablegoods)):
        nondurablesupply[i] = secure_random.choice(demandlevel)
        nondurableprices[i] = int((1+(turn/100)) * nondurableprices[i] * secure_random.choice(eval(nondurablesupply[i])))
    for i in range(len(durablegoods)):
        durablesupply[i] = secure_random.choice(demandlevel)
        durableprices[i] = int((1+(turn/100)) * nondurableprices[i] * secure_random.choice(eval(nondurablesupply[i])))

    
def ENTERTHEMARKET():
    global gold
    global playernondurablequantity
    global playernondurableprice
    
    turn = 1
    
    while (gold >= 0):
        print('\n|---||---|TURN ' + str(turn) + '|---||---|\n')
        print('GOLD COINS: ' + str(gold))
        displaythegoods()
        print('What do you want to buy? (c/s/o/a/m/g/p/b)')
        purchase = input().lower()
        barter = checkpurchase(purchase)
        
        if barter == 'nondurable':
            PURCHASEYOURNONDURABLE(purchase)
        elif barter == 'durable':
            PURCHASEYOURDURABLE(purchase)
        else:
            print('Sorry, we don\'t sell that in our market.')

        print('\n\n~*~*~~*~~~IT IS NIGHT TIME~~~*~~*~*~\n')
        tax = turn * 10
        displayyourinventory()
        
        print('\n\nYou must sell your non-durable goods before the day is over!')
        print('What item do you sell? You must sell!')
        sale = input().lower()
        
        if checkquantity(sale) == False:
            print('A guard taxes you ' + str(tax) + ' for falsifying your possessions. (everyone in the market can see what you have!)')
            gold -= tax
        
        if sale.startswith('c') or sale.startswith('s') or sale.startswith('o') or sale.startswith('a') or sale.startswith('m'):
            SELLYOURNONDURABLE(sale[0])
        elif sale.startswith('g') or sale.startswith('p') or sale.startswith('b'):
            SELLYOURDURABLE(sale[0])

        #clear nondurable inventory
        for i in range(len(nondurablegoods)):
            playernondurablequantity[i] = 0
            playernondurableprice[i] = 0


        print('\n\nThe day is over. All merchants and clients go home.\n')
        print('Do you retire from the market? (ye/no)')
        response = input().lower()
        if response.startswith('ye'):
            gameover()
        elif response.startswith('no'):
            turn += 1
        else:
            print('A guard taxes you ' + str(tax) + ' gold for your gibberish.')
            gold -= tax
            turn += 1
        UPDATETHEMARKET(turn)
    if gold <= 0:
        gameover()

def gameover():
    global gold
    global time_start
    
    print('\n\n||--||_____o1_____\n')
    print('You leave with ' + str(gold) + ' gold pieces this session.')
    print('%s seconds were spent in this market.' % int((time.time() - time_start)))
    if gold <= 100:
        print('If you are a merchant, you should be ashamed of yourself.')
    else:
        print('Leave with your head held high, merchant.')
    exit
        
def main():
    global time_start
    
    print('\n\n__________||BARTER MARKET||__________')
    print('You, a merchant, seek to obtain great riches. You only have 100g. Spend it wisely. Buy low and sell high. Do you enter the market? (ye/no)\n')
    if input().lower().startswith('ye'):
        time_start = time.time()
        ENTERTHEMARKET()
    else:
        gameover()
        
main()
