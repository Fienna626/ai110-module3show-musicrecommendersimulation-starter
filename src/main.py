"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from typing import Dict, Optional
from recommender import load_songs, recommend_songs


def print_recommendations(title: str, user_prefs: Dict, songs, k: int = 5, weights: Optional[Dict[str, float]] = None) -> None:
    print(f"\n=== {title} ===")
    print(f"User prefs: {user_prefs}")
    if weights:
        print(f"Weights: {weights}")

    recommendations = recommend_songs(user_prefs, songs, k=k, weights=weights)
    for song, score, explanation in recommendations:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        (
            "High-Energy Pop",
            {"genre": "pop", "mood": "happy", "energy": 0.9},
        ),
        (
            "Chill Lofi",
            {"genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True},
        ),
        (
            "Deep Intense Rock",
            {"genre": "rock", "mood": "intense", "energy": 0.95},
        ),
        (
            "Conflicting High-Energy Sad",
            {"genre": "jazz", "mood": "moody", "energy": 0.9},
        ),
    ]

    for title, prefs in profiles:
        print_recommendations(title, prefs, songs, k=5)

    energy_weight_experiment = {"genre": 1.0, "mood": 1.0, "energy": 2.0, "acoustic": 0.5}
    print_recommendations(
        "Energy-Weighted Experiment for Chill Lofi",
        profiles[1][1],
        songs,
        k=5,
        weights=energy_weight_experiment,
    )


if __name__ == "__main__":
    main()
