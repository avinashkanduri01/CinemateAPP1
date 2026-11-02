import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CineMate - Movie Discovery")
root.geometry("1100x700")
root.configure(bg="#141414")

BG = "#141414"
SIDEBAR = "#202020"
CARD = "#292929"
RED = "#e50914"
WHITE = "white"
GREY = "#aaaaaa"

# Movie collection: Name, Industry, Genre, Rating
movies = [
    # Hollywood
    ("Avengers: Endgame", "Hollywood", "Action", "8.4"),
    ("Avengers: Infinity War", "Hollywood", "Action", "8.4"),
    ("The Dark Knight", "Hollywood", "Crime", "9.0"),
    ("Inception", "Hollywood", "Sci-Fi", "8.8"),
    ("Interstellar", "Hollywood", "Sci-Fi", "8.7"),
    ("Titanic", "Hollywood", "Romance", "7.9"),
    ("Avatar", "Hollywood", "Fantasy", "7.9"),
    ("Avatar: The Way of Water", "Hollywood", "Fantasy", "7.5"),
    ("Spider-Man: No Way Home", "Hollywood", "Action", "8.2"),
    ("Iron Man", "Hollywood", "Action", "7.9"),
    ("Doctor Strange", "Hollywood", "Fantasy", "7.5"),
    ("The Batman", "Hollywood", "Crime", "7.8"),
    ("Joker", "Hollywood", "Crime", "8.3"),
    ("Oppenheimer", "Hollywood", "Drama", "8.3"),
    ("The Prestige", "Hollywood", "Thriller", "8.5"),
    ("Jurassic Park", "Hollywood", "Adventure", "8.2"),
    ("Gladiator", "Hollywood", "Action", "8.5"),
    ("The Conjuring", "Hollywood", "Horror", "7.5"),
    ("John Wick", "Hollywood", "Action", "7.4"),
    ("The Matrix", "Hollywood", "Sci-Fi", "8.7"),

    # Tollywood
    ("RRR", "Tollywood", "Action", "8.0"),
    ("Baahubali", "Tollywood", "Fantasy", "8.0"),
    ("Baahubali 2", "Tollywood", "Fantasy", "8.2"),
    ("Salaar", "Tollywood", "Action", "6.5"),
    ("Arjun Reddy", "Tollywood", "Romance", "7.8"),
    ("Pushpa", "Tollywood", "Action", "7.6"),
    ("Eega", "Tollywood", "Fantasy", "7.7"),
    ("Jersey", "Tollywood", "Drama", "8.5"),
    ("Ala Vaikunthapurramuloo", "Tollywood", "Drama", "7.3"),
    ("Magadheera", "Tollywood", "Fantasy", "7.7")
]

watchlist = []

# Sidebar
sidebar = tk.Frame(root, bg=SIDEBAR, width=220)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# Main content
content = tk.Frame(root, bg=BG)
content.pack(side="left", fill="both", expand=True)


def show_movies(movie_list, parent):

    if not movie_list:
        tk.Label(
            parent, text="No movies found!",
            fg=RED, bg=BG, font=("Arial", 14)
        ).pack(pady=20)
        return

    for movie in movie_list:

        card = tk.Frame(
            parent, bg=CARD, padx=15, pady=12
        )
        card.pack(fill="x", padx=30, pady=5)

        tk.Label(
            card, text=movie[0],
            font=("Arial", 13, "bold"),
            fg=WHITE, bg=CARD
        ).pack(side="left")

        tk.Label(
            card,
            text=f"{movie[1]} | {movie[2]} | Rating: {movie[3]}",
            font=("Arial", 10),
            fg=GREY, bg=CARD
        ).pack(side="left", padx=15)

        def add_favourite(m=movie):
            if m not in watchlist:
                watchlist.append(m)
                messagebox.showinfo(
                    "CineMate", m[0] + " added to Watchlist!"
                )
            else:
                messagebox.showinfo(
                    "CineMate", "Already in Watchlist!"
                )

        tk.Button(
            card, text="Add +",
            command=add_favourite,
            bg=RED, fg=WHITE,
            relief="flat"
        ).pack(side="right")


