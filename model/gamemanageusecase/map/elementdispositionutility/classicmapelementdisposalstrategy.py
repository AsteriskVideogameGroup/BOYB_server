import copy
import random

import math

from foundations.geometry.cartesianposition import Position
from foundations.geometry.shapedimension import Dimension
from model.gamemanageusecase.map.elementdispositionutility.imapelementdisposalstrategy import \
    IMapElementDisposalStrategy
from model.gamemanageusecase.map.map import Map
from model.gamemanageusecase.objects.obstacles.idestructibleobstacle import IDestructibleObstacle


class ClassicMapElementDisposalStrategy(IMapElementDisposalStrategy):
    def disposeInitialMapState(self, maptosetup: Map):

        # disponi ostacoli indistruttibili
        maptosetup.undescructibles = self._disposeUndestrObstacles(maptosetup.undescructibles, maptosetup.dimensions)

        # disponi bob
        self._disposeBoBs(maptosetup.bobs, maptosetup.dimensions)

        # disponi ostacoli distruttibili
        maptosetup.destructibiles = self._disposeDestrObstacles(maptosetup.destructibiles, maptosetup.dimensions,
                                                                maptosetup.bobs)

    def _disposeUndestrObstacles(self, undstrobstacles: list, dim: Dimension) -> list:
        """
        Dispose undestructible obstacles inside a map in (2k,2k) positions

        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   | X |   | X |   | X |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   | X |   | X |   | X |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   | X |   | X |   | X |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   | X |   | X |   | X |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+

        X = undstrobstacles placed
        :param undstrobstacles: list of different sample of undestructible obstacles that must be placed
        :param dim: dimensions of the map to be filled
        :return: list of undestructible obstacles that are positioned
        """

        height = dim.height
        width = dim.width

        undestructibleelementslist = list()

        for i in range(1, height + 1):
            if i % 2 == 0:
                for j in range(1, width + 1):
                    if j % 2 == 0:
                        newundstr: IDestructibleObstacle = copy.deepcopy(random.choice(undstrobstacles))
                        newposition: Position = Position(i, j)
                        newundstr.place(newposition)
                        undestructibleelementslist.append(newundstr)

        return undestructibleelementslist

    def _disposeBoBs(self, bobs: list, dim: Dimension):
        """
        Disposal algorithm for BoBs (balanced number of BoBs for each side: longer side => more BoBs)

        examples: 6 BoBs on 7x5 map

         +---+---+---+---+---+---+---+
         | XY|   |   | X |   |   | X |
         +---+---+---+---+---+---+---+
         |   |   |   |   |   |   |   |
         +---+---+---+---+---+---+---+
         |   |   |   |   |   |   |   |
         +---+---+---+---+---+---+---+
         |   |   |   |   |   |   |   |
         +---+---+---+---+---+---+---+
         | X |   |   | X |   |   | XY|
         +---+---+---+---+---+---+---+

         X = BoB placed
         Y = BoB placed in case of just 2 players

        :param bobs: BoBs that must be placed
        :param dim: Map dimensions
        """

        bobtoplace = len(bobs)

        if bobtoplace == 2:
            bobs[0].place(Position(1, 1))
            bobs[1].place(Position(dim.width, dim.height))

        elif bobtoplace > 0:
            width = dim.width
            height = dim.height

            bobindex = 0

            maxdim = max(height, width)

            if maxdim == height:
                bobtoplace, bobindex = self._disposeBoBsOnWidth(1, False, 4, bobtoplace, bobs, bobindex,
                                                                width, False)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnHeight(width, False, 3, bobtoplace, bobs, bobindex,
                                                                     height, True)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnWidth(height, True, 2, bobtoplace, bobs, bobindex,
                                                                    width, False)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnHeight(1, True, 1, bobtoplace, bobs, bobindex,
                                                                     height, True)
            else:

                bobtoplace, bobindex = self._disposeBoBsOnHeight(width, False, 4, bobtoplace, bobs, bobindex,
                                                                 height, False)
                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnWidth(height, True, 3, bobtoplace, bobs, bobindex,
                                                                    width, True)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnHeight(1, True, 2, bobtoplace, bobs, bobindex,
                                                                     height, False)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnWidth(1, False, 1, bobtoplace, bobs, bobindex,
                                                                    width, True)

    def _disposeBoBsOnHeight(self, x: int, negative: bool, remainingsides: int, remainingbobs: int, bobslist: list,
                             bobit: int, height: int, longside: bool):
        """
        Subroutine for the disposal of BoBs in a column of the map
        :param x: number of the column
        :param negative: true, if the disposal starts from the end of the column, or false, if the disposal starts from the beginning of the column
        :param remainingsides: number of other columns or rows where bobs have to be disposed
        :param remainingbobs: number of remaining disposing bobs
        :param bobslist: list of disposing bobs
        :param bobit: index of bobslist from which must be dispose the bobs
        :param height: height of the column
        :param longside: true, if the columns are longer than rows, or false, otherwise
        :return: the number of remaining disposing bobs and the index of bobs array from which resume the disposing
        """
        if longside:
            delta: int = math.floor(height / math.ceil(remainingbobs / remainingsides))
        else:
            delta: int = math.floor(height / math.floor(remainingbobs / remainingsides))
        if negative:
            for i in range(height, 1, -delta):
                bobslist[bobit].place(Position(x, i))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1
        else:
            for i in range(1, height, delta):
                bobslist[bobit].place(Position(x, i))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1

        return remainingbobs, bobit

    def _disposeBoBsOnWidth(self, y: int, negative: bool, remainingsides: int, remainingbobs: int, bobslist: list,
                            bobit: int, width: int, longside: bool):
        """
        Subroutine for the disposal of BoBs in a row of the map
        :param y: number of the row
        :param negative: true, if the disposal starts from the end of the row, or false, if the disposal starts from the beginning of the row
        :param remainingsides: number of other columns or rows where bobs have to be disposed
        :param remainingbobs: number of remaining disposing bobs
        :param bobslist: list of disposing bobs
        :param bobit: index of bobslist from which must be dispose the bobs
        :param width: width of the row
        :param longside: true, if the rows are longer than columns, or false, otherwise
        :return: the number of remaining disposing bobs and the index of bobs array from which resume the disposing
        """

        if longside:
            delta: int = math.floor(width / math.ceil(remainingbobs / remainingsides))
        else:
            delta: int = math.floor(width / math.floor(remainingbobs / remainingsides))
        if negative:
            for i in range(width, 1, -delta):
                bobslist[bobit].place(Position(i, y))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1
        else:
            for i in range(1, width, delta):
                bobslist[bobit].place(Position(i, y))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1

        return remainingbobs, bobit

    def _selectSafeArea(self, dim: Dimension, bobs: list, mindist: int) -> list:
        """
        Select area that must be free near bobs
        :param dim: dimensions of the map where to select the safe area
        :param bobs: bob array from which is computed the safe area
        :param mindist: minimum distance that must be free (x and y)
        :return: list of positions that must be left free
        """

        safearea = list()

        for bob in bobs:

            bobx = bob.position.x
            boby = bob.position.y

            startx = bobx - mindist
            starty = boby - mindist
            endx = bobx + mindist
            endy = boby + mindist

            if startx < 1:
                startx = 1
            if starty < 1:
                starty = 1
            if endx > dim.width:
                endx = dim.width
            if endy > dim.height:
                endy = dim.height

            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    if not ((x % 2 == 0) and (y % 2 == 0)):  # if the position is not (even,even) resume
                        safearea.append(Position(x, y))

        return safearea

    def _disposeDestrObstacles(self, dstrobstacles: list, dim: Dimension, bobs: list) -> list:
        """
        Randomly dispose destructible obstacles inside a map (caring about a safe zone near BoBs)

        example: 4 BoBs on 7x7 map. (safe zone of 1 tile)

        +---+---+---+---+---+---+---+
        | $ | + | X |   |   | + | $ |
        +---+---+---+---+---+---+---+
        | + | # | X | # |   | # | + |
        +---+---+---+---+---+---+---+
        |   |   |   | X |   | X |   |
        +---+---+---+---+---+---+---+
        |   | # | X | # |   | # |   |
        +---+---+---+---+---+---+---+
        |   | X | X | X |   |   |   |
        +---+---+---+---+---+---+---+
        | + | # | X | # |   | # | + |
        +---+---+---+---+---+---+---+
        | $ | + |   |   |   | + | $ |
        +---+---+---+---+---+---+---+

        # = Undestructible obstacles
        X = Destructible obstacles
        + = Safe zone
        $ = BoB

        :param undstrobstacles: list of different samples of destructible obstacles that must be placed
        :param dim: dimensions of the map to be filled
        :param bobs: list of bobs from which is computed the safe area (obstacles cannot be in safe area)
        :return: list of destructible obstacles that are positioned
        """

        MINDIST = 1  # Minimum distance from bobs
        PLACINGPROBABILITY = 0.45  # Probability of placing obstacle in a given position

        destructibleelementslist = list()

        safearea = self._selectSafeArea(dim, bobs, MINDIST)

        for y in range(1, dim.height + 1):
            for x in range(1, dim.width + 1):
                if not ((x % 2 == 0) and (y % 2 == 0)):  # if the position is not (even,even) resume

                    newposition = Position(x, y)
                    if not (newposition in safearea):  # if the position is not in the safearea
                        if random.random() < PLACINGPROBABILITY:
                            newobstacle = copy.deepcopy(random.choice(dstrobstacles))
                            newobstacle.place(newposition)

                            destructibleelementslist.append(newobstacle)

        return destructibleelementslist

    # TODO controllare quando ci saranno i powerup
    '''
    def disposePowerUps(self, powerups: list, dim: Dimension, occpositions: dict) -> list:
        """
        Randomly place a list of power-ups on the map (in an unoccupied position)
        :param powerups: list of power-ups to place
        :param dim: dimension of the map where to place the power-ups
        :param occpositions: dictionary with Position as keys to sign the occupied positions
        :return: list of placed power-ups
        """

        poweruplist = list()
        for pu in powerups:
            newy = random.randrange(1, dim.height + 1)
            newx = random.randrange(1, dim.width + 1)
            newpos = Position(newx, newy)
            ## TODO: Potrebbe dare problemi quando si andrà a rendere fluido il movimento dei BoB
            ## TODO: Essi potranno trovarsi nel punto di spawn del power-up se la loro posizione è float e non int
            while (newpos in occpositions):
                newy = random.randrange(1, dim.height + 1)
                newx = random.randrange(1, dim.width + 1)
                newpos = Position(newx, newy)

            pu.setPosition(newpos)
            poweruplist.append(pu)

        return poweruplist
        '''

    '''
    
        def _disposeUndestructibleObstacles(self, dimension: Dimension, undesctructibles: list) -> list:

        tmplistundestructibles: list = list()

        initialrow = 1
        lastrow = dimension.height + 1
        initialcolumn = 1
        lastcolumn = dimension.width + 1

        for i in range(initialrow, lastrow):
            if i % 2 == 0:
                for j in range(initialcolumn, lastcolumn):
                    if j % 2 == 0:
                        obstacle: IUndestructibleObstacle = copy.deepcopy(
                            random.choice(undesctructibles))  # primo ostacolo
                        newposition: Position = Position(i, j)
                        obstacle.place(newposition)  # set della posizione
                        tmplistundestructibles.append(obstacle)

        return tmplistundestructibles
        
    def _disposeBobs(self, dimension: Dimension, bobs: list) -> list:

        bobtoplace: int = len(bobs)
        
        sides: int = 4  # saranno sempre 4 lati per ogni mappa
        bobindex: int = 0 # inizia a disporre dal primo Bob

        if dimension.height > dimension.width:
            
            for i in range(0, sides):
                
                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBobOnSide(bobs, bobindex, dimension, bobtoplace, )
                else:
                    pass

    def _disposeBobOnSide(self, bobtodispose: list, bobindex: int, mapdimension: Dimension, positiononsideindex: int,
                          isrow: bool, numbobtodispose: int, numremainingsides: int, sidedimension: int,
                          islongerside: bool, disposefromleft: bool) -> (int, int):

        # calcolo spazio tra due bob vicini
        if islongerside:
            delta: int = math.floor(sidedimension / math.ceil(numbobtodispose / numremainingsides))
        else:
            delta: int = math.floor(sidedimension / math.floor(numbobtodispose / numremainingsides))

        # disposefromend è true se si inizia a disporre da sinistra
        if disposefromleft:
            initialposition: int = 1
            endposition: int = mapdimension.width
            step: int = delta
        else:
            initialposition: int = mapdimension.width
            endposition: int = 1
            step: int = -1 * delta

        for i in range(initialposition, endposition, step):
            bob: Bob = bobtodispose[bobindex]
            if isrow is True:
                newbobposition: Position = Position(i, positiononsideindex)
            else:
                newbobposition: Position = Position(positiononsideindex, i)

            bob.place(newbobposition)
            numbobtodispose -= 1  # devi posizionare un bob in meno
            bobindex += 1  # si può posizionare il bob successivo
            
            return numbobtodispose, bobindex'''
