#  W    zorowane na przykładzie Rona Zacharskiego


from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    odlegloscWszystkich = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = abs(rating2[klucz] - rating1[klucz])
            odlegloscWszystkich = odlegloscWszystkich + abs(rating2[klucz] - rating1[klucz])
            """print (odleglosc, klucz)"""
    if (udaloSiePorownac==True):
        """print 'Odleglosc w metryce taksowkowej'
        print (odlegloscWszystkich)"""
        return odlegloscWszystkich
    else:
        return -1
    pass


def computeNearestNeighbor(username, users):
    """dla danego użytkownika username, zwróć ze słownika users nazwę użytkownika o najbliższych preferencjach"""
    nameOfNearestNeighbor = ""
    distances = []
    imie2 = ""
    # TODO: wpisz kod
    odleglosci = []
    for compareUser in users:
        if(compareUser!=username):
            odleglosc = 0
            odleglosc = manhattan(users[username], users[compareUser])
            odleglosci.append((odleglosc, compareUser))
    nameOfNearestNeighbor = sorted(odleglosci[1])
    print nameOfNearestNeighbor[1]
    return nameOfNearestNeighbor[1]

def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearestName = computeNearestNeighbor(username, users)
    print 'Najblizszy sasiad to: %s' % nearestName
    recommendations = []
    ratingOfNearest = users[nearestName]
    print 'Jego rekomendacje to:'
    print ratingOfNearest
    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad
    # TODO: wpisz kod
    userRating = users[username]
    
    for artist in ratingOfNearest:
        if not artist in userRating:
            recommendations.append((artist, ratingOfNearest[artist]))
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

# przykłady

print( recommend('Hela', users))
#print( recommend('Celina', users))
#manhattan(users['Ania'], users['Gosia'])
#computeNearestNeighbor('Ania', users)
