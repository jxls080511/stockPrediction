import os
import pickle

def calc():
    log_out=open('I:\\MLHomework\\Data\\2\\clf8.log','w',encoding='utf-8')#log文件
    result_out=open('I:\\MLHomework\\Data\\2\\result8.log','w',encoding='utf-8')#log文件
    clf_dir='I:\\MLHomework\\Data\\2\\clf8'
    #先读入5-8月中国股市的数据
    chinese_stock={}
    with open('I:\\MLHomework\\Data\\4\\testData4m\\ASX.csv.data','r',encoding='utf-8') as f:
        for line in f:
            array=line.split('\t')
            date=array[0]
            v=int(array[len(array)-1])#最后的值不需要了
            l=list(0 for i in range(len(array)-2))
            for i in range(1,len(array)-2):
                l[i]=int(array[i])
            chinese_stock[date]=l
    
    us_stock_record={}
    for filename in os.listdir(clf_dir):
        us_stock_record[filename]={}
        with open('I:\\MLHomework\\stockData_american\\'+filename+'.csv','r',encoding='utf-8') as f:
            firstline=True#第一行不是数据
            for line in f:
                if(firstline):
                    firstline=False
                    continue
                else:
                    array=line.strip().split(',')
                    date=array[0]
                    openValue=float(array[1])
                    closeValue=float(array[4])
                    l=list(0 for i in range(2))
                    l[0]=openValue
                    l[1]=closeValue
                    us_stock_record[filename][date]=l
    
    money=1000000.0
    #for循环，每一天
    for year in range(2015,2016):
        for month in range(5,9):
            for day in range(1,32):
                date=str(year)+'-'
                if(month<10):
                    date+='0'+str(month)+'-'
                else:
                    date+=str(month)+'-'
                    
                if(day<10):
                    date+='0'+str(day)
                else:
                    date+=str(day)  
                #此时的date是一个日期string
                
                if(date in chinese_stock.keys()):
                    print(date+'\t'+str(money))
                    result_out.write(str(money)+'\n')
                    log_out.write(date+'\t'+str(money)+'\n')
                    #得到当天的中国股市情况
                    l=chinese_stock[date]
                    #对于高准确率的股票进行预测，并记下当天的开盘价收盘价
                    us_stock={}#记录美股的预测情况
                    buy_num=0#今天需要买入的股票数量
                    for stock_name in os.listdir(clf_dir):
                        record=list(0 for i in range(3))
                        #读入分类器
                        with open(clf_dir+'\\'+stock_name,'br') as f:
                            clf=pickle.load(f)
                            result=clf.predict(l)
                            if(1==result):
                                buy_num+=1
                            try:
                                record[0]=int(result[0])#第一列存预测结果
                                record[1]=us_stock_record[stock_name][date][0]#开盘价
                                record[2]=us_stock_record[stock_name][date][1]#收盘价
                            except:
                                #print('error')
                                #buy_num=0#如果出现异常，就不交易了，日期报错
                                record[0]=0;
                                if(1==result):
                                    buy_num-=1
                        us_stock[stock_name]=record
                    
                    #计算今天的收益
                    if(buy_num!=0):
                        div_money=(money+0.0)/buy_num
                        today_sum_money=0.0
                        for stock_name in us_stock.keys():
                            if(us_stock[stock_name][0]==1):
                                p=(us_stock[stock_name][2]+0.0)/us_stock[stock_name][1]#收益率
                                earn=div_money*(p-1.0)
                                today_sum_money+=div_money*p
                                log_out.write(stock_name+'\t'+str(us_stock[stock_name][1])+'\t'+str(us_stock[stock_name][2])+'\t'+str(earn)+'\n')
                        #以收盘价卖出所有股票
                        money=today_sum_money
    log_out.close()
    result_out.close()
    return money                
    
        
    
    #返回最后剩下的钱
    

if __name__ == '__main__':
    print(calc())