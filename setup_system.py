from foundations.persistence.ibobdescriptiondao import IBobDescriptionDAO
from foundations.persistence.idaoabstractfactory import IDAOAbstractFactory
from foundations.persistence.imodedao import IModeDAO
from foundations.persistence.iplayerdao import IPlayerDAO
from foundations.geometry.shapedimension import Dimension
from foundations.inversionofcontrol.ioccontainer import InversionOfControlContainer
from model.gamemanageusecase.characters.bobdescription import BobDescription
from model.gamemanageusecase.modes.mode import GameMode
from model.gamemanageusecase.players.player import Player

if __name__ == "__main__":
    # inizializzazione container IoC
    container: InversionOfControlContainer = InversionOfControlContainer().init("etc/config.json")

    # inizializzazione database
    daofactory: IDAOAbstractFactory = container.getObject("daofactory")
    daofactory.init()

    # creazione descrittori bob
    bobdescription: BobDescription = BobDescription()
    bobdescription.id = "classic_bob"
    bobdescription.damage = 1
    bobdescription.baselives = 200
    bobdescription.contemporarybombs = 1
    bobdescription.speed = 6
    bobdescription.specialpower = "none"
    bobdescription.range = 1

    bobdescription: BobDescription = BobDescription()
    bobdescription.id = "king_bob"
    bobdescription.damage = 1
    bobdescription.baselives = 5
    bobdescription.contemporarybombs = 1
    bobdescription.speed = 6
    bobdescription.specialpower = "none"
    bobdescription.range = 2

    # creazione oggetti player da salvare nel DB
    player1: Player = Player("p1")
    player2: Player = Player("p2")
    player3: Player = Player("p3")
    player4: Player = Player("p4")

    # creazione oggetti mode da salvare nel DB
    name: str = "classic_mode"
    mapdimensions: Dimension = Dimension(5, 5)
    maxplayers: int = 4
    secgameduration: int = 300
    mapelementdisposerid: str = "ClassicMapElementDisposalStrategy"
    objectfactoryid: str = "classic_factory"
    mode: GameMode = GameMode(name, mapdimensions, maxplayers, secgameduration, mapelementdisposerid, objectfactoryid)

    # data access objects
    playerdao: IPlayerDAO = daofactory.getPlayerDAO()
    modedao: IModeDAO = daofactory.getModeDAO()
    descriptiondao: IBobDescriptionDAO = daofactory.getBobDescriptionDAO()

    # salvataggio nel database dei player
    playerdao.save(player1)
    playerdao.save(player2)
    playerdao.save(player3)
    playerdao.save(player4)

    # salvataggio nel database della modalità
    modedao.save(mode)

    # salvataggio bobdescriptor
    descriptiondao.save(bobdescription)



