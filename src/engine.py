import clips
import os
import sys


class GiftRecommender:
    def __init__(self):
        """Initialize the gift recommendation engine"""
        self.env = clips.Environment()
        self._load_knowledge_base()

    def _get_kb_path(self):
        """Get the correct knowledge base path"""
        if getattr(sys, "frozen", False):
            # Running as compiled executable
            base_path = sys._MEIPASS  # type: ignore
        else:
            # Running as script
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        return os.path.join(base_path, "knowledge_base")

    def _load_knowledge_base(self):
        """Load all CLIPS files"""
        kb_path = self._get_kb_path()

        files_to_load = ["templates.clp", "mappings.clp", "gifts.clp", "rules.clp"]

        for file in files_to_load:
            file_path = os.path.join(kb_path, file)
            if os.path.exists(file_path):
                self.env.load(file_path)
                print(f"Loaded: {file}")
            else:
                error_msg = f"File not found: {file_path}"
                print(error_msg)
                raise FileNotFoundError(error_msg)

        self.env.reset()
        print("Knowledge base loaded and ready")

    def get_available_interests(self):
        """Return list of predefined interests from mappings"""
        interests = set()
        for fact in self.env.facts():
            if fact.template.name == "interest-mapping":
                interests.add(fact["interest"])
        return sorted(list(interests))

    def get_available_gift_types(self):
        """Return available gift types"""
        return ["physical", "experience", "activity", "any"]

    def recommend(
        self, age, interests, budget, gender="any", gift_type="any", sort_by_score=True
    ):
        """
        Get gift recommendations based on criteria

        Parameters:
        - age: int - child's age
        - interests: list of strings - child's interests
        - budget: float - maximum price
        - gender: string - 'male', 'female', or 'any'
        - gift_type: string - 'physical', 'experience', 'activity', or 'any'
        - sort_by_score: bool - sort results by score (highest first)
        """
        # Clear previous results
        self._clear_dynamic_facts()

        # Format interests for CLIPS
        interests_str = " ".join(f'"{interest}"' for interest in interests)

        # Create query fact
        query_str = (
            f"(user-query (age {age}) "
            f"(budget {budget:.2f}) "
            f"(gender {gender}) "
            f"(gift_type {gift_type}) "
            f"(interests {interests_str}))"
        )

        print(f"\nSearching with: {query_str}")

        # Assert the query
        self.env.assert_string(query_str)

        # Run inference
        self.env.run()

        # Collect and sort results
        recommendations = []
        for fact in self.env.facts():
            if fact.template.name == "matching-gift":
                recommendations.append(
                    {
                        "name": fact["name"],
                        "type": str(fact["type"]),
                        "category": fact["category"],
                        "price": float(fact["price"]),
                        "score": int(fact["score"]),
                    }
                )

        # Sort by score (highest first) if requested
        if sort_by_score:
            recommendations.sort(key=lambda x: x["score"], reverse=True)

        return recommendations

    def _clear_dynamic_facts(self):
        """Remove all run-time asserted facts"""
        facts_to_retract = []

        for fact in self.env.facts():
            if fact.template.name in [
                "user-query",
                "matching-gift",
                "matching-category",
                "category-match-count",
            ]:
                facts_to_retract.append(fact)

        for fact in facts_to_retract:
            fact.retract()

    def get_all_gifts(self):
        """Return all gifts in the database"""
        gifts = []
        for fact in self.env.facts():
            if fact.template.name == "gift":
                gifts.append(
                    {
                        "name": fact["name"],
                        "type": str(fact["type"]),
                        "category": fact["category"],
                        "min_age": fact["min_age"],
                        "max_age": fact["max_age"],
                        "price": float(fact["price"]),
                        "gender": str(fact["gender"]),
                    }
                )
        return gifts

    def get_recommendation_stats(self, recommendations):
        """Get statistics about recommendations"""
        if not recommendations:
            return None

        scores = [r["score"] for r in recommendations]
        prices = [r["price"] for r in recommendations]

        return {
            "count": len(recommendations),
            "avg_score": sum(scores) / len(scores),
            "max_score": max(scores),
            "min_score": min(scores),
            "avg_price": sum(prices) / len(prices),
            "min_price": min(prices),
            "max_price": max(prices),
        }
