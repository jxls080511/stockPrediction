import os
#起止年月，end年份月份不包含，usDir是美股数据的文件夹位置，outDir是输出（训练/测试）文件的位置
def getData(startY,endY,startM,endM,usDir,outDir):    
    record_dict={}
    for filename in os.listdir('I:\\MLHomework\\stockData_china'):
        print(filename)
        stock_dict={}
        with open('I:\\MLHomework\\stockData_china\\'+filename,'r',encoding='utf-8') as f:
            firstline=True
            for line in f:
                if(firstline):
                    firstline=False
                    continue
                else:
                    array=line.strip().split(',')
                    date=array[0]
                    openValue=float(array[1])
                    closeValue=float(array[4])
                    rise=1#上涨
                    if(closeValue<=openValue):
                        rise=0#下跌
                    stock_dict[date]=rise
        record_dict[filename]=stock_dict
    

    for us_filename in os.listdir(usDir):
        print('us'+us_filename)
        target_dict={}
        with open(usDir+'\\'+us_filename,'r',encoding='utf-8') as f:
            firstline=True
            for line in f:
                if(firstline):
                    firstline=False
                    continue
                else:
                    array=line.strip().split(',')
                    date=array[0]
                    openValue=float(array[1])
                    closeValue=float(array[4])
                    rise=1#上涨
                    if(closeValue<openValue):
                        rise=0#下跌
                    target_dict[date]=rise
    
        out=open(outDir+'\\'+us_filename+'.data','w',encoding='utf-8')
#         out2=open('I:\\MLHomework\\china_sequence.txt','w',encoding='utf-8')
#         first=True
        #用2015-1-1到2015-4-30的数据作为训练数据
        for year in range(startY,endY):
            for month in range(startM,endM):
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
                
                    #遍历所有中国股票
                    if(date in target_dict.keys()):
                        out.write(date+'\t')
                        for stockID in record_dict.keys():
                            #我需要中国股票作为训练数据的顺序输出成文件给我
#                             if(first):
#                                 out2.write(stockID[0:len(stockID)-4]+'\n')
#                             else:
#                                 out2.close()
                            stock_dict=record_dict[stockID]
                            if(date in stock_dict.keys()):
                                out.write(str(stock_dict[date])+'\t')
                            else:
                                out.write('0\t')
                        first=False            
                        #把这个股票的涨跌当做结果写在最后
                        out.write(str(target_dict[date])+'\n')

        out.close()
                      
if __name__ == '__main__':
    getData(2015,2016,5,9,'I:\\MLHomework\\stockData_american','I:\\MLHomework\\Data\\4\\testData4m')