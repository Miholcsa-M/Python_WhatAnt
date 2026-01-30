import csv

CSV_FILE = "romanian_ants_iteration2_habitat_10classes_corrected.csv"


class Species:
    def __init__(self, name, author, year, habitat, strategy):
        self.name = name
        self.author = author
        self.year = year
        self.habitat = habitat
        self.strategy = strategy

    def short(self):
        return self.name

    def antwiki_url(self):
        # Formica rufa -> https://www.antwiki.org/wiki/Formica_rufa
        return "https://www.antwiki.org/wiki/" + self.name.replace(" ", "_")

    def full_info(self):
        return (
            f"Species: {self.name}\n"
            f"  Author: {self.author}\n"
            f"  Year: {self.year}\n"
            f"  Habitat: {self.habitat}\n"
            f"  Competition strategy: {self.strategy}\n"
            f"  AntWiki link: {self.antwiki_url()}"
        )


def load_species(filename):
    species_list = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            species_list.append(
                Species(
                    row["Species"].strip(),
                    (row["Author"] or "").strip(),
                    row["Year"],
                    (row["Habitat"] or "").strip(),
                    (row["Competition_Strategy"] or "").strip()
                )
            )
    return species_list


def display_main_menu():
    print("\n=== Romanian Ant Species Project ===")
    print("1. Iteration 1 – Basic operations (name-based)")
    print("2. Iteration 2 – Detailed species information")
    print("3. Exit")


# ------------------ ITERATION 1 ------------------ #

def iteration1_menu():
    print("\n--- Iteration 1: Basic operations ---")
    print("1. Search species by exact name")
    print("2. Filter species by starting text")
    print("3. Show all species in alphabetic order")
    print("4. Back to main menu")


def iteration1(species_list):
    while True:
        iteration1_menu()
        choice = input("Choose option (1–4): ")

        if choice == "1":
            name = input("Species name (e.g. Formica rufa): ").lower()
            found = None
            for sp in species_list:
                if sp.name.lower() == name:
                    found = sp
                    break
            if found:
                print(f"\nFound species: {found.name}")
                print(f"(Author: {found.author}, Year: {found.year})")
            else:
                print("\nSpecies not found.")

        elif choice == "2":
            pattern = input("Start with (e.g. 'Formica' or 'Lasius n'): ").lower()
            matches = [sp for sp in species_list if sp.name.lower().startswith(pattern)]
            if matches:
                print(f"\nSpecies starting with '{pattern}':")
                for sp in matches:
                    print(" -", sp.name)
            else:
                print("No matches.")

        elif choice == "3":
            print("\nAll species in alphabetic order:")
            for sp in sorted(species_list, key=lambda x: x.name.lower()):
                print(" -", sp.name)

        elif choice == "4":
            break
        else:
            print("Invalid option.")


# ------------------ ITERATION 2 ------------------ #

def iteration2_menu():
    print("\n--- Iteration 2: Detailed species information ---")
    print("1. Search species by name or pattern")
    print("2. List species by habitat")
    print("3. Back to main menu")


def iteration2(species_list):
    while True:
        iteration2_menu()
        choice = input("Choose option (1–3): ")

        if choice == "1":
            pattern = input("Enter species name or pattern (e.g. 'Formica', 'rufa'): ").lower()
            matches = [sp for sp in species_list if pattern in sp.name.lower()]
            if matches:
                print(f"\nFound {len(matches)} species:")
                for sp in matches:
                    print("-" * 40)
                    print(sp.full_info())
            else:
                print("No species found.")

        elif choice == "2":
            print("\nExample habitats (case sensitive in CSV, but we compare lowercase):")
            print("  Coniferous Forest")
            print("  Mixed / Edge Forest")
            print("  Deciduous Forest")
            print("  Wet Grassland")
            print("  Mesic Grassland")
            print("  Semi-dry Grassland")
            print("  Xerothermic Grassland")
            print("  Urban / Ruderal")
            print("  Soil & Leaf Litter")
            print("  Wetland / Marsh")
            habitat = input("\nEnter habitat exactly as written above: ").lower()
            matches = [sp for sp in species_list if sp.habitat.lower() == habitat]
            if matches:
                print(f"\nSpecies in habitat '{habitat}':")
                for sp in matches:
                    print("-" * 40)
                    print(sp.full_info())
            else:
                print("No species found in this habitat.")

        elif choice == "3":
            break
        else:
            print("Invalid option.")


# ------------------ MAIN ------------------ #

def main():
    species_list = load_species(CSV_FILE)

    while True:
        display_main_menu()
        choice = input("Choose option (1–3): ")

        if choice == "1":
            iteration1(species_list)
        elif choice == "2":
            iteration2(species_list)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()