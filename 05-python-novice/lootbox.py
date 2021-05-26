import rewards

common = 0
rare = 0
epic = 0
legendary = 0

for i in range(5):
    reward_new = rewards.get_new_skin()
    if reward_new == "COMMON":
        common += 1
    elif reward_new == "RARE":
        rare += 1
    elif reward_new == "EPIC":
        epic += 1
    elif reward_new == "LEGENDARY":
        legendary += 1
if common > 0:
    print(common, "x common")
if rare > 0:
    print(rare, "x rare")
if epic > 0:
    print(epic, "x epic")
if legendary > 0:
    print(legendary, "x legendary")
