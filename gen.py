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

for username in usernames:
    password = generate_random_password()
    A.append(f"\'{password}\': \'{password}\', //( {username} )")

    # Select a different other username, ensuring it does not match the current username
    other_usernames = [u for u in usernames if u != username]
    other_username = random.choice(other_usernames)

    B.append(f"\'{password}\': {{ name: \'{other_username}\', photo: \'images/{username.replace(' ', '_')}.jpg \'}},")

# Print the output
for line in A:
    print(line)

for line in B:
    print(line)

