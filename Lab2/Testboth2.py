world_model = {"previous_light": None}

def model_based_agent(current_light):

    if (world_model["previous_light"] == "Green"
            and current_light == "Yellow"):
        action = "Prepare to Stop"

    elif current_light == "Red":
        action = "Stop"

    elif current_light == "Yellow":
        action = "Slow Down"

    elif current_light == "Green":
        action = "Go"

    else:
        action = "Invalid Signal"

    world_model["previous_light"] = current_light

    return action


print("***** Testing Model-Based Agent *****\n")

percepts = ["Green", "Yellow", "Red", "Green"]

for p in percepts:
    print("Percept:", p)
    print("Action:", model_based_agent(p))
    print("Memory:", world_model)
    print()