from utils.config import get_api_key
from agents.thinker import ThinkerAgent
from agents.summarizer import SummarizerAgent
from agents.planner import PlannerAgent

def main():
    print("🚀 Welcome to Astrogen AI 🚀")
    api_key = get_api_key()

    thinker = ThinkerAgent(api_key)
    summarizer = SummarizerAgent(api_key)
    planner = PlannerAgent(api_key)

    while True:
        print("\nSelect an option:")
        print("1. Brainstorm a new idea")
        print("2. Summarize a text")
        print("3. Create an action plan from an idea")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            topic = input("Enter a topic: ").strip()
            result = thinker.generate_idea(topic)
            print("\nGenerated Idea:\n", result)
        elif choice == "2":
            text = input("Enter text to summarize: ").strip()
            result = summarizer.summarize(text)
            print("\nSummary:\n", result)
        elif choice == "3":
            idea = input("Enter an idea: ").strip()
            result = planner.plan(idea)
            print("\nAction Plan:\n", result)
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
