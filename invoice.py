from datetime import date
from datetime import datetime
now = datetime.now()
import random
number = random.randint(1111,9999)

def content():
    add = input('Enter adress')
    print("")

    print('LULU HYPER MARKET LLC ')
    print('Branch:Trivandrum')
    print('TEL- 048567')
    print('-' * 145)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t INVOICE")
    print('-' * 145)
    print('Name:', name)
    print('Adress:', add)
    print('Date', date.today())
    print('Time:', now.strftime("%H:%M:%S"))
    print('Bill No:', number)
    print('-' * 145)
    print('S.No \tDescription \t\t Price \t\tQty \t\t Disc \t\t Net \t\t Tax Rate \t\t Total')
    print('-' * 145)
def concl():
    print('-' * 145)
    print('')
    print('')
    print('')
    print('\t\t\t\t\t\t\t\t\t\t\t\t\tTHANKYOU VISIT AGAIN')
    print('')
    print('')
    print('For more details visit www.luluhypermarket.com')
def con2():
    print('-' * 145)
    print('Grand Total:\t\t₹', tot1+tot2)
def con3():
    print('-' * 145)
    print('Grand Total:\t\t₹', tot1+tot2+tot3)
def con4():
    print('-' * 145)
    print('Grand Total:\t\t₹', tot1+tot2+tot3+tot4)

print('')
print('\t\t\t\t\t\t\t\t\t\t\t WELCOME TO LULU HYPERMARKET')
print('')
print('s.no \tProduct \t\t\t\t\t\t\t\t\t\t Price')
print('1 \t\tAPPLE iPhone 14 Pro (Deep Purple, 128 GB) \t\t ₹1,20,999')
print('2 \t\tAPPLE iPad Pro (4th Gen) 128 GB ROM       \t\t ₹77,990')
print('3 \t\tAPPLE Watch Ultra (Orange Alpine Strap)   \t\t ₹80,999')
print('4 \t\tAPPLE 2022 MacBook AIR M2  (Midnight)     \t\t ₹1,12,999')
print('')
name=input('Enter your name')
n=int(input('Enter No. of product you wish to buy'))
if n==1:
    p1=int(input('Enter No. of first product'))
    q=int(input('Quantity:'))
    if p1==1:
        dis=q*5000
        net=q*120999-q*5000
        tot=q*129499
        tax=q*7500
        content()
        print('1 \t\tiPhone 14 Pro \t\t₹1,25,999\t',q,'\t\t\t',dis,'\t\t',net,'\t',tax,'\t\t\t',tot)
        print('')
        print('-' * 145)
        print('Grand Total:\t\t₹',tot)
        concl()
    elif p1==2:
        dis = q * 2500
        net = q * 77990 - q * dis
        tax = q * 3000
        tot = net + tax
        content()
        print('1 \t\tiPad Pro     \t\t₹77,990   \t',q,'\t\t\t', dis,'\t\t', net,'\t',tax,'\t\t\t', tot)
        print('')
        print('-' * 145)
        print('Grand Total:\t\t₹', tot)
        concl()
    elif p1==3:
        dis = q * 2500
        net = q * 80999 - q * dis
        tax = q * 3200
        tot = net + tax
        content()
        print('1 \t\tWatch Ultra  \t\t₹80,999  \t',q,'\t\t\t', dis,'\t\t', net,'\t',tax,'\t\t\t',tot)
        print('')
        print('-' * 145)
        print('Grand Total:\t\t₹', tot)
    elif p1==4:
        dis = q * 2500
        net = q * 80999 - q * dis
        tax = q * 3200
        tot = net + tax
        content()
        print('1 \t\tMacBook AIR M2\t\t₹80,999  \t',q,'\t\t\t',dis,'\t\t', net,'\t', tax,'\t\t\t', tot)
        print('')
        print('-' * 145)
        print('Grand Total:\t\t₹', tot)

