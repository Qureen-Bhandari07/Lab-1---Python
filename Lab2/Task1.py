def simple_reflex_agent(light):
    if light=='Green':
        return("GO")
    elif light=='Yellow':
        return('Green light is ending, slow down.')
    elif light=='Red':
        return('STOP')
    else:
        return 'INVALID SIGNAL!'
    
print("********** Simple Reflex Agent **********\n")
print("Program by: Qureen Bhandari")
print("Roll no: 24 \n")

print("When Light is Red")
action = simple_reflex_agent('Green')
print('Action : ',action)

print('\nWhen light is yellow')
action = simple_reflex_agent('Yellow')
print("Action : ",action)

print('\nWhen light is Red')
action = simple_reflex_agent('Red')
print("Action : ",action)
