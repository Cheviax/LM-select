import pandas as pd
import math
import csv

# read data
df      =   pd.read_csv('limg_in.csv')
df.head()

out     =   open('limg_out.csv', 'w', encoding='UTF8', newline='')
writer  =   csv.writer(out)
switch  =   df['switch'][0]

c_lis   =   df['c_li']
z_lis   =   df['z_li']
c_mgs   =   df['c_mg']
z_mgs   =   df['z_mg']
z_cls   =   df['z_cl']
c_4s    =   df['c_4']
z_4s    =   df['z_4']
c_5s    =   df['c_5']
z_5s    =   df['z_5']
c_6s    =   df['c_6']
z_6s    =   df['z_6']
z_alls  =   (c_lis * z_lis) + (c_mgs*z_mgs) + (c_4s * z_4s) + (c_5s * z_5s) + (c_6s * z_6s)
c_cls   =   (z_alls * -1) / z_cls

d_pores =   df['d_pore']
v_pores =   df['v_pore']

swi     =   df[switch]

d_li    =   2.44
d_mg    =   2.66

row     =   []
row.append(switch)
row.append('ss')
row.append('mg2li')
row.append('ion_str')

writer.writerow(row)
for i in range(len(c_cls)):
    c_li    =   c_lis[i] / 1000
    z_li    =   z_lis[i]
    c_mg    =   c_mgs[i] / 1000
    z_mg    =   z_mgs[i]
    c_cl    =   c_cls[i] / 1000
    z_cl    =   z_cls[i]
    c_4     =   c_4s[i] / 1000
    z_4     =   z_4s[i]
    c_5     =   c_5s[i] / 1000
    z_5     =   z_5s[i]
    c_6     =   c_6s[i] / 1000
    z_6     =   z_6s[i]

    li2mg   =   (c_mg * 24.31) / (c_li * 6.941)

    d_pore  =   d_pores[i]
    v_pore  =   v_pores[i]

    bb      =   v_pore / 25
    ii      =   (c_li * z_li ** 2 / 2) + (c_mg * z_mg ** 2 / 2) + (c_cl * z_cl ** 2 / 2) \
                + (c_4 * z_4 ** 2 / 2) + (c_5 * z_5 ** 2 / 2) + (c_6 * z_6 ** 2 / 2)
    alp     =   -0.3565 * math.log10(ii) - 0.5576
    bet     =   0.505 + 0.5686 * alp
    lgaa    =   alp * math.log10(d_pore/10) + bet
    aa      =   10 ** lgaa
    s0      =   (d_pore - d_li) / (d_pore - d_mg)
    ss      =   s0 * aa ** bb

    line    = []
    line.append(swi[i])
    line.append(ss)
    line.append(li2mg)
    line.append(ii*1000)
    writer.writerow(line)

out.close()