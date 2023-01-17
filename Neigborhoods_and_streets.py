class Neighborhoods_and_streets:
    def __init__(self):
        self.neighborhoods = []
    
    def add_neighborhood(self, name):
        '''Adds a neighborhood to the list of neighborhoods'''
        for i in range(len(self.neighborhoods)):
            if name in self.neighborhoods[i]:
                print("Neighborhoodname already exists")
                break
        else:
            self.neighborhoods.append([name])

    def add_street_to_neighborhood(self, neighborhoodname, streetname):
        '''Adds a street to a neighborhood'''
        for i in range(len(self.neighborhoods)):
            if self.neighborhoods[i][0] == neighborhoodname:
                self.neighborhoods[i].append(streetname)
                break
    
    def print_streets_in_neighborhood(self, neighborhoodname):
        '''Prints all streets in a neighborhood'''
        for i in range(len(self.neighborhoods)):
            if self.neighborhoods[i][0] == neighborhoodname:
                if len(self.neighborhoods[i]) == 1:
                    print("There are no streets in this neighborhood")
                else:
                    for street in range(1, len(self.neighborhoods[i])):
                        if street != len(self.neighborhoods[i]) - 1:
                            print(self.neighborhoods[i][street], end=", ")
                        else:
                            print(self.neighborhoods[i][street])
                break
    
    def neighborhood_of_street(self, streetname):
        '''Prints the neighborhood of a street'''
        for i in range(len(self.neighborhoods)):
            if streetname in self.neighborhoods[i]:
                print(self.neighborhoods[i][0])
                break

neighborhoods_and_streets = Neighborhoods_and_streets()
neighborhoods_and_streets.add_neighborhood("Reykjavík")
neighborhoods_and_streets.add_neighborhood("Kópavogur")
neighborhoods_and_streets.print_streets_in_neighborhood("Reykjavík")
neighborhoods_and_streets.add_street_to_neighborhood("Reykjavík", "Laugavegur")
neighborhoods_and_streets.print_streets_in_neighborhood("Reykjavík")
neighborhoods_and_streets.neighborhood_of_street("Laugavegur")
