from tabulate import tabulate


class PlayerRepository:
    def get_player_reviews(self):
        try:
            with open("player_reviews.txt", "r") as file:
                player_reviews = file.readlines()
            return [review.strip() for review in player_reviews]
        except FileNotFoundError:
            print("Player reviews file not found.")
            return []

    def display_player_reviews(self):
        player_reviews = self.get_player_reviews()
        if not player_reviews:
            print("No player reviews found.")
            return None

        print("\nPlayer Reviews:\n")
        table = []
        headers = ["Name", "Goals", "Assists", "Appearances", "MOTM"]
        for review in player_reviews:
            parts = [part.strip() for part in review.split(",")]
            table.append(parts)
        print(tabulate(table, headers=headers, tablefmt="grid"))

    def add_player_review(self, player):
        try:
            with open("player_reviews.txt", "r") as file:
                player_reviews = file.readlines()
                for review in player_reviews:
                    # Compare names exactly (case-insensitive)
                    existing_name = review.split(",")[0].strip().lower()
                    if player.name.lower() == existing_name:
                        print(f"Player {player.name} already exists.")
                        return

            with open("player_reviews.txt", "a") as file:
                file.write(f"{player.name}, {player.goals}, {player.assists}, "
                           f"{player.appearances}, {player.motm}\n")
            print(f"Player review for {player.name} added successfully!")
        except FileNotFoundError:
            print("Player reviews file not found.")

    def update_player_review(self, player):
        try:
            with open("player_reviews.txt", "r") as file:
                player_reviews = file.readlines()

            for i, review in enumerate(player_reviews):
                if player.name.lower() in review.lower():
                    player_reviews[i] = f"{player.name}, {player.goals},\n"
                    f"{player.assists}, {player.appearances}, {player.motm}\n"
                    break
            else:
                print(f"Player {player.name} not found in reviews.")
                return

            with open("player_reviews.txt", "w") as file:
                file.writelines(player_reviews)
            print(f"Player review for {player.name} updated successfully!")
        except FileNotFoundError:
            print("Player reviews file not found.")

    def delete_player_review(self, player_name):
        try:
            with open("player_reviews.txt", "r") as file:
                player_reviews = file.readlines()

            for i, review in enumerate(player_reviews):
                if player_name.lower() in review.lower():
                    del player_reviews[i]
                    break
            else:
                print(f"Player {player_name} not found in reviews.")
                return

            with open("player_reviews.txt", "w") as file:
                file.writelines(player_reviews)
            print(f"Player review for {player_name} deleted successfully!")
        except FileNotFoundError:
            print("Player reviews file not found.")
