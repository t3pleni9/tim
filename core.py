import os

from main.actors import ACTORS
from main.kernel import core_kernel
from main.models import Event
from setup import init

NAME = 'TIM'
VERSION = '1.0.0'
DATA_PATH = '.data'


def main():
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    init(DATA_PATH)
    for Actor in ACTORS:
        Actor.init()

    core_kernel.emit_event(Event.INIT, None)


if __name__ == '__main__':
    main()
