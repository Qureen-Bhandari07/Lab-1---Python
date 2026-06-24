def simple_reflex_agent(light):
    if light == "Red":
        return "Stop"
    elif light == "Yellow":
        return "Slow Down"
    elif light == "Green":
        return "Go"
    else:
        return "Invalid Signal"


print("***** Testing Simple Reflex Agent *****\n")

percepts = ["Red", "Yellow", "Green", "Red"]

for p in percepts:
    print("Percept:", p)
    print("Action:", simple_reflex_agent(p))
    print()