"""Домашнее задание №1: аналитика каталога стримингового сервиса."""

import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# Task 1
def average_rating(movies: list) -> float:
    total_rating = sum(movie["rating"] for movie in movies)
    average_rating = total_rating / len(movies)
    return round(average_rating, 1)


def catalog_age_stats(movies, current_year=2026) -> tuple[int, int, int]:
    sorted_movies = sorted(movies, key=lambda x: x["year"])
    average_age = sum(current_year - movie["year"] for movie in movies) / len(movies)
    oldest_age = current_year - sorted_movies[0]["year"]
    newest_age = current_year - sorted_movies[-1]["year"]
    return oldest_age, newest_age, math.ceil(average_age)


def duration_in_hours(minutes) -> str:
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


# Task 2
def rating_tier(rating) -> str:
    if rating >= 9.0:
        return "шедевр"
    elif rating >= 7.0:
        return "хорошо"
    else:
        return "средне" if rating >= 5.0 else "слабо"


def decade_label(year) -> str | None:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _ if year < 2015:
            return "старые"
    return None


# Task 3
def print_no_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def first_90_rating_movie(movies):
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(f"{movies[index]['title']}")
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120) -> int:
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Task 4
def normalize_title(title) -> str:
    normalized_words = []
    for word in title.split():
        normalized_words.append(word[0].upper() + word[1:])
    return " ".join(normalized_words)


def make_slug(title) -> str:
    title = title.lower()
    title = title.replace(" ", "-")
    return title


def format_report_line(movie) -> str:
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


# Task 5
def titles_sorted_by_rating(movies) -> list[str]:
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3) -> list[tuple[str, float]]:
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


# Task 6
def count_by_genre(movies) -> dict[str, int]:
    genre_count = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count


def actor_filmography(movies) -> dict[str, list[str]]:
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def get_movies_above_average_rating(movies) -> dict[str, float]:
    mean_rating = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > mean_rating
    }


# Task 7
def all_genres(movies) -> set[str]:
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2) -> set[str]:
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b) -> set[str]:
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b


# Task 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def demonstrate_iter_high_rated(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

    summary = sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)
    print(f"Суммарная продолжительность: {summary} минут")


# Task 9
def build_report(movies):
    """
    Example of a report:
    ОТЧЕТ ПО КАТАЛОГУ
    Средний рейтинг: 7.2
    Средний возраст фильмов: 8 лет

    Топ-3 фильма:
    "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi
    "Midnight In Oslo" (2020) — 8.9/10, 2ч 4м, жанры: mystery, thriller
    "The Dune Chronicles" (2021) — 8.6/10, 2ч 35м, жанры: drama, sci-fi

    Фильмов по жанрам:
    drama — 5
    comedy — 3
    sci-fi — 3
    thriller — 3
    action — 2
    mystery — 1

    Все жанры каталога: action, comedy, drama, mystery, sci-fi, thriller
    """
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    newest_age, oldest_age, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")

    print("\nТоп-3 фильма:")
    top_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)[:3]
    print("\n".join(f"  {format_report_line(movie)}" for movie in top_movies))

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre, count in sorted(
        genre_counts.items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"  {genre} — {count}")

    print(f"\nВсе жанры каталога: {', '.join(sorted(all_genres(movies)))}")


def main() -> None:
    build_report(movies)


if __name__ == "__main__":
    main()
