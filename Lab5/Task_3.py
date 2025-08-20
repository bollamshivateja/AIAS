import random

# Example product catalog with brands and categories
products = [
    {"name": "FreshBrew Coffee", "brand": "BrewCo", "category": "Coffee"},
    {"name": "Morning Roast", "brand": "BeanWorks", "category": "Coffee"},
    {"name": "Green Tea Classic", "brand": "TeaTime", "category": "Tea"},
    {"name": "Herbal Calm", "brand": "Leafy", "category": "Tea"},
    {"name": "Crunchy Oats Cereal", "brand": "GrainGood", "category": "Cereal"},
    {"name": "Honey Flakes", "brand": "SunnyStart", "category": "Cereal"},
    {"name": "Almond Milk", "brand": "NutriChoice", "category": "Milk"},
    {"name": "Soy Delight", "brand": "PlantPure", "category": "Milk"},
]

# User purchase history and feedback memory
purchase_history = []
feedback_memory = {}

def get_recommendations(purchase_history, feedback_memory, num_recs=2):
    # Find categories the user bought before
    bought_categories = set([p["category"] for p in purchase_history])
    bought_brands = set([p["brand"] for p in purchase_history])
    recs = []
    explanations = []

    # For each category, recommend a product from a different brand
    for category in bought_categories:
        # Exclude brands the user bought most recently in this category
        recent_brand = None
        for p in reversed(purchase_history):
            if p["category"] == category:
                recent_brand = p["brand"]
                break
        # Filter products in the same category, but not the recent brand
        candidates = [prod for prod in products if prod["category"] == category and prod["brand"] != recent_brand]
        # Remove products the user disliked
        candidates = [prod for prod in candidates if feedback_memory.get(prod["name"], 0) >= 0]
        if candidates:
            rec = random.choice(candidates)
            recs.append(rec)
            explanations.append(
                f"We recommend '{rec['name']}' from {rec['brand']} because you like {category}, and this is a different brand from your last purchase."
            )
        # If no candidates, skip

    # Recommend something new from a category the user hasn't tried
    new_categories = set([p["category"] for p in products]) - bought_categories
    for category in new_categories:
        candidates = [prod for prod in products if prod["category"] == category]
        # Remove products the user disliked
        candidates = [prod for prod in candidates if feedback_memory.get(prod["name"], 0) >= 0]
        if candidates:
            rec = random.choice(candidates)
            recs.append(rec)
            explanations.append(
                f"Try '{rec['name']}' from {rec['brand']} - you haven't tried products from the {category} category yet!"
            )
        if len(recs) >= num_recs:
            break

    # If not enough recommendations, fill with random fair picks
    while len(recs) < num_recs:
        candidates = [prod for prod in products if prod not in recs and feedback_memory.get(prod["name"], 0) >= 0]
        if not candidates:
            break
        rec = random.choice(candidates)
        recs.append(rec)
        explanations.append(
            f"Here's another suggestion: '{rec['name']}' from {rec['brand']}."
        )
    return recs, explanations

def get_product_by_name(name):
    for prod in products:
        if prod["name"].lower() == name.lower():
            return prod
    return None

def main():
    print("Welcome to the Fair Product Recommender!")
    while True:
        print("\nYour purchase history:")
        if purchase_history:
            for p in purchase_history:
                print(f"- {p['name']} ({p['brand']}, {p['category']})")
        else:
            print("No purchases yet.")

        # Recommend products
        recs, explanations = get_recommendations(purchase_history, feedback_memory)
        print("\nRecommended for you:")
        for i, (rec, expl) in enumerate(zip(recs, explanations)):
            print(f"{i+1}. {rec['name']} ({rec['brand']}, {rec['category']})")
            print(f"   Reason: {expl}")

        # User feedback
        for i, rec in enumerate(recs):
            while True:
                feedback = input(f"Do you like the suggestion '{rec['name']}'? (like/dislike/skip): ").strip().lower()
                if feedback in ("like", "dislike", "skip"):
                    break
                print("Please enter 'like', 'dislike', or 'skip'.")
            if feedback == "like":
                # Positive feedback: increase score
                feedback_memory[rec["name"]] = feedback_memory.get(rec["name"], 0) + 1
            elif feedback == "dislike":
                # Negative feedback: decrease score
                feedback_memory[rec["name"]] = feedback_memory.get(rec["name"], 0) - 1
            # skip does nothing

        # Simulate a purchase
        buy = input("\nWould you like to buy something? Enter product name or 'no': ").strip()
        if buy.lower() == "no":
            print("Thank you for using the recommender. Goodbye!")
            break
        prod = get_product_by_name(buy)
        if prod:
            purchase_history.append(prod)
            print(f"You bought: {prod['name']} ({prod['brand']}, {prod['category']})")
        else:
            print("Product not found. Please try again.")

if __name__ == "__main__":
    main()
