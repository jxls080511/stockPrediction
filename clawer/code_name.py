import re

def china():
    out=open('D:\\programing\\Python\\MLHomework\\american_codeName.txt','w',encoding='utf-8')
    with open('D:\\programing\\Python\\MLHomework\\american_codeNameaaa.txt','r',encoding='utf-8') as f:
        for line in f:
            array=line.strip().split('\t')
            match=re.search('([^(]+)\\(([^\\)]+)\\)',array[0])
            name=match.group(1)
            code=match.group(2)
            market=array[2]
            out.write(name+'\t'+code+'\t'+market+'\n')
    out.close()
                

def american():
    out=open('D:\\programing\\Python\\MLHomework\\american_codeName2.txt','w',encoding='utf-8')
    with open('D:\\programing\\Python\\MLHomework\\美股抽取.txt','r',encoding='utf-8') as f:
        for line in f:
            array=line.strip().split('\t')
            name=''
            code=''
            market=''
            if('.NASDQ' in array[0]):
                array1=array[0].split('.NASDQ')
                market='NASDQ'
                name=array1[1].strip()
                code=array1[0].strip()
            if('.NYSE' in array[0]):
                array1=array[0].split('.NYSE')
                market='NYSE'
                name=array1[1].strip()
                code=array1[0].strip()
            if('.AMEX' in array[0]):
                array1=array[0].split('.AMEX')
                market='AMEX'
                name=array1[1].strip()
                code=array1[0].strip()
            
            out.write(name+'\t'+code+'\t'+market+'\n')
    out.close()
    
if __name__ == '__main__':
    china()
    american()