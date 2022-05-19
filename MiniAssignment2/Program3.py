#Adding Sublist
class Sublist:
    lst1=[]
    lst1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    lst1[2][1][2].extend(["h", "i", "j"])
    print('Updated List', lst1)