import random, sys

# Seed the randomness for unittesting
if len(sys.argv) > 1:
    random.seed(sys.argv[1])

def get_new_skin() -> str:
    """
        Get a random player skin! The function
        returns a string that declares how rare
        the skin is.

        The skin can be `COMMON`, `RARE`, `EPIC`
        or `LEGENDARY`.
    """

    r = random.randint(1, 100)

    if r == 1:
        return 'LEGENDARY'
    elif r <= 5:
        return 'EPIC'
    elif r <= 40:
        return 'RARE'
    else:
        return 'COMMON'
