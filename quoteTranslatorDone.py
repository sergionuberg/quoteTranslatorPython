def display_menu():
    print("\nchoose a language to translate the quote:")
    print("1. english")
    print("2. french")
    print("3. spanish")
    print("4. exit")

def get_translation(choice):
    if choice == "1":
        return "success is the product of daily habits, not once-in-a-lifetime transformation."
    elif choice == "2":
        return "le succès est le produit d'habitudes quotidiennes, pas d'une transformation unique dans une vie."
    elif choice == "3":
        return "el éxito es el resultado de hábitos diarios, no de una transformación única en la vida."
    else:
        return None

def main():
    while True:
        display_menu()
        user_choice = input("enter your choice from 1 to 4: ").strip()
        
        if user_choice == "4":
            print("exiting the program")
            break
        
        translation = get_translation(user_choice)
        if translation:
            print("\nquote:")
            print(f"{translation}")
        else:
            print("invalid choice, can you please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
