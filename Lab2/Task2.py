previous_light = None

def model_based_agent(current_light):
    global previous_light

    #decision based on current light and memory
    if previous_light == "Green" and current_light == "Yellow":
        action = 'Prepare to stop'

    elif current_light == 'Red':
        action = 'STOP'

    elif current_light == 'Yellow':
        action = 'Slow Down'
    
    else:
        action = 'Invalid Signal'

    #Update memory
    previous_light = current_light

    return action
print("********** Model-Based Agent **********\n")
print("Program by: Qureen Bhandari")
print("Roll no: 24")

print('Initaially Previous Light State : ', previous_light)

print("\n The percept sequence is (Green) ")
action =  model_based_agent("Green")
print("Action : ", action)
print("Memory contains : ",previous_light)

print('\nThe percept sequence is (Yellow)')
action =  model_based_agent('Yellow')
print("Action : ", action)
print("Memory contains : ",previous_light)

print("\nThe percept sequence is (Red) ")
action =  model_based_agent("Red")
print("Action : ", action)
print("Memory contains : ",previous_light)

print("\nThe percept sequence is (Green)")
action = model_based_agent("Green")
print("Action : ",action)
print("Memory contains : ",previous_light)
