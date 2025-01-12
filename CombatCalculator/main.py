# Main file for the Reform or Revolution Combat Calculator

import utils
import player

if __name__ == "__main__":
    utils.LoadDefaults()
    p = player.Player()

    p.ManageUnits()

    input()