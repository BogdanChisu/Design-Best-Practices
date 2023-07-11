"""
https://refactoring.guru/design-patterns/abstract-factory
"""

class Sedan:
    def who_am_i(self):
        pass


class LHDSedan(Sedan):
    def who_am_i(self):
        print('Left Hand Drive Sedan')


class RHDSedan(Sedan):
    def who_am_i(self):
        print('Right Hand Drive Sedan')


class StationWagon:
    def who_am_i(self):
        pass


class LHDStationWagon(StationWagon):
    def who_am_i(self):
        print('Left Hand Drive Station Wagon')


class RHDStationWagon(StationWagon):
    def who_am_i(self):
        print('Right Hand Drive Station Wagon')


class Coupe:
    def who_am_i(self):
        pass


class LHDCoupe(Coupe):
    def who_am_i(self):
        print('Left Hand Drive Coupe')


class RHDCoupe(Coupe):
    def who_am_i(self):
        print('Right Hand Drive Coupe')


class CarFactory:
    def create_sedan(self):
        pass

    def create_station_wagon(self):
        pass

    def create_coupe(self):
        pass


class LHDCarFactory(CarFactory):
    def create_sedan(self):
        return LHDSedan()

    def create_station_wagon(self):
        return LHDStationWagon()

    def create_coupe(self):
        return LHDCoupe()


class RHDCarFactory(CarFactory):
    def create_sedan(self):
        return RHDSedan()

    def create_station_wagon(self):
        return RHDStationWagon()

    def create_coupe(self):
        return RHDCoupe()


def main():
    car_factory = LHDCarFactory()
#    car_factory = RHDCarFactory()

    sedan = car_factory.create_sedan()
    sedan.who_am_i()

    station_wagon = car_factory.create_station_wagon()
    station_wagon.who_am_i()

    coupe = car_factory.create_coupe()
    coupe.who_am_i()


if __name__ == '__main__':
    main()