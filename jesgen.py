import random
import string
import pyfiglet
from faker import Faker
from colorama import *

class JesGenConsole:
    def __init__(self):
        self.prompt = "G3N > "
        self.current_generator = None
        self.generators = {
            "gen/name": self.generate_name,
            "gen/email": self.generate_email,
            "gen/phone": self.generate_phone,
            "gen/ccnum": self.generate_ccnum,
            "gen/ccexp": self.generate_ccexp
        }
        self.amount = 1
        self.fake = Faker()

    def run(self):
        result = pyfiglet.figlet_format("J3SG3N")
        print(result)
        while True:
            user_input = input(self.prompt)
            if user_input.strip() == "exit":
                break
            elif user_input.strip() == "show options":
                print(Fore.YELLOW + "=============options=============")
                for option, generator in self.generators.items():
                    print(Fore.YELLOW + f"{option:<10} {generator.__name__[9:]:<30}")
                print(Style.RESET_ALL)
            elif user_input.startswith("use"):
                generator_choice = user_input.split(" ")[1]
                if generator_choice not in self.generators:
                    print(Fore.RED + f"[-] Invalid generator choice: {generator_choice}")
                    print(Style.RESET_ALL)
                else:
                    self.current_generator = self.generators[generator_choice]
                    print(f"G3N ({self.current_generator.__name__[9:].title()} Generator) > ", end="")
            elif user_input.startswith("set amount"):
                amount = int(user_input.split(" ")[-1])
                self.amount = amount
                print(Fore.GREEN + f"[+] Amount set to {amount}")
                print(Style.RESET_ALL)
            elif user_input.strip() == "run":
                if self.current_generator is None:
                    print(Fore.RED + "[-] No generator selected. Please select a generator with the 'use' command.")
                    print(Style.RESET_ALL)
                else:
                    results = [self.current_generator() for _ in range(self.amount)]
                    print(Fore.GREEN + f"[+] Results ({len(results)}):")
                    print(Style.RESET_ALL)
                    for result in results:
                        print(Fore.BLUE + f"\t: {result}")
                        print(Style.RESET_ALL)
            else:
                print(Fore.RED + f"[-] Invalid command: {user_input}")
                print(Style.RESET_ALL)

    def generate_name(self):
        return self.fake.name()

    def generate_email(self):
        return self.fake.email()

    def generate_phone(self):
        return self.fake.phone_number()

    def generate_ccnum(self):
        return self.fake.credit_card_number()

    def generate_ccexp(self):
        return self.fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")

console = JesGenConsole()
console.run()
