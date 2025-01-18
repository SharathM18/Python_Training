# coupon = ['CDEC01','ONEJAN02','2234150']

def discount_coupon():
    print('Welcome to online shopping.')
    print('your cart is not empty.')
    print('You have to pay Rs. 1500/-')
    have_coupon = input('Do you have coupon? type y or n: ')
    if have_coupon == 'y':
        ip_coupon = input('Please enter the coupon code: ')

        if ip_coupon.upper() == 'CDEC01'.upper():
            print('successfully applied the coupon code. Please pay 1000/-')

        elif ip_coupon.upper() == 'ONEJAN02'.upper():
            print('successfully applied the coupon code. Please pay 750/-')

        elif ip_coupon == '2234150':
            print('successfully applied the coupon code.')
            print('Congratulations! You got 1000 loyalty points for shopping with us. Please pay 1500/-')
        else:
            print('invalid coupon code')
    else:
        print('Please pay Rs. 1500/-')

discount_coupon()