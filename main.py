"""
Copyright (C) 2023 - Aeris One

Ce programme est régi par la licence CeCILL soumise au droit français et
respectant les principes de diffusion des logiciels libres. Vous pouvez
utiliser, modifier et/ou redistribuer ce programme sous les conditions
de la licence CeCILL diffusée sur le site "http://www.cecill.info".
"""


def retrieve_sconfig() -> dict:
    """
    Retrieve system config from environment variables

    :return: dict
    """
    pass


def main(sconfig: dict):
    """
    Main function

    Should be called only once.
    Should define discord and matrix clients, then run all functions in events/
        passing them the clients.
    Should finally start the clients.
    """
    pass


if __name__ == "__main__":
    sconfig = retrieve_sconfig()
    main(sconfig)