def show_page(page):

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content, text=page,
        font=("Arial", 25, "bold"),
        fg=WHITE, bg=BG
    ).pack(pady=20)

    if page == "Home":
        tk.Label(
            content,
            text="Discover Your Next Favourite Movie",
            fg=GREY, bg=BG
        ).pack(pady=10)

        show_movies(movies, content)

    elif page == "Hollywood" or page == "Tollywood":
        results = [
            m for m in movies if m[1] == page
        ]
        show_movies(results, content)

    elif page == "Search Movies":

        search_box = tk.Entry(
            content, font=("Arial", 14), width=30
        )
        search_box.pack(pady=15)

        result_area = tk.Frame(content, bg=BG)
        result_area.pack(fill="both", expand=True)

        def search_movies():
            for widget in result_area.winfo_children():
                widget.destroy()

            keyword = search_box.get().strip().lower()

            results = [
                m for m in movies
                if keyword in m[0].lower()
            ]
            show_movies(results, result_area)

        tk.Button(
            content, text="Search",
            command=search_movies,
            bg=RED, fg=WHITE
        ).pack(pady=10)

    elif page == "Genres":

        genres = sorted(set(m[2] for m in movies))
        selected = tk.StringVar(value=genres[0])

        tk.OptionMenu(
            content, selected, *genres
        ).pack(pady=15)

        result_area = tk.Frame(content, bg=BG)
        result_area.pack(fill="both", expand=True)

        def filter_genre():
            for widget in result_area.winfo_children():
                widget.destroy()

            results = [
                m for m in movies if m[2] == selected.get()
            ]
            show_movies(results, result_area)

        tk.Button(
            content, text="Show Movies",
            command=filter_genre,
            bg=RED, fg=WHITE
        ).pack(pady=10)

    elif page == "Moods":

        moods = {
            "Excited": ["Action", "Adventure"],
            "Romantic": ["Romance"],
            "Curious": ["Sci-Fi", "Thriller"],
            "Adventurous": ["Fantasy"],
            "Scared": ["Horror"]
        }

        selected = tk.StringVar(value="Excited")

        tk.OptionMenu(
            content, selected, *moods.keys()
        ).pack(pady=15)

        result_area = tk.Frame(content, bg=BG)
        result_area.pack(fill="both", expand=True)

        def filter_mood():
            for widget in result_area.winfo_children():
                widget.destroy()

            genres = moods[selected.get()]
            results = [
                m for m in movies if m[2] in genres
            ]
            show_movies(results, result_area)

        tk.Button(
            content, text="Recommend Movies",
            command=filter_mood,
            bg=RED, fg=WHITE
        ).pack(pady=10)

    elif page == "My Watchlist":

        result_area = tk.Frame(content, bg=BG)
        result_area.pack(fill="both", expand=True)

        if not watchlist:
            tk.Label(
                result_area,
                text="Your Watchlist is empty!",
                fg=GREY, bg=BG
            ).pack(pady=30)

        else:
            for movie in watchlist:

                card = tk.Frame(
                    result_area, bg=CARD,
                    padx=15, pady=10
                )
                card.pack(fill="x", padx=30, pady=5)

                tk.Label(
                    card, text=movie[0],
                    fg=WHITE, bg=CARD
                ).pack(side="left")

                def remove_movie(m=movie):
                    watchlist.remove(m)
                    show_page("My Watchlist")

                tk.Button(
                    card, text="Remove",
                    command=remove_movie,
                    bg=RED, fg=WHITE
                ).pack(side="right")


# Logo
tk.Label(
    sidebar, text="CINEMATE",
    font=("Arial", 23, "bold"),
    fg=RED, bg=SIDEBAR
).pack(pady=35)

# Navigation
pages = [
    "Home",
    "Hollywood",
    "Tollywood",
    "Search Movies",
    "Genres",
    "Moods",
    "My Watchlist"
]

for page in pages:
    tk.Button(
        sidebar, text=page,
        font=("Arial", 12),
        fg=WHITE, bg=SIDEBAR,
        activebackground=RED,
        activeforeground=WHITE,
        relief="flat", anchor="w",
        padx=25, pady=13,
        command=lambda p=page: show_page(p)
    ).pack(fill="x", padx=10, pady=4)

show_page("Home")
root.mainloop()