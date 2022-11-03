from random import choice, randint


class SingleColour(object):
    name = "SingleColour"
    sprites = {1: 'single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length

class TwoColour(object):
    name = "TwoColour"
    sprites = {1: 'single', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class Tabby(object):
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"

class Marbled(object):
    name = "Marbled"
    sprites = {1: 'marbled', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} marbled"
        else:
            return self.colour + self.length + " marbled"

class Rosette(object):
    name = "Rosette"
    sprites = {1: 'rosette', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rosette"
        else:
            return self.colour + self.length + " rosette"

class Smoke(object):
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"

class Ticked(object):
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"

class Speckled(object):
    name = "Speckled"
    sprites = {1: 'speckled', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} speckled{self.length}"
        else:
            return f"{self.colour} speckled{self.length}"

class Bengal(object):
    name = "Bengal"
    sprites = {1: 'bengal', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'

    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bengal{self.length}"
        else:
            return f"{self.colour} bengal{self.length}"

class Snowflake(object):
    name = "Snowflake"
    sprites = {1: 'snowflake', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} snowflake"
        else:
            return self.colour + self.length + " snowflake"

class Clouded(object):
    name = "Clouded"
    sprites = {1: 'clouded', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} clouded"
        else:
            return self.colour + self.length + " clouded"

class Merle(object):
    name = "Merle"
    sprites = {1: 'merle', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} merle"
        else:
            return self.colour + self.length + " merle"

class Abyssinian(object):
    name = "Abyssinian"
    sprites = {1: 'abyssinian', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} abyssinian"
        else:
            return self.colour + self.length + " abyssinian"

class Doberman(object):
    name = "Doberman"
    sprites = {1: 'doberman', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} doberman"
        else:
            return self.colour + self.length + " doberman"

class Pinstripe(object):
    name = "Pinstripe"
    sprites = {1: 'pinstripe', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} pinstripe"
        else:
            return self.colour + self.length + " pinstripe"

class Ghost(object):
    name = "Ghost"
    sprites = {1: 'ghost', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ghost"
        else:
            return self.colour + self.length + " ghost"

class Spotted(object):
    name = "Spotted"
    sprites = {1: 'spotted', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} spotted"
        else:
            return self.colour + self.length + " spotted"

class Tortie(object):
    name = "Tortie"
    sprites = {1: 'tortie', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',  'MITAINE', 'SQUEAKS', 'STAR',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO', 'VITILIGO2'
        ]

    def __init__(self, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                              "LIGHTBROWN", "BROWN", "DARKBROWN",
                              "BLACK2", "DARK", "CHOCOLATE", "FAWN",
                              "LILAC", "BLUE", "CINNAMON", "CARAMEL"])
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"

class Calico(object):
    name = "Calico"
    sprites = {1: 'calico', 2: 'white'}
    white_patches = [
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS',
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE'
    ]
    def __init__(self, length):
        self.colour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                              "LIGHTBROWN", "BROWN", "DARKBROWN",
                              "BLACK2", "DARK", "CHOCOLATE", "FAWN",
                              "LILAC", "BLUE", "CINNAMON", "CARAMEL"])
        self.length = length
        self.white = True

    def __repr__(self):
        return f"calico{self.length}"


# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK', 'PALE', 'CREAM',
    'APRICOT', 'ORANGE', 'FAWN', 'CINNAMON', 'CHOCOLATE'
]
pelt_c_no_white = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER', 'GOLDEN',
    'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK', 'PALE', 'CREAM',
    'APRICOT', 'ORANGE', 'FAWN', 'CINNAMON', 'CHOCOLATE'
]
pelt_c_no_bw = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'PALEGINGER', 'GOLDEN', 'GINGER',
    'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'BLUE', 'CARAMEL', 'LILAC', 'DARK', 'PALE', 'CREAM',
    'APRICOT', 'ORANGE', 'FAWN', 'CINNAMON', 'CHOCOLATE'
]
tortiepatterns = ['tortiesolid', 'tortietabby', 'tortiebengal', 'tortiemarbled', 'tortieticked',
    'tortiesmoke', 'tortierosette', 'tortiespeckled', 'tortiesnowflake', 'tortieclouded', 'tortiemerle',
    'tortieghost', 'tortiepinstripe']
patch_colours = ['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'GOLDONE', 'GOLDTWO',
    'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR', 'PALEONE2', 'PALETWO2', 'PALETHREE2',
    'PALEFOUR2', 'CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR', 'APRICOTONE', 'APRICOTTWO'
    'APRICOTTHREE', 'APRICOTFOUR', 'ORANGEONE', 'ORANGETWO', 'ORANGETHREE', 'ORANGEFOUR']
tortiebases = ['spotted', 'single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette',
               'speckled', 'abyssinian', 'snowflake', 'clouded', 'merle', 'ghost', 'pinstripe', 'doberman']
