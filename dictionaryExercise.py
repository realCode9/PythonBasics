dictEmp = {
    "name" : "Varun",
    "company" : "Emids",
    "age" : 28,
    "location" : "Remote",
    "dept" : "IT"
}

print("Employee dictionary is below")
print(dictEmp)
print(len(dictEmp))
dictEmp["dept"] = "Sales"                            #add item with already existing key to verify dictionary not allow items with duplicate keys
print(dictEmp)                  #this will overwrite value assigned to the duplicate key with new value

dictEmp["weight"] = 60.5        #add item with float data type
print(dictEmp)                  #{'name': 'Varun', 'company': 'Emids', 'age': 28, 'location': 'Remote', 'dept': 'Sales', 'weight': 60.5}
                                #this shows that dictionary can have data with multiple data types

dictEmp["personal"] = {"mobile": 8989787878, "address": "pune"}
print(dictEmp)
dictEmp["empInfo"] = (1234, 4534, "Shrivastava")
print(dictEmp)

empDictPrepare = dict(Name= "Varun", List = "Shweta", Birthday= "2004")       #Use of dictionary constructor to create dictionary
print(empDictPrepare)

print(empDictPrepare.get("Name"))
print(empDictPrepare.keys())            #this keys return list of keys of dictionary
print(empDictPrepare.values())          #this values return list of values of dictionary

#access whole dictionary item with key value using for loop

for x, y in empDictPrepare.items():
    print("Item key is " + x + " and value is " + y)

if "Name" in empDictPrepare.keys():
    print("Key is present in dict")

if "Shweta" in empDictPrepare.values():
    print("Value  is present in dict")

poppedItem = empDictPrepare.pop("Birthday")         #this will remove value with given key i.e birthday
print(poppedItem)           #popped item value is 2004
print(empDictPrepare)           #{'Name': 'Varun', 'List': 'Shweta'}

empDictPrepare.popitem()        #this popItem method remove last inserted item in to the dictionary
print(empDictPrepare)       #{"Name": "Varun"}

copiedDict = dictEmp.copy()
print("Print Copied Dictionary Is Here")
print(copiedDict)       #{'name': 'Varun', 'company': 'Emids', 'age': 28, 'location': 'Remote', 'dept': 'Sales', 'weight': 60.5, 'personal': {'mobile': 8989787878, 'address': 'pune'}, 'empInfo': (1234, 4534, 'Shrivastava')}
