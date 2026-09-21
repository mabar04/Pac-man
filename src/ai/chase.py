from src.ai.ghost_ai import GhostAI


class ChaseAI(GhostAI):
    """Chase behavior placeholder."""

    def choose_direction(self, ghost, player):
        return "chase"
