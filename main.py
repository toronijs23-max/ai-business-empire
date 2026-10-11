from dataclasses import dataclass


@dataclass
class Agent:
    name: str
    role: str


AGENTS = [
    Agent("CEO Agent", "Compares findings and recommends decisions"),
    Agent("Market Agent", "Analyzes customers and competitors"),
    Agent("Finance Agent", "Estimates costs, revenue and risks"),
    Agent("Quality Agent", "Checks evidence and assumptions"),
]


def show_team():
    print("=== AI BUSINESS EMPIRE ===")
    print("AI agent team initialized:")
    for agent in AGENTS:
        print(f"- {agent.name}: {agent.role}")


if __name__ == "__main__":
    show_team()
