#!/usr/bin/env python3
"""
Children's Gift Recommendation System
A rule-based expert system using CLIPS for inference
"""

from src.gui import main as gui_main


def main():
    """Main entry point - launches GUI directly"""
    try:
        print("Starting Gift Recommender System...")
        print("Loading knowledge base and initializing GUI...\n")
        gui_main()
    except KeyboardInterrupt:
        print("\n\nGoodbye! Thanks for using the Gift Recommender!\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please check that all knowledge base files are in the correct location.")
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
