# -*- coding: utf-8 -*- #
import urllib 
import urllib2 
import requests
import codecs
import socket

def download():
    with codecs.open('D:\\programing\\Python\\MLHomework\\china_codeName.txt','r','utf-8') as f:
        for line in f:
            array=line.strip().split('\t')
            name=array[0]
            code=array[1]
            market=array[2]
            if(u'上证'==market):
                print code+u'上证'
                url='http://table.finance.yahoo.com/table.csv?s='+code+'.ss'
                urllib.urlretrieve(url, 'D:\\programing\\Python\\MLHomework\\stockData_china\\'+code+'.ss.csv')
            elif(u'深成'==market):
                print code+u'深成'
                url='http://table.finance.yahoo.com/table.csv?s='+code+'.sz'
                urllib.urlretrieve(url, 'D:\\programing\\Python\\MLHomework\\stockData_china\\'+code+'.sz.csv')

def american_download():
    #socket.setdefaulttimeout(15)
    n=0
    with codecs.open('I:\\MLHomework\\american_codeName.txt','r','utf-8') as f:
        for line in f:
            array=line.strip().split('\t')
            name=array[0]
            code=array[1]
            market=array[2]

            n+=1
            print code,n
            url='http://table.finance.yahoo.com/table.csv?s='+code+'&d=8&e=24&f=2015&g=d&a=1&b=1&c=2010&ignore=.csv'
            try:
                urllib.urlretrieve(url, 'I:\\MLHomework\\stockData_american1\\'+code+'.csv')
            except:
                print 'error'


def china_download_day(seqFilePath,downloadDir,outDataPath,y,m,d):
    data=[]
    out=codecs.open(outDataPath,'w','utf-8')#输出data数据
    n=0
    with codecs.open(seqFilePath,'r','utf-8') as f:
        for line in f:
            array=line.strip().split('.')
            code=array[0]
            market=array[1]
            print(code+market+'\t'+str(n))
            n+=1
            savedFilePath=''
            if(u'ss'==market):
                url='http://table.finance.yahoo.com/table.csv?s='+code+'.ss&d='+str(m-1)+'&e='+str(d)+'&f='+str(y)+'&g=d&a='+str(m-1)+'&b='+str(d)+'&c='+str(y)+'&ignore=.csv'
                urllib.urlretrieve(url, downloadDir+'\\'+code+'.ss.csv')
                savedFilePath=downloadDir+'\\'+code+'.ss.csv'
            elif(u'sz'==market):
                url='http://table.finance.yahoo.com/table.csv?s='+code+'.sz&d='+str(m-1)+'&e='+str(d)+'&f='+str(y)+'&g=d&a='+str(m-1)+'&b='+str(d)+'&c='+str(y)+'&ignore=.csv'
                urllib.urlretrieve(url, downloadDir+'\\'+code+'.sz.csv')
                savedFilePath=downloadDir+'\\'+code+'.sz.csv'
            #下载完成之后就可以得到这个文件中的数据       
            with codecs.open(savedFilePath,'r','utf-8') as f:
                firstline=True
                for line in f:
                    if(firstline):
                        firstline=False
                        continue
                    else:#那些error的会出错 最后break就行
                        rise=1#上涨
                        date=''
                        try:
                            array=line.strip().split(',')
                            date=array[0]
                            openValue=float(array[1])
                            closeValue=float(array[4])
                            if(closeValue<openValue):
                                rise=0#下跌
                        except:
                            rise=0#下跌
                            print('error')
                        #组个日期字符串出来
                        dateT=str(y)+'-'
                        if(m<10):
                            dateT+='0'+str(m)+'-'
                        else:
                            dateT+=str(m)+'-'
                    
                        if(d<10):
                            dateT+='0'+str(d)
                        else:
                            dateT+=str(d)
                            
                        #如果日期和文件中的相同那就ok
                        if(dateT==date):
                            out.write(str(rise)+'\t')
                        else:
                            out.write(str(0)+'\t')
                        break
    out.close()
    
if __name__ == '__main__':
    #download()
    american_download()
    #china_download_day('I:\\MLHomework\\china_sequence.txt','I:\\MLHomework\\stockData_china_1day','I:\\MLHomework\\1dayData.txt',2015,8,26)