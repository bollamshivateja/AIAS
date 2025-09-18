from datetime import datetime
from typing import List, Dict, Tuple

def detect_overlapping_fields_brute_force(schedules: List[Dict]) -> List[Tuple[str, str]]:
    overlaps = []
    n = len(schedules)
    for i in range(n):
        for j in range(i + 1, n):
            f1, f2 = schedules[i], schedules[j]
            s1, e1 = datetime.fromisoformat(f1['start_time']), datetime.fromisoformat(f1['end_time'])
            s2, e2 = datetime.fromisoformat(f2['start_time']), datetime.fromisoformat(f2['end_time'])
            if s1 < e2 and s2 < e1:
                overlaps.append(tuple(sorted([f1['field_id'], f2['field_id']])))
    return overlaps

def detect_overlapping_fields_sorted(schedules: List[Dict]) -> List[Tuple[str, str]]:
    if len(schedules) < 2: return []
    sorted_schedules = sorted(schedules, key=lambda x: x['start_time'])
    overlaps = []
    for i in range(len(sorted_schedules)):
        for j in range(i + 1, len(sorted_schedules)):
            f1, f2 = sorted_schedules[i], sorted_schedules[j]
            s1, e1 = datetime.fromisoformat(f1['start_time']), datetime.fromisoformat(f1['end_time'])
            s2, e2 = datetime.fromisoformat(f2['start_time']), datetime.fromisoformat(f2['end_time'])
            if s2 >= e1: break
            if s1 < e2 and s2 < e1:
                overlaps.append(tuple(sorted([f1['field_id'], f2['field_id']])))
    return overlaps
def detect_overlapping_fields_sweep_line(schedules: List[Dict]) -> List[Tuple[str, str]]:
    if len(schedules) < 2: return []
    events = []
    for s in schedules:
        events.append((datetime.fromisoformat(s['start_time']), 0, s['field_id']))
        events.append((datetime.fromisoformat(s['end_time']), 1, s['field_id']))
    events.sort(key=lambda x: (x[0], x[1]))
    overlaps, active = [], set()
    for _, t, fid in events:
        if t == 0:
            for af in active:
                overlaps.append(tuple(sorted([fid, af])))
            active.add(fid)
        else:
            active.remove(fid)
    return overlaps

def detect_overlapping_fields(schedules: List[Dict], strategy: str = "auto") -> List[Tuple[str, str]]:
    if not schedules or len(schedules) < 2: return []
    if strategy == "auto":
        n = len(schedules)
        strategy = "brute_force" if n <= 50 else "sorted" if n <= 500 else "sweep_line"
    if strategy == "brute_force":
        return detect_overlapping_fields_brute_force(schedules)
    elif strategy == "sorted":
        return detect_overlapping_fields_sorted(schedules)
    elif strategy == "sweep_line":
        return detect_overlapping_fields_sweep_line(schedules)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

def get_user_input():
    schedules = []
    print("=== Field Watering Schedule Overlap Detector ===")
    print("Enter 3 field watering schedules (press Enter with empty field_id to finish)")
    print("Time format: YYYY-MM-DDTHH:MM:SS (e.g., 2024-01-01T08:00:00)\n")
    while len(schedules) < 3:
        print(f"Field {len(schedules) + 1}:")
        field_id = input("  Field ID: ").strip()
        if not field_id: break
        while True:
            start_time = input("  Start time (YYYY-MM-DDTHH:MM:SS): ").strip()
            try: datetime.fromisoformat(start_time); break
            except ValueError: print("  Invalid time format. Please use YYYY-MM-DDTHH:MM:SS")
        while True:
            end_time = input("  End time (YYYY-MM-DDTHH:MM:SS): ").strip()
            try:
                datetime.fromisoformat(end_time)
                if end_time > start_time: break
                else: print("  End time must be after start time.")
            except ValueError: print("  Invalid time format. Please use YYYY-MM-DDTHH:MM:SS")
        schedules.append({"field_id": field_id, "start_time": start_time, "end_time": end_time})
        print()
    return schedules

def display_results(schedules, results):
    print("\n" + "="*60)
    print("INPUT SCHEDULES:")
    print("="*60)
    for i, s in enumerate(schedules, 1):
        print(f"{i:2d}. Field: {s['field_id']}\n    Start: {s['start_time']}\n    End:   {s['end_time']}\n")
    print("="*60)
    print("OVERLAP DETECTION RESULTS:")
    print("="*60)
    if not results:
        print("✅ No overlapping watering times found!")
    else:
        print(f"⚠  Showing up to 3 overlapping pair(s):")
        for i, (f1, f2) in enumerate(results[:3], 1):
            print(f"   {i}. {f1} ↔ {f2}")

if __name__ == "__main__":
    try:
        schedules = get_user_input()
        if not schedules:
            print("No schedules entered. Exiting.")
        elif len(schedules) < 2:
            print("Need at least 2 fields to check for overlaps.")
        else:
            print("\nAnalyzing overlaps...")
            results = detect_overlapping_fields(schedules, "auto")
            display_results(schedules, results)
            print("\n" + "="*60)
            print("STRATEGY COMPARISON:")
            print("="*60)
            for strategy in ["brute_force", "sorted", "sweep_line"]:
                result = detect_overlapping_fields(schedules, strategy)
                print(f"{strategy:12}: {len(result)} overlap(s) - {result[:3]}")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")
        print("Please check your input format and try again.")