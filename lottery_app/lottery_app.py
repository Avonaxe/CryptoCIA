from blockchain_simulation import Blockchain

class LotteryApp:
    def __init__(self):
        self.blockchain = Blockchain()
        self.players = []

    def enter_lottery(self, player_name):
        self.players.append(player_name)
        self.blockchain.add_block(f"{player_name} entered the lottery")
        return f"{player_name} has been added to the lottery."

    def pick_winner(self):
        if not self.players:
            return None, "No players have entered the lottery."

        import random
        winner = random.choice(self.players)
        self.blockchain.add_block(f"{winner} won the lottery")
        return winner, f"The winner is: {winner}"

    def get_blockchain(self):
        return self.blockchain.chain