tortiecolours = ["SILVER", "GREY", "DARKGREY", "BLACK", "LIGHTBROWN", "BROWN", "DARKBROWN", "BLUE",
                 "LILAC", "BLACK2", "DARK", "FAWN", "CINNAMON", "CARAMEL", "CHOCOLATE"]

pelt_length = ["short", "medium", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE',
               'PALEYELLOW', 'RED', 'AQUA', 'PALEVIOLET', 'SAGE', 'PALEBLUE', 'PINK',
               'DARKPINK', 'VIOLET', 'BROWN', 'SPRINGGREEN', 'GOLDEN', 'HONEY',
               'COPPER', 'MAGENTA', 'MINT', 'EMERALD', 'DARKRED']
scars1 = ["ONE", "TWO", "THREE"]
scars2 = ["LEFTEAR", "RIGHTEAR", "LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW"]
scars4 = [
    "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
    "TOETRAP", "LEGBITE", "NECKBITE", "FACE"
]
scars5 = ["SNAKE"]

plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                    "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                    "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "PINK", "PURPLE", "MULTI", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW"
]

pelt_names_F = ["Spotted", "SingleColour", "SingleColour", "TwoColour", "Tabby", "Tortie", "Calico", "Ghost", "Doberman", "Pinstripe",
    "Tabby", "TwoColour", "Speckled", "Marbled", "Bengal", "Rosette", "Smoke", "Ticked", "Merle", "Abyssinian", "Snowflake", "Clouded"]
pelt_names_M = ["Spotted", "SingleColour", "SingleColour", "TwoColour", "Tabby", "Tabby", "Speckled", "Ghost", "Doberman", "Pinstripe",
    "TwoColour", "Marbled", "Bengal", "Rosette", "Smoke", "Ticked", "Merle", "Abyssinian", "Snowflake", "Clouded"]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'WHITE2', 'BLUE', 'LILAC', 'BLACK2', 'DARK', 'FAWN', 'CINNAMON', 'CARAMEL',
    'CHOCOLATE', 'PALE', 'APRICOT', 'CREAM', 'ORANGE'
]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE',
    'BLUEYELLOW', 'BLUEGREEN', 'PALEYELLOW', 'RED', 'AQUA', 'PALEVIOLET',
    'SAGE', 'PALEBLUE', 'PINK', 'DARKPINK', 'VIOLET', 'BROWN', 'SPRINGGREEN',
    'GOLDEN', 'HONEY', 'COPPER', 'MAGENTA', 'MINT', 'EMERALD', 'DARKRED'
]
little_white = ['LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS', 
    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY']
mid_white = ['TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR']
high_white = ['ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 
    'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
    'CURVED', 'GLASS', 'MASKMANTLE']
mostly_white = ['VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE']
point_markings = ['COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL']
vit = ['VITILIGO', 'VITILIGO2']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE', 'EXTRA', 'POINTMARK'
]

skin_sprites = ['BLACK', 'RED', 'PINK']


