import random
import string

# List of usernames
usernames = [
    'Dr. curry',
    'Pacco',
    'Hai so',
    'Hai jai',
    'Carol',
    'Yenny',
    'Jasmine',
    'Vincent',
    'Fat boy',
    'Yumi',
    'Fung fung',
    'Justin',
    'Jacky',
    'Leo',
    'Kwan B',
    'allison',
    'Jensen',
    'Elise'
]

# Function to generate a random password
def generate_random_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Create the output
A = []
B = []

# Shuffle the usernames to ensure randomness
random_usernames = usernames.copy()
random.shuffle(random_usernames)

# Generate entries for A and B
for i, username in enumerate(random_usernames):
    password = generate_random_password()
    A.append(f"A: '{password}': '{password}', //( {username} )")

    # Select a different other username, ensuring it does not match the current username
    other_usernames = [u for u in random_usernames if u != username]
    other_username = random.choice(other_usernames)

    B.append(f"B: '{password}': {{ name: '{other_username}', photo: 'images/{other_username.replace(' ', '_')}.jpg' }}")


# Print the output
for line in A:
    print(line)

for line in B:
    print(line)

