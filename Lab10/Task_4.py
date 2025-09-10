def process_scores(scores):
    print("Average:", sum(scores) / len(scores))
    print("Highest:", max(scores))
    print("Lowest:", min(scores))

print("Scores Analysis")
process_scores([85, 90, 78, 92, 88])
