# weather.py
x = "awesome" 
# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    """# Function to convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5.0/9.0

def weather(pCelcius):
     if pCelcius < 0:
         return "Freezing"
     elif (pCelcius >= 0 and pCelcius < 10):    
         return "Very Cold"
     elif (pCelcius >= 10 and pCelcius < 20):
         return "Cold"
     elif (pCelcius >= 20 and pCelcius < 30):
         return "Warm"
     elif (pCelcius >= 30 and pCelcius < 40):  
         return "Hot"
     elif (pCelcius >= 40):
         return "Very Hot"  
     

# Main code
if __name__ == "__main__":
   
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"The temperature in Celsius is: {celsius:.2f}")
    print (f"The weather is: {weather(celsius)}")   
    print((fahrenheit_to_celsius.__doc__))
    
