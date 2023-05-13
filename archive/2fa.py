
import secrets

input_text = input("Enter 2FA code: ") # This is where the user inputs the 2FA code
def create2fa(): # Let's say this function creates a 2FA code with random shit and returns it back to where we call the function
  code = secrets.token_hex(6) # Using the library secrets we can create this with ease
  return code # Returns the code after completed

def login_function():
  fa_code = create2fa() # This establishes what 2fa_code is; example '6a4b8a64201f'
  user.send(fa_code) # Sends the code to the user through discord
  if input_text == fa_code: # checks if the inputed code is = to the actual code
    print("Logged in!") # Prints logged in
  else: # Else statement if the input does not match
    print("Wrong 2FA!") #Prints wrong 2FA

