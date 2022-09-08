from cmath import sqrt

###Total 
Tx1=7.526
Ty1=-41.49

#x2=-28.72 
#y2= 41.14

Tx2= -28.11
Ty2= 40.083

Td=sqrt((Tx2-Tx1)**2+(Ty2-Ty1)**2)
Tt=Td/0.5
print(f'Total:{Td}, {Tt+20}')


#('Mario_Cell')
px1=(6.97)
py1=(-40.47)


#'Cafe_Palantino')
sx1=(2.58)
sy1=(-31.726)

tp=(sqrt((sx1-px1)**2+(sy1-py1)**2))/0.5
print(f'first street: {tp}')
#'LiliPink')
tx1=( -5.407)
ty1=( -12.86)

ts=(sqrt((tx1-sx1)**2+(ty1-sy1)**2))/0.5
print(f'second street: {ts}')

#'Confam_drog')
cx1 =(-13.167)
cy1= (5.625)

tt=(sqrt((cx1-tx1)**2+(cy1-ty1)**2))/0.5
print(f'third street; {tt}')


#('Exito')
qx1=( -21.52)
qy1=( 24.45)

tc=(sqrt((qx1-cx1)**2+(qy1-cy1)**2))/0.5
print(f'forth street; {tc}')

#'Sweet')
sex1=(-28.72)
sey1=(41.14)

tq=(sqrt((sex1-qx1)**2+(sey1-qy1)**2))/0.5
print(f'fifth street; {tq}')