elif n==2:
    p1 = int(input('Enter No. of first product'))
    q1 = int(input('Quantity:'))
    p2 = int(input('Enter No. of second product'))
    q2 = int(input('Quantity:'))
    if p1 == 1:

        dis = q1 * 5000
        net = q1 * 120999 - q1 * 5000
        tot1 = q1 * 129499
        tax = q1 * 7500
        content()

        print('1 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 2:

        dis = q1 * 2500
        net = q1 * 77990 - q1 * dis
        tax = q1 * 3000
        tot1 = net + tax
        content()
        print('1 \t\tiPad Pro     \t\t₹77,990   \t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 3:

        dis = q1 * 2500
        net = q1* 80999 - q1 * dis
        tax = q1 * 3200
        tot1 = net + tax
        content()
        print('1 \t\tWatch Ultra  \t\t₹80,999  \t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 4:

        dis = q1 * 2500
        net = q1 * 80999 - q1 * dis
        tax = q1 * 3200
        tot1 = net + tax
        content()
        print('1 \t\tMacBook AIR M2\t\t₹80,999  \t', q1, '\t\t\t', dis, '\t\t', net, '\t\t', tax, '\t\t', tot1)
    if p2==1:
        dis = q2 * 5000
        net = q2 * 120999 - q2 * 5000
        tot2 = q2 * 129499
        tax = q2 * 7500
        print('2 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)



    elif p2==1:
        dis = q2 * 5000
        net = q2 * 120999 - q2 * 5000
        tot2 = q2 * 129499
        tax = q2 * 7500

        print('2 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)

    elif p2 == 2:
        dis = q2 * 2500
        net = q2 * 77990 - q2 * dis
        tax = q2 * 3000
        tot2 = net + tax

        print('2 \t\tiPad Pro     \t\t₹77,990   \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)

    elif p2 == 3:
        dis = q2 * 2500
        net = q2 * 80999 - q2 * dis
        tax = q2 * 3200
        tot2 = net + tax

        print('1 \t\tWatch Ultra  \t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)

    elif p2 == 4:
        dis = q2 * 2500
        net = q2 * 80999 - q2 * dis
        tax = q2 * 3200
        tot2 = net + tax

        print('2 \t\tMacBook AIR M2\t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)
    con2()
    concl()





elif n==3:
    p1 = int(input('Enter No. of first product'))
    q1 = int(input('Quantity:'))
    p2 = int(input('Enter No. of second product'))
    q2 = int(input('Quantity:'))
    p3 = int(input('Enter No. of third product'))
    q3 = int(input('Quantity:'))
    if p1 == 1:

        dis = q1 * 5000
        net = q1 * 120999 - q1 * 5000
        tot1 = q1 * 129499
        tax = q1 * 7500
        content()

        print('1 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 2:

        dis = q1 * 2500
        net = q1 * 77990 - q1 * dis
        tax = q1 * 3000
        tot1 = net + tax
        content()
        print('1 \t\tiPad Pro     \t\t₹77,990   \t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 3:

        dis = q1 * 2500
        net = q1* 80999 - q1 * dis
        tax = q1 * 3200
        tot1 = net + tax
        content()
        print('1 \t\tWatch Ultra  \t\t₹80,999  \t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 4:

        dis = q1 * 2500
        net = q1 * 80999 - q1 * dis
        tax = q1 * 3200
        tot1 = net + tax
        content()
        print('1 \t\tMacBook AIR M2\t\t₹80,999  \t', q1, '\t\t\t', dis, '\t\t', net, '\t\t', tax, '\t\t', tot1)
    if p2==1:
        dis = q2 * 5000
        net = q2 * 120999 - q2 * 5000
        tot2 = q2 * 129499
        tax = q2 * 7500
        print('2 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)



    elif p2==1:
        dis = q2 * 5000
        net = q2 * 120999 - q2 * 5000
        tot2 = q2 * 129499
        tax = q2 * 7500

        print('2 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)

    elif p2 == 2:
        dis = q2 * 2500
        net = q2 * 77990 - q2 * dis
        tax = q2 * 3000
        tot2 = net + tax

        print('2 \t\tiPad Pro     \t\t₹77,990   \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)

    elif p2 == 3:
        dis = q2 * 2500
        net = q2 * 80999 - q2 * dis
        tax = q2 * 3200
        tot2 = net + tax

        print('2 \t\tWatch Ultra  \t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)

    elif p2 == 4:
        dis = q2 * 2500
        net = q2 * 80999 - q2 * dis
        tax = q2 * 3200
        tot2 = net + tax

        print('1 \t\tMacBook AIR M2\t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)
    if p3==1:
        dis = q2 * 5000
        net = q2 * 120999 - q2 * 5000
        tot2 = q2 * 129499
        tax = q2 * 7500
        print('3 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)


    elif p3 == 2:
        dis = q3 * 2500
        net = q3 * 77990 - q3 * dis
        tax = q3 * 3000
        tot3 = net + tax

        print('3 \t\tiPad Pro     \t\t₹77,990   \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot3)

    elif p3 == 3:
        dis = q3 * 2500
        net = q3 * 80999 - q3 * dis
        tax = q3 * 3200
        tot3 = net + tax

        print('3 \t\tWatch Ultra  \t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot3)

    elif p3 == 4:
        dis = q3 * 2500
        net = q3 * 80999 - q3 * dis
        tax = q3 * 3200
        tot3 = net + tax

        print('3 \t\tMacBook AIR M2\t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot3)
    con3()
    concl()
elif n==4:
    p1 = int(input('Enter No. of first product'))
    q1 = int(input('Quantity:'))
    p2 = int(input('Enter No. of second product'))
    q2 = int(input('Quantity:'))
    p3 = int(input('Enter No. of third product'))
    q3 = int(input('Quantity:'))
    p4 = int(input('Enter No. of fourth  product'))
    q4 = int(input('Quantity:'))
    if p1 == 1:

        dis = q1 * 5000
        net = q1 * 120999 - q1 * 5000
        tot1 = q1 * 129499
        tax = q1 * 7500
        content()

        print('1 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 2:

        dis = q1 * 2500
        net = q1 * 77990 - q1 * dis
        tax = q1 * 3000
        tot1 = net + tax
        content()
        print('1 \t\tiPad Pro     \t\t₹77,990   \t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 3:

        dis = q1 * 2500
        net = q1* 80999 - q1 * dis
        tax = q1 * 3200
        tot1 = net + tax
        content()
        print('1 \t\tWatch Ultra  \t\t₹80,999  \t', q1, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot1)

    elif p1 == 4:

        dis = q1 * 2500
        net = q1 * 80999 - q1 * dis
        tax = q1 * 3200
        tot1 = net + tax
        content()
        print('1 \t\tMacBook AIR M2\t\t₹80,999  \t', q1, '\t\t\t', dis, '\t\t', net, '\t\t', tax, '\t\t', tot1)
    if p2==1:
        dis = q2 * 5000
        net = q2 * 120999 - q2 * 5000
        tot2 = q2 * 129499
        tax = q2 * 7500
        print('2 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)


    elif p2 == 2:
        dis = q2 * 2500
        net = q2 * 77990 - q2 * dis
        tax = q2 * 3000
        tot2 = net + tax

        print('2 \t\tiPad Pro     \t\t₹77,990   \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)

    elif p2 == 3:
        dis = q2 * 2500
        net = q2 * 80999 - q2 * dis
        tax = q2 * 3200
        tot2 = net + tax

        print('2 \t\tWatch Ultra  \t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)

    elif p2 == 4:
        dis = q2 * 2500
        net = q2 * 80999 - q2 * dis
        tax = q2 * 3200
        tot2 = net + tax

        print('2 \t\tMacBook AIR M2\t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot2)
    if p3==1:
        dis = q2 * 5000
        net = q2 * 120999 - q2 * 5000
        tot3 = q2 * 129499
        tax = q2 * 7500
        print('3 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot3)


    elif p3 == 2:
        dis = q3 * 2500
        net = q3 * 77990 - q3 * dis
        tax = q3 * 3000
        tot3 = net + tax

        print('3 \t\tiPad Pro     \t\t₹77,990   \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot3)

    elif p3 == 3:
        dis = q3 * 2500
        net = q3 * 80999 - q3 * dis
        tax = q3 * 3200
        tot3 = net + tax

        print('3 \t\tWatch Ultra  \t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot3)

    elif p3 == 4:
        dis = q3 * 2500
        net = q3 * 80999 - q3 * dis
        tax = q3 * 3200
        tot3 = net + tax

        print('3 \t\tMacBook AIR M2\t\t₹80,999  \t', q2, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot3)




    if p4==1:
        dis = q4 * 5000
        net = q4 * 120999 - q4 * 5000
        tot4 = q4 * 129499
        tax = q4 * 7500

        print('4 \t\tiPhone 14 Pro \t\t₹1,25,999\t', q4, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot4)

    elif p4 == 2:
        dis = q4 * 2500
        net = q4 * 77990 - q4 * dis
        tax = q4 * 3000
        tot4 = net + tax

        print('4 \t\tiPad Pro     \t\t₹77,990   \t', q4, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot4)

    elif p4 == 3:
        dis = q4 * 2500
        net = q4 * 80999 - q4 * dis
        tax = q4 * 3200
        tot4 = net + tax

        print('4 \t\tWatch Ultra  \t\t₹80,999  \t', q4, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot4)

    elif p4== 4:
        dis = q4 * 2500
        net = q4 * 80999 - q4 * dis
        tax = q4 * 3200
        tot4 = net + tax

        print('4 \t\tMacBook AIR M2\t\t₹80,999  \t', q4, '\t\t\t', dis, '\t\t', net, '\t', tax, '\t\t\t', tot4)
    con4()
    concl()
else:
    print('ERROR: YOU HAVE ENTERED AN INVALID OPTION')
