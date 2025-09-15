from player_review_logic import PlayerReviewLogic, Player


def main():
    """Main function to run the player review system."""
    review_logic = PlayerReviewLogic()

    while True:
        print("\nPlayer Review System")
        print("1. Display Player Reviews")
        print("2. Add Player Review")
        print("3. Update Player Review")
        print("4. Delete Player Review")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Fetch reviews and display them
            review_logic.display_player_reviews()
        elif choice == '2':
            # Get information of the player to add the review
            name = input("Enter player's name: ")
            goals = int(input("Enter number of goals: "))
            assists = int(input("Enter number of assists: "))
            appearances = int(input("Enter number of appearances: "))
            MOTM = int(input("Enter number of Man of the Match awards: "))
            player = Player(name, goals, assists, appearances, MOTM)
            review_logic.add_player_review(player)
        elif choice == '3':
            # Get the different information of the player to update their
            # review
            name = input("Enter player's name to update: ")
            goals = int(input("Enter new number of goals: "))
            assists = int(input("Enter new number of assists: "))
            appearances = int(input("Enter new number of appearances: "))
            MOTM = int(input("Enter new number of Man of the Match awards: "))
            player = Player(name, goals, assists, appearances, MOTM)
            review_logic.update_player_review(player)
        elif choice == '4':
            # Get the name of the player who's review you want to delete then
            # delete
            name = input("Enter player's name to delete: ")
            review_logic.delete_player_review(name)
        elif choice == '5':
            # Exit the system
            print("Exiting the Player Review System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
