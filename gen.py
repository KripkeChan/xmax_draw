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
    'Elise', 
    'Mario',
    'Chris'
]

# Function to generate a random password
def generate_random_password(length=6):
    # Ensure the first character is a letter
    first_char = random.choice(string.ascii_letters)
    # Generate the remaining characters
    remaining_chars = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation.replace('"', '').replace("'", '').replace('\\', '')) for _ in range(length - 1))
    password = first_char + remaining_chars
    return password

# Create the output
A = []
B = []

# Shuffle the usernames to ensure randomness
random_usernames = usernames.copy()
random.shuffle(random_usernames)

# Create a list of used usernames for B
used_usernames = set()

for username in random_usernames:
    password = generate_random_password()
    A.append(f"'{password}': '{password}', //( {username} )")

    # Select a different other username, ensuring it does not match the current username and has not been used yet
    other_usernames = [u for u in usernames if u != username and u not in used_usernames]

    if other_usernames:  # Ensure there is at least one other username available
        other_username = random.choice(other_usernames)
        used_usernames.add(other_username)  # Mark this username as used
        B.append(f"'{password}': {{ name: '{other_username}', photo: 'images/{username.replace(' ', '_')}.jpg' }},")

# Print the output for A
print("A:")
for line in A:
    print(line)

# Print the output for B
print("\nB:")
for line in B:
    print(line)