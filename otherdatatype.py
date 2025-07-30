# list
mylist = ["one","Two","Three","Four","Five"]
print(mylist)
mylist.append("Six")
print(type(mylist))
for x in mylist:
    print(x)    
newlist = [x for x in mylist if "T" in x]
print(newlist)
newlist.sort()
print(newlist)
mrglist = mylist + newlist
print (mrglist )
#tuple
mytuple = ("one","Two","Three","Four","Five")
#mytuple.__add__(
print ("Tuple")
print(mytuple)
print(type(mytuple))
for x in mytuple:
    print(x)
(One,Two,Three,Four,Five) = mytuple
print(One)
print(Two)
print(Three)
print(Four)
print(Five)
print(mytuple*2 )
print(mytuple.index("Two",))
#set
myset = {"one","Two","Three","Four","Five"}
myset.add('Six') 
print("Set")
print(myset)
print(myset)
#dictionary
mydict = {
 "type":"Student",
 "Dtls": [{   
  "id": 1 ,
  "name": "Ashish",
  "lname": "Joshi"
},
{
  "id": 2,
  "name": "Rahul",
  "lname": "Jain"
}
 ]
}
print("Dictionary")
print(mydict)
print(mydict["Dtls"][1])
for x in mydict["Dtls"][1].values():
    print(x)
[print(x["id"])  for x in mydict["Dtls"] if x["name"] == "Ashish" ]

y = next((x for x in mydict["Dtls"] if x["name"] == "Ashish"), {})
print(f"typ1 {y}")
y = {k: v for x in mydict["Dtls"] if x["name"] == "Ashish" for k, v in x.items()}
print(f"type 2 {y}")

#y = {x for x in mydict["Dtls"] if x["name"] == "Ashish" }
#print(y)

for x in mydict["Dtls"]:
    print(x.get("address","address not found"))
