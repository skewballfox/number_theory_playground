j=0
k=0
m=0
m_numbers={0:1,1:5}
m_prime_factorizations={}
m_prime_numbers={}

def factors(x,known_factorizations, primes):
    y=x
    unique_factorizations=[]
    factorization=[]
    done=False
    while done==False:
        done=True
        if x not in primes.keys():
            while y!=0:
                for key in primes:
                    if primes[key]!=1:
                        while y//primes[key]==0 and y!=0:
                            print("old y and prime: ", y, primes[key])
                            factorization.append(primes[key])
                            y=y//primes[key]
                            print("new y and current factorization: ", y, factorization)
                            if y in primes.keys():
                                print ("wtf")
                                factorization.append(y)
                                y=0
                                done=False
                                break

                            elif y in known_factorizations.keys():
                                print ("hi")
                                factorization.extend(known_factorizations[y])

                                y=0
                                done=False
                                break
                if factorization:
                    unique_factorizations.append(factorization)
                    done=False
                    break


    print (unique_factorizations)
    return unique_factorizations

while k<1:
     print("what")
     if j not in m_numbers.keys():
         m_numbers[j]=((4*j)+1)
     i=j
     m_prime_factors=[]
     """while i != 0:
         if m_numbers[j]%m_numbers[i]==0:
             if i!=j:
                 m_prime_factors.append(m_numbers[i])
         i-=1
     """
     m_prime_factors=factors(m_numbers[j],m_prime_factorizations,m_prime_numbers)
     if not m_prime_factors:
         print("m prime number:")
         print (m_numbers[j])
         m_prime_numbers[m]=m_numbers[j]
         m+=1
     elif len(m_prime_factors)==2:
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
