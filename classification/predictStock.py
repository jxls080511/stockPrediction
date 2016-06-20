from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

import os
import pickle

def train_data(filePath):
    data=[]
    target=[]
    with open(filePath,'r',encoding='utf-8') as f:
        for line in f:
            array=line.split('\t')
            l=list(0 for i in range(len(array)-2))
            for i in range(1,len(array)-2):
                l[i]=int(array[i])
            data.append(l)
            target.append(int(array[len(array)-1]))
    
    #clf=RandomForestClassifier()
    try:
        clf=svm.SVC(kernel='rbf')
        #clf=RandomForestClassifier()
        #clf=GaussianNB()
        #clf=tree.DecisionTreeClassifier()
        
        clf.fit(data, target)
        return clf
    except:
        return None
    



def test_data(clf,testFile):
    sum=0
    right_sum=0
    with open(testFile,'r',encoding='utf-8') as f:
        for line in f:
            sum+=1
            array=line.split('\t')
            v=int(array[len(array)-1])
            l=list(0 for i in range(len(array)-2))
            for i in range(1,len(array)-2):
                l[i]=int(array[i])
            result=clf.predict(l)
            if(result==v):
                right_sum+=1
            print(str(v)+'\t'+str(result))
    print('precision='+str(right_sum/(sum+0.0)))
    print(str(right_sum)+'/'+str(sum))
    return right_sum/(sum+0.0)

def perdict_all():
    trainDir='I:\\MLHomework\\\Data\\4\\trainData4m'
    testDir='I:\\MLHomework\\\Data\\4\\testData4m'
    clfDir='I:\\MLHomework\\\Data\\2\\clf8'#分类器保存位置
    
    out=open('I:\\MLHomework\\\Data\\2\\result_svm3.txt','w',encoding='utf-8')
    #数据统计
    sum=0
    pn_list=[0,0,0,0,0,0,0,0,0,0]#分别表示准确率50-60的，60-70的，70-80的，80-90的，90-100的数量
    #训练数据文件夹
    for filename in os.listdir(trainDir):
        #测试数据文件夹
        if(filename in os.listdir(testDir)):
            print(filename[0:len(filename)-9])
            clf=train_data(trainDir+'\\'+filename)
            
            if(clf!=None):
                p=test_data(clf,testDir+'\\'+filename)
                sum+=1
                #把这个股票代码保存起来
                out.write(filename[0:len(filename)-9]+'\t'+str(p)+'\n')

                if(p>=0.8):
                    #把分类器保存起来
                    with open(clfDir+'\\'+filename[0:len(filename)-9],'bw') as f:
                        pickle.dump(clf,f)
#                     if(os.path.exists(trainDir+'\\'+filename)):
#                         os.remove(trainDir+'\\'+filename)
#                     if(os.path.exists(testDir+'\\'+filename)):
#                         os.remove(testDir+'\\'+filename)
                if(p==1):#防止在1的时候数组出界
                    p-=0.01

                pn_list[int((p*100)/10)]=pn_list[int((p*100)/10)]+1
                
                for i in range(10):
                    print(str(i*10)+'~'+str(10+i*10)+'='+str(pn_list[i])+'\t\t\t占'+str(pn_list[i]/(sum+0.0)))
    out.close()

def perdict_193Stock(clfDir,testDataPath,outFilePath):
    l=list(0 for i in range(2892))#一共中国股票是2892维/个
    with open(testDataPath,'r',encoding='utf-8') as f:
        for line in f:
            array=line.split('\t')
            for i in range(2892):
                l[i]=array[i]
            
            
    out=open(outFilePath,'w',encoding='utf-8')
    for filename in os.listdir(clfDir):
        print(filename)
        with open(clfDir+'\\'+filename,'br') as f:
            clf=pickle.load(f)
            result=clf.predict(l)
            out.write(filename+'\t'+str(result[0])+'\n')
    out.close()
    

if __name__ == '__main__':
    #perdict_193Stock('I:\\MLHomework\\Data\\2\\clf','I:\\MLHomework\\1dayData.txt','I:\\MLHomework\\1dayDataResult.txt')
    perdict_all()