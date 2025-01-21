# External Imports

# Internal Imports
import player
import utils


if __name__ == '__main__':
    try:
        pd = utils.LoadPlayerData()
    except Exception as e:
        utils.PrintErrorMenu(e)
        pd = utils.CreatePlayerData()
    
    p = player.Player(pd[0], pd[1], pd[2], pd[3], pd[4], pd[5], pd[6])
    
    p.main()
