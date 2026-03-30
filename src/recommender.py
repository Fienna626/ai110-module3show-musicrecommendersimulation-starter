import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score_song(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        score = 0.0
        reasons: List[str] = []

        if song.genre == user.favorite_genre:
            score += 2.0
            reasons.append("genre match (+2.0)")

        if song.mood == user.favorite_mood:
            score += 1.0
            reasons.append("mood match (+1.0)")

        energy_diff = abs(song.energy - user.target_energy)
        energy_score = max(0.0, 1.0 - energy_diff)
        score += energy_score
        reasons.append(f"energy closeness (+{energy_score:.2f})")

        if user.likes_acoustic and song.acousticness >= 0.7:
            score += 0.5
            reasons.append("acoustic preference (+0.5)")

        return score, reasons

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = []
        for song in self.songs:
            score, _ = self._score_song(user, song)
            scored.append((song, score))

        scored.sort(key=lambda item: item[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = self._score_song(user, song)
        return "; ".join(reasons)


def _get_song_value(song: object, key: str, default=None):
    if isinstance(song, dict):
        return song.get(key, default)
    return getattr(song, key, default)


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a single song against user preferences and return reasons."""
    score = 0.0
    reasons: List[str] = []

    if _get_song_value(song, "genre") == user_prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if _get_song_value(song, "mood") == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_diff = abs(_get_song_value(song, "energy", 0.0) - user_prefs.get("energy", 0.0))
    energy_score = max(0.0, 1.0 - energy_diff)
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    if "target_valence" in user_prefs:
        valence_diff = abs(_get_song_value(song, "valence", 0.5) - user_prefs["target_valence"])
        valence_score = max(0.0, 1.0 - valence_diff)
        score += valence_score
        reasons.append(f"valence closeness (+{valence_score:.2f})")

    if user_prefs.get("likes_acoustic") and _get_song_value(song, "acousticness", 0.0) >= 0.7:
        score += 0.5
        reasons.append("acoustic preference (+0.5)")

    return score, reasons


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    print(f"Loading songs from {csv_path}...")
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs: List[Tuple[Dict, float, List[str]]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, reasons))

    scored_songs.sort(key=lambda item: item[1], reverse=True)

    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in scored_songs[:k]
    ]
