attendees = set(
    [
        "Alec Zamora",
        "Andrew Nere",
        "Ashley Payne",
        "Ashwin Sundar",
        "Bill Frasure",
        "Bradley Sutton",
        "Bruce Eckel",
        "Chris Marks",
        "Chris Phelps",
        "D. J. Hagberg",
        "Dave Bartlett",
        "David Xenakis",
        "Earl Wagner",
        "Gordon Weakliem",
        "James Ward",
        "Jeremy Cerise",
        "Jimmy Utley",
        "Joe Schrag",
        "Joey Gibson",
        "Justin Poehnelt",
        "Justin Ryan",
        "Mallory Weber",
        "Patrick Force",
        "Schuyler Metcalf",
        "Stephanie Reeves",
        "Thomas R Gagnier",
        "William Mooney",
    ]
)


responded = set(
    [
        "Ashwin Sundar",
        "Bill Frasure",
        "Bruce Eckel",
        "Chris Marks",
        "Chris Phelps",
        "D. J. Hagberg",
        "Dave Bartlett",
        "Emma Fewer",
        "James Ward",
        "Jeremy Cerise",
        "Jimmy Utley",
        "Joe Schrag",
        "Joey Gibson",
        "Justin Poehnelt",
        "Justin Ryan",
        "Mallory Weber",
        "Schuyler Metcalf",
        "Stephanie Reeves",
        "Tom Gagnier",
        "Will Mooney",
    ]
)

for nonresponded in attendees - responded:
    print(nonresponded)
