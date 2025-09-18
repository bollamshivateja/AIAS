def parse_and_normalize_sensor_data(text: str) -> dict[str, list[tuple[str, float]]]:
    from collections import defaultdict
    # Step 1: Parse the text into structured data
    sensor_data = defaultdict(list)  # sensor_id -> list of (timestamp, value)
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue  # skip blank lines
        parts = line.split(',')
        if len(parts) != 3:
            continue  # skip malformed lines
        sensor_id, timestamp, value_str = parts
        try:
            value = float(value_str)
        except ValueError:
            continue  # skip lines with non-numeric values
        sensor_data[sensor_id].append((timestamp, value))
    # Step 2: Compute z-score normalization per sensor
    result = {}
    for sensor_id, entries in sensor_data.items():
        values = [v for _, v in entries]
        n = len(values)
        if n == 0:
            result[sensor_id] = []
            continue
        mean = sum(values) / n
        if n == 1:
            std = 0.0
        else:
            # Use population std (divide by n), as per ML convention for normalization
            variance = sum((v - mean) ** 2 for v in values) / n
            std = variance ** 0.5
        # Edge case: std == 0 (all values identical or only one value)
        if std == 0:
            z_scores = [0.0] * n
        else:
            z_scores = [round((v - mean) / std, 3) for v in values]
        # Pair timestamps with z-scores
        result[sensor_id] = [(entries[i][0], z_scores[i]) for i in range(n)]
    return result

if __name__ == "__main__":
    print("Enter sensor data (CSV lines: sensor_id,timestamp,value). Blank line to finish:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            break
        lines.append(line)
    user_input = "\n".join(lines)
    output = parse_and_normalize_sensor_data(user_input)
    # Print output in alternate lines (key, then each value on its own line)
    for sensor_id, data in output.items():
        print(sensor_id)
        for item in data:
            print(item)