j=0
k=0
m=0
m_numbers={}
m_prime_factorizations={}
m_prime_numbers={}
while k<1:
     print("what")
     if j not in m_numbers.keys():
         m_numbers[j]=((4*j)+1)
     i=j
     m_prime_factors=[]
     while i != 0:
         if m_numbers[j]%m_numbers[i]==0:
             if i!=j:
                 m_prime_factors.append(m_numbers[i])
         i-=1
     if not m_prime_factors:
         print("m prime number:")
         print (m_numbers[j])
         m_prime_numbers[m]=m_numbers[j]
         m+=1
     elif len(m_prime_factors)==4:
         print("found it!")
         print(m_prime_factors)
         print(m_numbers[j])
         k+=1;
     else:
         print ("m factorable number: ")
         print (m_numbers[j])
         print (m_prime_factors)
         m_prime_factorizations[m_numbers[j]]=m_prime_factors

     j+=1;
print (m_prime_numbers)
