import unittest
from player_review_logic import PlayerReviewLogic, Player


class TestPlayerReviewLogic(unittest.TestCase):
    def test_add_player_review(self):
        """Test adding a player review."""
        logic = PlayerReviewLogic()
        player = Player("John Doe", 10, 5, 20, 3)
        logic.add_player_review(player)
        # Extract only the names from reviews for assertion
        reviews = logic.get_player_reviews()
        review_names = [review.split(",")[0].strip() for review in reviews]
        self.assertIn(player.name, review_names)

    def test_update_player_review(self):
        """ Test updating a player review."""
        logic = PlayerReviewLogic()
        player = Player("Jane Doe", 15, 7, 25, 4)
        logic.add_player_review(player)
        player.goals = 20
        logic.update_player_review(player)

    def test_delete_player_review(self):
        """Test deleting a player review."""
        logic = PlayerReviewLogic()
        player = Player("Mark Smith", 5, 2, 10, 1)
        logic.add_player_review(player)
        logic.delete_player_review(player.name)
        # Check if the player review was deleted correctly
        reviews = logic.get_player_reviews()
        self.assertNotIn(player.name, [i for i in reviews])

    def test_display_player_reviews(self):
        """Test displaying player reviews."""
        logic = PlayerReviewLogic()
        player1 = Player("Alice Johnson", 8, 3, 15, 2)
        player2 = Player("Bob Brown", 12, 4, 18, 5)
        logic.add_player_review(player1)
        logic.add_player_review(player2)

        # Capture the output of the display function
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        logic.display_player_reviews()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if the output contains both players' names
        output = captured_output.getvalue()
        self.assertIn(player1.name, output)
        self.assertIn(player2.name, output)


if __name__ == '__main__':
    unittest.main()
