from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

def test_data(clf,testFile,remove_list):
    sum=0
    right_sum=0
    with open(testFile,'r',encoding='utf-8') as f:
        for line in f:
            sum+=1
            array=line.split('\t')
            v=int(array[len(array)-1])
            l=[]
            for i in range(1,len(array)-1):
                if(i-1 not in remove_list):
                    l.append(int(array[i]))
            
            #print(len(l))   
            result=clf.predict(l)
            if(result==v):
                right_sum+=1
            #print(str(v)+'\t'+str(result))
    print('precision='+str(right_sum/(sum+0.0)))
    print(str(right_sum)+'/'+str(sum))
    return right_sum/(sum+0.0)

if __name__ == '__main__':
    #读文件
    data=[]
    target=[]
    with open('I:\\MLHomework\\Data\\2\\trainData1y\\NOBGY.csv.data','r',encoding='utf-8') as f:
        for line in f:
            array=line.split('\t')
            #print(len(array))
            l=list(0 for i in range(len(array)-2))
            for i in range(1,len(array)-1):
                l[i-1]=int(array[i])
            data.append(l)
            #print(len(l))  
            target.append(int(array[len(array)-1]))
    
            
    # create a base classifier used to evaluate a subset of attributes
    #model = RandomForestClassifier()
    remove_list=[]
    
    print('RandomForestClassifier')
    clf=RandomForestClassifier()
    clf.fit(data, target)
    test_data(clf,'I:\\MLHomework\\Data\\2\\testData8m\\NOBGY.csv.data',remove_list)
    print('SVM')
    clf11=svm.SVC(kernel='rbf')
    clf11.fit(data, target)
    test_data(clf11,'I:\\MLHomework\\Data\\2\\testData8m\\NOBGY.csv.data',remove_list)
    
    print('1')
    for i in range(0,len(clf.feature_importances_)):
        if(clf.feature_importances_[i]==0.0):
            remove_list.append(i)
    print(len(remove_list))
    #读文件
    data2=[]
    target2=[]
    with open('I:\\MLHomework\\Data\\2\\trainData1y\\NOBGY.csv.data','r',encoding='utf-8') as f:
        for line in f:
            array=line.split('\t')
            l=[]
            for i in range(1,len(array)-2):
                if(i-1 not in remove_list):
                    l.append(int(array[i]))
            data2.append(l)
            target2.append(int(array[len(array)-1]))
            
    print('RandomForestClassifier')
    clf2=RandomForestClassifier()
    clf2.fit(data2, target2)
    test_data(clf2,'I:\\MLHomework\\Data\\2\\testData8m\\NOBGY.csv.data',remove_list)
    print('SVM')
    clf22=svm.SVC(kernel='rbf')
    clf22.fit(data2, target2)
    test_data(clf22,'I:\\MLHomework\\Data\\2\\testData8m\\NOBGY.csv.data',remove_list)
#     for importance in clf.feature_importances_:
#         print(importance)
        
