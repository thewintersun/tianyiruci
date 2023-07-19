'''
XA_1:=(2*CLOSE+HIGH+LOW)/3;
XA_2:=EMA(XA_1,3);
XA_3:=EMA(XA_2,3);
XA_4:=EMA(XA_3,3);
AEFG1:(XA_4-REF(XA_4,1))/REF(XA_4,1)*100;

AEFG2:MA(AEFG1,2),COLORYELLOW,LINETHICK3;
AEFG3:MA(AEFG1,1),COLORMAGENTA,LINETHICK3;
'''
import matplotlib.pyplot as plt
import pandas as pd
import talib
import numpy as np


def show(ema_days=3, calc_daily=True):
    # daily
    weekly = [0.00, 8.01, 10.22, 5.81, 11.31, 12.61, 11.26, 11.98, 11.80, 5.92, 4.30, 1.20, 4.66,
              15.96, 13.26, 19.26, 21.03, 25.12, 25.00, 28.66, 29.20, 29.50, 24.04, 21.81, 27.65,
              27.46, 31.09, 36.64, 39.02, 37.86, 39.84, 44.57, 42.97, 40.77, 44.29, 40.22, 38.01,
              36.48, 30.65, 33.27, 35.56, 37.27, 40.16, 40.99, 41.78, 42.77, 45.22, 41.10, 52.32,
              55.00, 55.91, 56.61]
    daily = [261.89, 261.39, 253.77, 247.84, 253.45, 261.94, 272.54, 272.88, 270.40, 272.37, 273.89,
             268.81, 267.45, 269.85, 272.58, 270.51,
            275.84, 281.01, 280.38, 285.92, 289.64, 296.48, 297.06, 296.50, 297.10, 298.43, 297.65,
            301.61, 303.41, 308.48, 310.29, 308.17, 298.52, 300.04, 301.64, 303.91, 304.94, 304.26,
            305.77, 305.68, 311.30, 316.10, 317.21, 319.50, 319.51, 310.17, 315.73, 320.74, 314.87,
            313.81, 309.15, 314.05, 309.04, 308.49, 305.73, 317.73, 320.68, 318.29, 318.70, 319.16,
            314.28, 308.77, 303.08, 306.89, 310.77, 302.13, 296.39, 300.49, 290.55, 288.74, 293.86,
            292.87, 296.04, 296.14, 293.59, 292.04, 286.47, 279.12, 276.74, 270.01, 280.54, 279.37,
            286.71, 293.59, 293.37, 293.89, 287.87, 291.09, 300.26, 298.33, 299.91, 296.50, 306.53,
            309.17, 306.72, 307.78, 308.51, 308.06, 309.91, 309.11, 302.78, 305.11, 302.75, 302.08,
            311.40, 319.36, 316.80, 321.53, 316.58, 314.29, 324.41, 323.88, 324.49, 322.96, 321.39,
            318.10, 313.07, 309.44, 303.67, 320.25, 320.85, 329.99, 342.01, 344.49, 349.47, 346.15,
            347.21, 349.76, 350.11, 351.47, 347.33, 350.78, 352.42, 354.45, 357.34]

    if calc_daily:
        xa_1 = daily
    else:
        xa_1 = weekly
        ema_days = 3

    xa_2 = talib.EMA(np.array(xa_1), ema_days)
    xa_2 = np.nan_to_num(xa_2)

    xa_3 = talib.EMA(np.array(xa_2), ema_days)
    xa_3 = np.nan_to_num(xa_3)

    xa_4 = talib.EMA(np.array(xa_3), ema_days)
    xa_4 = np.nan_to_num(xa_4)

    '''
    AEFG1:(XA_4-REF(XA_4,1))/REF(XA_4,1)*100;
    AEFG2:MA(AEFG1,2),COLORYELLOW,LINETHICK3;
    AEFG3:MA(AEFG1,1),COLORMAGENTA,LINETHICK3;
    '''
    AEFG1 = [0.0] * ema_days
    for i in range(ema_days, len(xa_4)):
        v = ((xa_4[i] - xa_4[i-1]) / xa_4[i-1]) * 100
        AEFG1.append(v)

    AEFG2 = talib.MA(np.array(AEFG1), 2)
    AEFG3 = talib.MA(np.array(AEFG1), 1)
    AEFG2 = np.nan_to_num(AEFG2)
    AEFG3 = np.nan_to_num(AEFG3)

    x = range(1, len(xa_1) + 1)

    start_index = ema_days + 20
    plt.subplot(2, 1, 1)
    # basic line
    plt.plot(x[start_index:], xa_1[start_index:], label="basic")

    plt.subplot(2, 1, 2)
    plt.plot(x[start_index:], AEFG2[start_index:], label="AEFG2")
    plt.plot(x[start_index:], AEFG3[start_index:], label="AEFG3")

    plt.show()


if __name__ == '__main__':
    show(3)
    show(5)
    show(10)
    show(3, False)
