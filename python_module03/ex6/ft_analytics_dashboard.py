game_data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "game_modes": [
        "casual",
        "competitive",
        "ranked",
    ],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}

def list_comprehension() -> None:
    print("=== List Comprehension Examples ===")

    high_scorers: list[str]= [name for name, score in game_data["players"].items()
    if score["total_score"] > 2000]

    score_doubled: list[str] = [info["total_score"] * 2 
    for name, info in game_data["players"].items()]

    active_players: list[str] = [value["player"] for value in game_data["sessions"]]
    active_players: list[str] = list(set(active_players))

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {score_doubled}")
    print(f"Active players: {active_players}")


def dict_comprehension() -> None:
    print("\n=== Dict Comprehension Examples ===")
    scores = {key: value["total_score"] for key, value in game_data["players"].items()}
    categories = ["high", "medium", "low"]
    score_cat = {cat: len([
        name for name , info in game_data["players"].items()
        if(cat == "high" and info["total_score"] > 5000) or
        (cat == "medium" and 2000 < info["total_score"] <= 5000) or
        (cat == "low" and info["total_score"] <= 2000)
        ])
        for cat in categories
    }
    achivements =  {name: info["achievements_count"] for name, info in game_data["players"].items()}

    print(f"Player scores: {scores}")
    print(f"Score categories: {score_cat}")
    print(f"Achievement counts: {achivements}")

def set_comprehension() -> None:
    print("\n=== Set Comprehension Examples ===")
    
    unique_players = {session["player"] for session in game_data["sessions"]}
    unique_achievements = {ach for ach in game_data["achievements"]}
    active_modes = {session["mode"] for session in game_data["sessions"]}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active modes: {active_modes}")


def combined_analysis() -> None:
    print("\n=== Combined Analysis ===")
    
    total_players = len(game_data["players"])
    
    unique_ach_set = {ach for ach in game_data["achievements"]}
    total_unique_ach = len(unique_ach_set)
    
    # 3. Average Score
    all_scores = [info["total_score"] for info in game_data["players"].values()]
    avg_score = sum(all_scores) / total_players

    # 4. Top Performer (The "No-Lambda" Way)
    highest_score = max(all_scores)
    
    top_names = [
        name for name, info in game_data["players"].items() 
        if info["total_score"] == highest_score
    ]
    
    top_name = top_names[0]
    top_info = game_data["players"][top_name]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {top_name} ({highest_score} points, {top_info['achievements_count']} achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    list_comprehension()
    dict_comprehension()
    set_comprehension()
    combined_analysis()