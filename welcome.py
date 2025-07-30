x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

if __name__ == "__main__": 
    myfunc()
    print("Python is " + x)
    txt = "Hello, And Welcome!"
    print(txt.lower())
    print(txt.upper())
    print(txt.replace("H", "J")) 
    print(txt.split(",")) # returns ['Hello', ' And Welcome!']
    if str.title('and') in txt:
        print(f'Yes and present in {txt}')
    else:
        print(f'No and not present in {txt}')
    print(txt.strip()) # returns "Hello, And Welcome!"
    print(txt.replace('Hello','Hi') ) 
    zx = 'check encoding \"'
    print(zx.encode(encoding="ascii",errors="replace"))
    for x in txt:
        print(x)

        
    


    

    

   