# CHOOSING PELT
def choose_pelt(gender,colour=None,white=None,pelt=None,length=None,determined=False):
    if pelt is None:
        a = randint(0, 100)
        if a != 1:
            pelt = choice(pelt_names_F) if gender == "female" else choice(pelt_names_M)
        else:
            pelt = choice(pelt_names_F)
            if gender == 'male' and pelt in ['Tortie', 'Calico']:
                print("Male tortie/calico!")
    elif pelt in ['Tortie', 'Calico'] and gender == 'male' and not determined:
        a = randint(0, 200)
        if a != 1:
            pelt = choice(pelt_names_M)
    if length is None:
        length = choice(pelt_length)
    if pelt == "SingleColour":
        if colour is None and not white:
            return SingleColour(choice(pelt_colours), length)
        elif colour is None:
            return SingleColour("WHITE", length)
        else:
            return SingleColour(colour, length)
    elif pelt == "TwoColour":
        if colour is None:
            return TwoColour(choice(pelt_c_no_white), length)
        else:
            return TwoColour(colour, length)
    elif pelt == "Tabby":
        if colour is None and white is None:
            return Tabby(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Tabby(choice(pelt_colours), white, length)
        else:
            return Tabby(colour, white, length)
    elif pelt == "Marbled":
        if colour is None and white is None:
            return Marbled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Marbled(choice(pelt_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == "Rosette":
        if colour is None and white is None:
            return Rosette(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rosette(choice(pelt_colours), white, length)
        else:
            return Rosette(colour, white, length)
    elif pelt == "Smoke":
        if colour is None and white is None:
            return Smoke(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Smoke(choice(pelt_colours), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == "Ticked":
        if colour is None and white is None:
            return Ticked(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == "Speckled":
        if colour is None and white is None:
            return Speckled(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Speckled(choice(pelt_colours), white, length)
        else:
            return Speckled(colour, white, length)
    elif pelt == "Bengal":
        if colour is None and white is None:
            return Bengal(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Bengal(choice(pelt_colours), white, length)
        else:
            return Bengal(colour, white, length)
    elif pelt == "Snowflake":
        if colour is None and white is None:
            return Snowflake(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Snowflake(choice(pelt_colours), white, length)
        else:
            return Snowflake(colour, white, length)
    elif pelt == "Abyssinian":
        if colour is None and white is None:
            return Abyssinian(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Abyssinian(choice(pelt_colours), white, length)
        else:
            return Abyssinian(colour, white, length)
    elif pelt == "Merle":
        if colour is None and white is None:
            return Merle(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Merle(choice(pelt_colours), white, length)
        else:
            return Merle(colour, white, length)
    elif pelt == "Clouded":
        if colour is None and white is None:
            return Clouded(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Clouded(choice(pelt_colours), white, length)
        else:
            return Clouded(colour, white, length)
    elif pelt == "Doberman":
        if colour is None and white is None:
            return Doberman(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Doberman(choice(pelt_colours), white, length)
        else:
            return Doberman(colour, white, length)
    elif pelt == "Pinstripe":
        if colour is None and white is None:
            return Pinstripe(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Pinstripe(choice(pelt_colours), white, length)
        else:
            return Pinstripe(colour, white, length)
    elif pelt == "Ghost":
        if colour is None and white is None:
            return Ghost(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ghost(choice(pelt_colours), white, length)
        else:
            return Ghost(colour, white, length)
    elif pelt == "Spotted":
        if colour is None and white is None:
            return Spotted(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Spotted(choice(pelt_colours), white, length)
        else:
            return Spotted(colour, white, length)
    elif pelt == "Tortie":
        if white is None:
            return Tortie(choice([False, True]), length)
        else:
            return Tortie(white, length)
    else:
        return Calico(length)

def describe_color(pelt, tortiecolour, tortiepattern, white_patches):
        color_name = ''
        color_name = str(pelt.colour).lower()
        if tortiecolour != None:
            color_name = str(tortiecolour).lower()
        if color_name == 'palegrey':
            color_name = 'pale grey'
        elif color_name == 'darkgrey':
            color_name = 'dark grey'
        elif color_name == 'paleginger':
            color_name = 'pale ginger'
        elif color_name == 'darkginger':
            color_name = 'dark ginger'
        elif color_name == 'lightbrown':
            color_name = 'light brown'
        elif color_name == 'darkbrown':
            color_name = 'dark brown'
        elif color_name == 'white2':
            color_name = 'white'
        elif color_name == 'black2':
            color_name = 'black'
        if pelt.name == "Tabby":
            color_name = color_name + ' tabby'
        elif pelt.name == "Speckled":
            color_name = color_name + ' speckled'
        elif pelt.name == "Bengal":
            color_name = color_name + ' bengal'
        elif pelt.name == "Marbled":
            color_name = color_name + ' marbled tabby'
        elif pelt.name == "Rosette":
            color_name = color_name + ' rosetted'
        elif pelt.name == "Ticked":
            color_name = color_name + ' ticked tabby'
        elif pelt.name == "Smoke":
            color_name = color_name + ' smoke'
        elif pelt.name == "Pinstripe":
            color_name = color_name + ' pinstripe tabby'
        elif pelt.name == "Doberman":
            color_name = color_name + ' doberman point'
        elif pelt.name == "Ghost":
            color_name = color_name + ' ghost tabby'
        elif pelt.name == "Abyssinian":
            color_name = color_name + ' abyssinian'
        elif pelt.name == "Clouded":
            color_name = color_name + ' clouded tabby'
        elif pelt.name == "Merle":
            color_name = color_name + ' merle'
        elif pelt.name == "Snowflake":
            color_name = color_name + ' snowflake'
        elif pelt.name == "Spotted":
            color_name = color_name + ' spotted tabby'

        elif pelt.name == "Tortie":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' torbie'
            else:
                color_name = color_name + ' tortie'
        elif pelt.name == "Calico":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' tabico'
            else:
                color_name = color_name + ' calico'
        # enough to comment but not make calico
        if white_patches is not None:
            if white_patches in little_white + mid_white:
                color_name = color_name + ' and white'
            # and white
            elif white_patches in high_white:
                if pelt.name != "Calico":
                    color_name = color_name + ' and white'
            # white and
            elif white_patches in mostly_white:
                color_name = 'white and ' + color_name
            # colorpoint
            elif white_patches in point_markings and pelt.name != 'Doberman':
                color_name = color_name + ' point'
                if color_name == 'dark ginger point' or color_name == 'ginger point':
                    color_name = 'flame point'
            # vitiligo
            elif white_patches in vit:
                color_name = color_name + ' with vitiligo'
        else:
            color_name = color_name

        if color_name == 'tortie':
            color_name = 'tortoiseshell'

        if white_patches == 'FULLWHITE':
            color_name = 'white'

        if color_name == 'white and white':
            color_name = 'white'
            
        if color_name == 'white2 and white':
            color_name = 'white'

        return color_name