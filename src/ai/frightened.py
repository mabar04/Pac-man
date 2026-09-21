from src.ai.ghost_ai import GhostAI


class FrightenedAI(GhostAI):
    """Frightened behavior placeholder."""

    def choose_direction(self, ghost, player):
        return "frightened"
