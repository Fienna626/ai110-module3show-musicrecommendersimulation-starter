# 🎵 Music Recommender Simulation

## Phase 1

Step 2: Identify Key Features

*Examine the data/songs.csv file to see the available attributes for your simulator, such as genre, mood, energy, and tempo_bpm.*

the available attributes are:

genre
mood
energy
tempo_bpm
valence
danceability
acousticness

*Use the #file:songs.csv context to ask Copilot to analyze the available data and suggest which features would be most effective for a simple content-based recommender. Evaluate if the suggested features (e.g., energy, valence) align with your personal experience of how a musical "vibe" is defined.*

genre

Good for coarse matching of style.
Often the strongest signal for whether a song “fits” a user’s taste.
mood

Useful for matching the user’s current vibe (happy, chill, intense, focused, etc.).
Works well with genre to capture emotional intent.
energy

Numeric measure of intensity; helps distinguish calm vs. active tracks.
Aligns well with “vibe” because it affects how a song feels physically.
valence

Numeric measure of positivity/happiness.
Good for differentiating bright vs. moody tracks.
tempo_bpm

Supports matching on pace or rhythm.
Especially useful if the user wants fast workout music vs. slow background music.
danceability and acousticness

Nice extra refinements for subtle vibe differences.
Could be lower priority features in a simple model.


*Determine your "Algorithm Recipe"—the set of rules your system will use to score songs.*
binary match for categorical features (genre, mood)
distance-based score for numeric features (energy, valence, tempo_bpm)

*Formulate a prompt to help you design a math-based "Scoring Rule" for your recommender. Ask Copilot how to calculate a score for a numerical feature (like energy) that rewards songs that are closer to the user's preference, rather than just having higher or lower values.*
 I want a math-based scoring rule for a song recommender. For numeric features like energy, how do I calculate a score that rewards songs closer to the user's preferred value instead of just favoring higher or lower numbers? Please show a formula using absolute difference and normalization. Also explain how to combine categorical matches like genre and mood with numeric closeness, and how to choose weights so genre is worth more than mood.

*Ask Copilot to explain why we need both a "Scoring Rule" (for one song) and a "Ranking Rule" (for a list of songs) to build a recommendation system.* 
Scoring Rule:

Computes a score for one song relative to user preferences.
Converts categorical and numeric feature matches into a single value.

Ranking Rule:

Takes all songs and orders them by score.
Decides which songs should be recommended first.

## Phase 2

*Manually compute one song score*

Assume user profile:

favorite_genre = "lofi"
favorite_mood = "chill"
target_energy = 0.38
Song: Library Rain (lofi, chill, energy 0.35)

genre_match = 1
mood_match = 1
energy_similarity = 1.0 - |0.35 - 0.38| = 0.97
Total score:

2.0 * 1 + 1.0 * 1 + 0.97 = 3.97

*Predict which song should rank first*
Library Rain
rank first among the starter songs for that profile because it matches both genre and mood and has energy very close to the target.

*Identify weight imbalance risks*
If genre weight is too high:

the system may recommend wrong-vibe songs just because they share genre.

If mood weight is too high:

you may get songs with the right emotional feel but a very different style

If numeric weights are too low:

the recommender cannot distinguish between multiple same-genre/mood songs

If numeric weights are too high:

the system may favor songs with the right energy but wrong genre/mood

## Phase 3
[x]Implement load_songs() 
[x]Trace score_song()
[x]Verify numeric conversions
[x]Confirm sorting correctness
[x]Implement recommend_songs()

## Phase 4
[x]Run at least two user profiles
[x]Explain why a specific song ranked first
[x]Run a small data experiment
[x]Identify one bias or limitation
[x]Interpret surprising output
