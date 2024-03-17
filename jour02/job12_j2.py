Rectangel_width = int(input('Please enter width: '))
Rectangel_hight = int(input('Please enter hight: '))



for h in range(Rectangel_hight):
    if h == 0 or h == Rectangel_hight:
        print ( '-' * Rectangel_width)
    else:
        print ("|" + " " * (Rectangel_width-2 )+ "|" ) 