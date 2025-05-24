import random

def generate_flips(num_flips):
    """Generate a list of random 'heads' (H) and 'tails' (T)."""
    return ['H' if random.randint(0, 1) == 0 else 'T' for _ in range(num_flips)]

def check_streak(flips, streak_length=6):
    """Check if a streak of 'H' or 'T' appears in the list."""
    count = 0
    for i in range(len(flips) - streak_length + 1):
        if len(set(flips[i:i + streak_length])) == 1:  # Checks if all are 'H' or 'T'
            count += 1
    return count > 0
num_experiments = 10000
num_flips_per_experiment = 100
streak_count = sum(check_streak(generate_flips(num_flips_per_experiment)) for _ in range(num_experiments))

percentage = (streak_count / num_experiments) * 100

print(f"Out of {num_experiments} experiments, {streak_count} contained a streak of six heads or tails.")
print(f"Percentage of experiments with a streak: {percentage:.2f}%")