ch=input('1)溫度轉換 2)分蘋果問題')
#選擇
if ch== str(1):
    F=input('華氏溫度')
    #輸入華氏溫度
    F=int(F)
    #轉換型態
    C=(F-32)*(5/9)
    #轉換溫度
    print('華氏' + str(F) + '度=' + '攝氏' + str(C) + '度')
    #輸出

elif ch == str(2):
    A = input('有幾個蘋果')
    #輸入蘋果
    K = input('有幾位小朋友')
    #輸入小朋友
    A = int(A)
    #轉換型態
    K = int(K)
    #轉換型態
    X = A/K
    #計算整數
    X = int(X)
    #取出整數
    Y = A-K*X
    #計算餘數
    print('每人可分得' + str(X) + '頻果，剩下' + str(Y) + '顆蘋果')



