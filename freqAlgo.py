def freq():
    file_path="C:/Users/Asawari/Desktop/speech.txt"
    f = open(file_path, "r")
    val = f.read()
    f.close()

    length = len(val)
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict_var = {}
    for x in str1:
        dict_var[x]=0
    for x in str2:
        dict_var[x]=0

    for i in val:
        i = str(i)
        if i in dict_var:
            if dict_var[i]==0:
                dict_var[i]=1
            else:
                dict_var[i]=dict_var[i]+1

    for key in dict_var.keys():
        print(key,":",(dict_var[key]/length)*100)


if __name__=="__main__":
    freq()