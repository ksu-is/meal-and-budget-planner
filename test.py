recipe = {} 
recipe['chicken'] = [2.50, 'chicken', 'oil', 'herbs'] #A valid key-value pair 
recipe['pasta'] = [1.5, 'pasta','sauce'] #A valid key-value pair 
recipe[3] = [['three', ['THREE', 'tHrEe']]] #It is valid too 
for k, v in recipe.items(): 
    print(k, '=>', v) 
