from data_access import PlayerRepository


class PlayerReviewLogic:
    def __init__(self):
        self.player_repository = PlayerRepository()

    def get_player_reviews(self):
        """Retrieve player reviews from the repository."""
        return self.player_repository.get_player_reviews()

    def display_player_reviews(self):
        """Display all player reviews."""
        self.player_repository.display_player_reviews()

    def add_player_review(self, player):
        """Add a new player review."""
        self.player_repository.add_player_review(player)

    def update_player_review(self, player):
        """Update an existing player review."""
        self.player_repository.update_player_review(player)

    def delete_player_review(self, player_name):
        """Delete a player review by name."""
        self.player_repository.delete_player_review(player_name)


class Player:
    def __init__(self, name, goals, assists, appearances, motm):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.appearances = appearances
        self.motm = motm

    def to_dict(self):
        return {
            "Name": self.name,
            "Goals": self.goals,
            "Assists": self.assists,
            "Appearances": self.appearances,
            "MOTM": self.motm
        }

    def __str__(self):
        return f"{self.name},{self.goals},{self.assists},{self.appearances},{self.MOTM}"
