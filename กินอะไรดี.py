subsidy = 2000
total = 0
add_on_item = 0
saving = 0
rent = int(input())
water = int(input())
elec = int(input())
net = int(input())
phone = int(input())
print('rent:', str(rent), '฿')
print('water:', str(water), '฿')
print('elec:', str(elec), '฿')
print('net:', str(net), '฿')
print('phone:', str(phone), '฿')
print("total:",str(rent),'+',str(water),'+',str(elec),'+',str(net),'+',str(phone))
total = rent+water+elec+net+phone
print("    =", total, '฿')
remaining_cash = subsidy-total
if remaining_cash >= 10:
    print('SELECT: chewy noodles')
    print('    = 10 ฿')
    add_on_item = 10
elif remaining_cash < 10 and remaining_cash >= 6:
    print('SELECT: instant noodles')
    print('    = 6 ฿')
    add_on_item = 6
elif remaining_cash < 6 and remaining_cash >= 2:
    print('SELECT: soup')
    print('    = 2 ฿')
    add_on_item = 2
elif remaining_cash < 2:
    print('SELECT: drinking water')
    print('    = 0 ฿')
    add_on_item = 0
saving = 2000-total-add_on_item
print('SAVING: 2000 -',str(total),'-',str(add_on_item))
print('    =',str(saving),'฿')
