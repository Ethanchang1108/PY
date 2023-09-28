consum = input('請輸入消費金額')
#輸入金額
consum = int(consum)
#轉換型態
BGive = consum//5000
#計算回饋金600的次數
r = consum%5000
#計算餘數
SGive = r/1000
#計算回饋100的次數
SGive = int(SGive)
#轉換型態
sumgive = 100*SGive + 600*BGive 
#計算總體回饋金
print ('回饋金：' + str(sumgive))
#輸出回饋金的經額

#計算餘數
if (4000<r):
#判斷要不要用600會饋金的規則
    y = r-5000
    #計算差多少
    print('再消費' + str(-y) + '可多得回饋金200喔！' )
    #輸出

elif 0 == r%1000 :
#判斷要不要用剛剛好整除的規則
    print(0)
    #輸出
else :
    #用100回饋金的規則
    srec = consum%1000
    x = srec-1000
    #計算差多少
    print('再消費' + str(-x) + '可多得回饋金100喔！')
    #輸出



