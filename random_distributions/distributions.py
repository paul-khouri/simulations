import numpy as np

def create_csv_list(f, header_list, two_D_List):
    writeFile = open(f, "w")
    header_string = ','.join(header_list)+'\n'
    writeFile.write(header_string)
    print(header_string)
    for x in two_D_List:
        value_string =','.join(str(e) for e in x)
        row = "{}\n".format(value_string )
        writeFile.write(row)
    writeFile.close()

def list_and_csv(s):
    '''
    Copy ndarray to python list and create csv column

    Parameters:
        s (ndarray): number set

    Returns:
        None
    '''
    L = []
    for x in s:
        L.append([x])
        #print(x)
    create_csv_list("test.csv", ["set"], L)

def norm_set():
    mu = 15
    sigma = 6
    s = np.random.normal(mu,sigma,15)
    print(s)
    print(type(s))
    np.ndarray.sort(s)
    print(s)
    np.around(s,0)
    print(s)
    print(np.round(s,decimals=1))
    z=np.round(s,decimals=1)
    print(np.round(s,decimals=0).astype(int))
    y= np.round(s,decimals=0).astype(int)
    L=[]
    for x in y:
        L.append([x])
        print(x)
    create_csv_list("test.csv", ["set"], L)

def binomial_set():
    n = 10
    p = 0.5
    size = 1000
    s = np.random.binomial(n, p, size)
    np.ndarray.sort(s)
    list_and_csv(s)
    #print(s)

def poisson_set():
    lam = 10
    size = 14
    s = np.random.poisson(lam, size)
    np.ndarray.sort(s)
    list_and_csv(s)
    print(s)

def uniform_set():
    a= 14
    b= 25
    size=15
    s = np.random.uniform(a,b, size).astype(int)
    np.ndarray.sort(s)
    list_and_csv(s)
    print(s)

def exponential_set():
    scale = 10 # 1/lambda
    size = 15
    s = np.random.exponential(scale=scale, size=size).astype(int)
    np.ndarray.sort(s)
    print(s)
    L=[]
    for x in s:
        L.append([x])
        print(x)
    create_csv_list("test.csv", ["set"], L)




if __name__ == "__main__":
    binomial_set()
    #poisson_set()
    #uniform_set()
    #exponential_set()
    #norm_set()
    #print("hello")
