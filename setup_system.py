from foundations.geometry.shapedimension import Dimension
from foundations.ioc.FEDContainer import FEDContainer
from foundations.ioc.naiveimplementation.DepthFirstGraphICTranslator import DepthFirstGraphICTranslator
from foundations.ioc.naiveimplementation.JSONSource import JSONSource
from foundations.ioc.naiveimplementation.NaiveLibraryImporter import NaiveLibraryImporter
from foundations.ioc.utils.InjContentTranslator import InjContentTranslator
from foundations.ioc.utils.InjectionSource import InjectionSource
from foundations.ioc.utils.LibraryInporter import LibraryImporter
from foundations.persistence.ibobdescriptiondao import IBobDescriptionDAO
from foundations.persistence.idaoabstractfactory import IDAOAbstractFactory
from foundations.persistence.imodedao import IModeDAO
from foundations.persistence.iplayerdao import IPlayerDAO
from model.gamemanageusecase.characters.bobdescription import BobDescription
from model.gamemanageusecase.modes.mode import GameMode
from model.gamemanageusecase.players.player import Player

if __name__ == "__main__":
    # configuration source
    source: InjectionSource = JSONSource("etc/config.json")

    # setup libreria ioc
    importer: LibraryImporter = NaiveLibraryImporter()
    trans: InjContentTranslator = DepthFirstGraphICTranslator(importer)
    container: FEDContainer = FEDContainer(trans, source)

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

    otherdescription: BobDescription = BobDescription()
    otherdescription.id = "king_bob"
    otherdescription.damage = 1
    otherdescription.baselives = 5
    otherdescription.contemporarybombs = 1
    otherdescription.speed = 6
    otherdescription.specialpower = "none"
    otherdescription.range = 2

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
    mapelementdisposerid: str = "classic_strategy"
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
    descriptiondao.save(otherdescription)



