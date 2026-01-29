import random
import string

def create_identity():
    providers = ["proton.me", "tuta.info", "duck.com"]
    domain = random.choice(providers)

    year = random.randint(1990, 2005)

    chars = string.ascii_letters + string.digits + "!@#$"
    password = "".join(random.sample(chars, 15))

    unique_id = hex(random.getrandbits(32))

    print(f"___ NEW IDENTITY ___")
    print(f"ID: {unique_id}")
    print(f"Born: {year}")
    print(f"Email: user_{random.randint(100, 999)}@{domain}")
    print(f"Key: {password}")

if __name__ == "__main__":
    create_identity()