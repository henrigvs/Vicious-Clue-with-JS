class Filtering:

    @staticmethod
    def filterEnigmaByDifficulty(enigmas, difficulty):
        enigmasFiltered = []
        for enigma in enigmas:
            if enigma['difficulty'] == difficulty:
                enigmasFiltered.append(enigma)
        return enigmasFiltered