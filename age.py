import random

# List of common Somali first, middle, and last names (mixed genders)
somali_first_names = [
    "Aamina", "Abdi", "Ahmed", "Ali", "Amal", "Ayan", "Bilan", "Cabdullahi",
    "Dahabo", "Elmi", "Faduma", "Farah", "Guled", "Halima", "Idil", "Jama",
    "Kaltun", "Leyla", "Mohamed", "Nadifa", "Osman", "Rahma", "Saciid", "Ubax",
    "Yasmin", "Zahra"
]

somali_middle_names = [
    "Hussein", "Ibrahim", "Ismail", "Jamal", "Jibril", "Khadra", "Liban",
    "Mahad", "Nasir", "Qasim", "Rayan", "Sahra", "Salah", "Samira", "Tahir",
    "Yasin", "Yusuf", "Zaki", "Abdul", "Aden", "Faisal", "Harun", "Isse", "Muna"
]

somali_last_names = [
    "Ali", "Bare", "Dalmar", "Farah", "Gedi", "Hassan", "Ismail", "Jama",
    "Khalif", "Mumin", "Nor", "Omar", "Qasim", "Roble", "Sharif", "Tahir",
    "Warsame", "Yusuf", "Abukar", "Adan", "Barre", "Dahir", "Elmi", "Guleid"
]

# Generate 1000 Somali names with random ages below 50
random_somali_names_with_ages_under_50 = [
    (random.choice(somali_first_names), 
     random.choice(somali_middle_names), 
     random.choice(somali_last_names), 
     random.randint(1, 50)) for _ in range(1000)
]

# Print out the names and ages
for first, middle, last, age in random_somali_names_with_ages_under_50:
    print(f"{first} {middle} {last}, {age} years old")
