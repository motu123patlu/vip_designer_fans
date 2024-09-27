class Fan:
    def __init__(self, name, email, is_vip=False):
        self.name = name
        self.email = email
        self.is_vip = is_vip
        self.perks = []

    def make_vip(self):
        self.is_vip = True
        self.perks = ["Exclusive content", "Early access to events", "Personalized messages"]
        print(f"{self.name} has been upgraded to VIP status!")

    def get_info(self):
        status = "VIP" if self.is_vip else "Regular"
        return f"Name: {self.name}, Email: {self.email}, Status: {status}"

    def show_perks(self):
    
        if self.is_vip:
            print(f"Special Perks for {self.name}:")
            for perk in self.perks:
                print(f"- {perk}")
        else:
            print(f"{self.name} is a regular fan. No special perks available.")


class VIPExperience:
    def __init__(self):
        self.fans = []

    def add_fan(self, name, email):
        fan = Fan(name, email)
        self.fans.append(fan)
        print(f"{name} has been added as a regular fan.")

    def upgrade_to_vip(self, email):
        for fan in self.fans:
            if fan.email == email:
                fan.make_vip()
                return
        print("Fan not found!")

    def list_fans(self):
        print("\nFans List:")
        for fan in self.fans:
            print(fan.get_info())

    def show_vip_experience(self, email):
        for fan in self.fans:
            if fan.email == email:
                fan.show_perks()
                return
        print("Fan not found!")

# User interface to interact with the VIP Experience program
def main():
    experience = VIPExperience()

    while True:
        print("\n--- VIP Fans Designer Experience ---")
        print("1. Add a Fan")
        print("2. Upgrade Fan to VIP")
        print("3. List All Fans")
        print("4. Show VIP Experience (Perks)")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter fan's name: ")
            email = input("Enter fan's email: ")
            experience.add_fan(name, email)

        elif choice == '2':
            email = input("Enter fan's email to upgrade to VIP: ")
            experience.upgrade_to_vip(email)

        elif choice == '3':
            experience.list_fans()

        elif choice == '4':
            email = input("Enter fan's email to view VIP perks: ")
            experience.show_vip_experience(email)

        elif choice == '5':
            print("Exiting the VIP Fans Designer Experience. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
output:
# Run the program
if __name__ == "__main__":
    ma--- VIP Fans Designer Experience ---
1. Add a Fan
2. Upgrade Fan to VIP
3. List All Fans
4. Show VIP Experience (Perks)
5. Exit
