year=input('請輸入一個年份')
#輸入
year = int(year)
x = year%4
#計算年份
y = year%100
#計算年份
v = year%400
#計算年份
if x==0 :
#判斷是不是4的倍數
    if y==0 :
    #判斷是不是100的倍數
        if v==0:
        #判斷是不是400的倍數
            print(str(year),'是閏年')
            #輸出
        else:
           print(str(year)+'是平年')    
            #輸出
    else:
        print(str(year),'是閏年')
        #輸出
else:
    print(str (year),'是平年')
    #輸出
