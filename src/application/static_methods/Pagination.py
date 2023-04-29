class Pagination:

    @staticmethod
    def paginateRiddle(riddle, maxPerPage):
        pagination = {}
        lastPage = (len(riddle) / maxPerPage) + 1
        key = 1
        indexEnigmas = 0
        while key <= lastPage:
            tempArray = []
            i = 0
            while i < 5 and indexEnigmas < len(riddle):
                tempArray.append(riddle[indexEnigmas])
                indexEnigmas += 1
                i += 1
            pagination[key] = tempArray
            key += 1
        return pagination
