dctlist = {}

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_json_str(p):
    keys = ["__class__", "x", "y"] #retrieving object items
    values = [p.__class__.__name__, p.x, p.y]

    global dct #globally accessible dictionary with type: dict
    dct = dict(zip(keys,values))

    ret = "{\n"
    for i in range(len(keys)): #json formatter
        ret += f"{keys[i]} : {values[i]} \n"
    ret += "}"

    return ret
    
def read_json_str(s): 
    for i,j in dctlist.items():
        if s == j: #If the input JSON matches a value in the dictionary,
            return i #Return object name that is found (if exists)
    return "No object is found"
    

p = Point(1,2)
q = Point(12,5) #variable for test

p1 = get_json_str(p) #Print point p in JSON form and creating a global dct variable
dctlist.setdefault("p", str(dct)) #Storing point p

q1 = get_json_str(q)
dctlist.setdefault("q", str(dct))

print(f"{p1} \n") #print JSON of p (problem a)
print(f"{q1} \n") #print JSON of q for test

print(f"{dctlist} \n") #Dictionary storage test

#String of JSON to check if such an object exists (problem b)
n = read_json_str("{'__class__': 'Point', 'x': 1, 'y': 2}")
print(n)

#Let's try to find Point "q"
n = read_json_str("{'__class__': 'Point', 'x': 12, 'y': 5}")
print(n)

#Let's use wrong values
n = read_json_str("{'__class__': 'Point', 'x': 999, 'y': 999}")
print(n)

print("\n")