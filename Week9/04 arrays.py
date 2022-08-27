def MinMax(tempetures):
    tempetures.reverse()
    print(tempetures)
    tempetures.sort()
    min = tempetures[0]
    max = tempetures[-1]
    print("Month minimal temperature was:",min,"ºC")
    print("Month highest temperature was:",max,"ºC")

MinMax([9,10,11,15,4,2,1])