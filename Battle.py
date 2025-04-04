
class Battle:
    def __init__(self) -> None:
        pass

    @staticmethod
    def battleBetween(armyI, armyII):  # Quitamos 'self'
        totalForceI = sum(unit.force for unit in armyI.unit)
        totalForceII = sum(unit.force for unit in armyII.unit)

        if totalForceI > totalForceII:
            armyI.gold += 100
            armyII.loseUnits()
        elif totalForceI == totalForceII:
            armyI.loseUnits()
            armyII.loseUnits()
        else:
            armyII.gold += 100
            armyI.loseUnits()

    