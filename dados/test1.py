
  
with open('dado1.txt', 'r+',  encoding='UTF-8', ) as arquivo: 
    txt = arquivo.readlines()

for l in txt :
   
    
    with open('result1.txt', 'a+', encoding='UTF-8') as arquivo2:
       
        arquivo2.write(l+'",' '\n')

  




