#programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#Nesting
capitals = {
  "France":"Paris",
  "Germany":"Berlin",
}

#Nesting list in a dictionay

travel_log = {
  "France": {"cities_visited":["Paris", "Lille", "Dijon"]},
  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting a dictionay in a list

travel_log = [
  {
    "country":"France",  "cities_visited":["Paris", "Lille", "Dijon"], "total_visites": 12
  },
  {
    "country":"Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visites": 5
  },
]
