# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from os import path
from random import randint
from numpy import array
from numpy.linalg import norm
import pygame
from pygame import Color
from pygame.mixer import Sound
from pygame.locals import *
from sys import exit

pygame.init()
clock = pygame.time.Clock()


# %%
# Other imports

# Color Constants
COLOR_BLACK: Color = Color(0, 0, 0)
COLOR_WHITE: Color = Color(255, 255, 255)

# Game Constants
CELL_SIZE: int = 40
CELL: array = array([CELL_SIZE, CELL_SIZE])


# %%
# Window

WIDTH: int = 640
HEIGHT: int = 480
SCREEN_SIZE: array = array([WIDTH, HEIGHT])
TITLE: str = "Hello PyGame World!"
FIXED_FPS: int = 60

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(TITLE)


# %%
# Vectors

# Vector Constants
VECTOR_ZERO: array = array([0, 0])
VECTOR_ONE: array = array([1.0, 1.0])
# VECTOR_RIGHT: array = array([1, 0])
# VECTOR_LEFT: array = array([-1, 0])
# VECTOR_UP: array = array([0, 1])
# VECTOR_DOWN: array = array([0, -1])


# %%
class InputEvent:

    def get_input_strength() -> array:
        is_pressed = pygame.key.get_pressed()
        keys: dict = {K_w: 0.0, K_a: 0.0, K_s: 0.0, K_d: 0.0}
        strength: array

        for key in keys:
            keys[key] = 1.0 if is_pressed[key] else 0.0

        strength = array([keys[K_d] - keys[K_a], keys[K_s] - keys[K_w]])
        strength_norm = norm(strength)

        if strength_norm:
            strength /= strength_norm

        return strength


# %%
class Entity:
    position: array
    color: pygame.Color = pygame.Color(115, 10, 46)
    scale: array = VECTOR_ONE
    anchor: array = array([.5, .5])

    class SignalNotExists(Exception):
        pass

    class Signal:
        _observers: dict = {}
        owner = None

        class NotOwner(Exception):
            '''Lançado ao tentar operar o sinal para um objeto que não a pertence'''
            pass

        class AlreadyConnected(Exception):
            '''Lançada ao tentar conectar um sinal a um mesmo observador'''
            pass

        class NotConnected(Exception):
            '''Lançado ao tentar desconectar um sinal de um objeto que não é observador'''
            pass

        # TODO -> Allow args
        def connect(self, owner, observer, method) -> None:
            if owner != self.owner:
                raise Entity.Signal.NotOwner

            if self._observers.get(observer) != None:
                raise Entity.Signal.AlreadyConnected

            self._observers[observer] = method

        def disconnect(self, owner, observer) -> None:
            if owner != self.owner:
                raise Entity.Signal.NotOwner

            if self._observers.pop(observer) == None:
                raise Entity.Signal.NotConnected

        def emit(self, *args) -> None:
            for observer in self._observers.keys():
                self._observers[observer](*args)

        def __init__(self, owner) -> None:
            self.owner = owner

    def _draw(self) -> pygame.Rect:
        target_pos: array = self.position - CELL * self.anchor

        return pygame.draw.rect(screen, self.color, (
            target_pos[0], target_pos[1], CELL_SIZE * self.scale[0], CELL_SIZE * self.scale[1]))

    def connect(self, signal, observer, method) -> None:
        try:
            signal.connect(self, observer, method)
        except Entity.Signal.NotOwner:
            raise Entity.SignalNotExists

    def disconnect(self, signal, observer, method) -> None:
        try:
            signal.disconnect(self, observer)
        except Entity.Signal.NotOwner:
            raise Entity.SignalNotExists

    def get_x(self) -> int:
        return self.position[0]

    def get_y(self) -> int:
        return self.position[1]

    def __init__(self, coords: array = VECTOR_ZERO) -> None:
        self.position = coords


# %%
class Node(Entity):

    class EmptyName(Exception):
        pass

    class InvalidChild(Exception):
        '''Lançado ao tentar adicionar um filho que já tem um pai, ou, a si mesmo'''
        pass

    class DuplicatedChild(InvalidChild):
        '''Lançado ao tentar inserir um filho de mesmo nome'''
        pass

    def add_child(self, node, at: int = -1) -> None:
        if node == self or node._parent:
            raise Entity.InvalidChild

        if self._children_refs.get(node.name, False):
            raise Node.DuplicatedChild

        if at == -1:
            self._children_index.append(node)
        else:
            self._children_index.insert(at, node)

        self._children_refs[node.name] = node
        node._parent = self

    def remove_child(self, node=None, at: int = -1):

        if not self._children_refs:
            return None

        if node == None:
            node = self._children_index.remove(at)

        return self._children_refs.pop(node.name, None)

    def get_child(self, name: str = '', at: int = -1):

        if name:
            return self._children_refs.get(name, None)
        else:
            return self._children_index[at]

    def get_parent(self):
        return self._parent

    def get_global_position(self) -> list:

        if self._parent:
            return self._parent.get_global_position() + self.position
        else:
            return self.position

    def _draw(self, parent_offset: array = VECTOR_ZERO) -> pygame.Rect:
        target_pos: array = self.position + parent_offset - CELL * self.anchor

        rect: pygame.Rect = pygame.draw.rect(screen, self.color, (
            target_pos[0], target_pos[1], CELL_SIZE * self.scale[0], CELL_SIZE * self.scale[1]))

        for child in self._children_index:
            rect.union(child._draw(target_pos))

        return rect

    def __init__(self, name: str = 'Node', coords: array = VECTOR_ZERO) -> None:
        super().__init__(coords=coords)

        if not name:
            raise Node.EmptyName

        self.name = name
        self._children_index: list = []
        self._children_refs: dict = {}
        self._parent = None


# %%
class Atlas(pygame.sprite.Sprite):
    base_size: array = array([0, 0])
    _static: bool = True
    _speed: float = 0.06
    _current_time: float = 0.0

    def update(self) -> None:

        if self._static:
            return

        self._current_time = (self._current_time +
                              self._speed) % len(self.textures)
        self._frame = int(self._current_time)
        self.__update_frame()

    def _update_frame(self) -> None:

        if self.textures:
            self.__update_frame()

    def __update_frame(self) -> None:
        self.image: pygame.Surface = self.textures[self.frame]
        self.rect = self.image.get_rect()
        self.base_size = array(self.image.get_size())

    def add_texture(self, *paths: str) -> None:

        for path in paths:
            self.textures.append(pygame.image.load(path))

        if len(self.textures) > 1:
            self._static = False

        self._update_frame()

    def set_textures(self, value: list) -> None:
        self._textures = value
        self._frame = 0
        self._update_frame()

    def get_textures(self) -> list:
        return self._textures

    def set_frame(self, value: int) -> None:

        if value > len(self._textures):
            return

        self._frame = value
        self._current_time = float(self._frame)
        self._update_frame()

    def get_frame(self) -> int:
        return self._frame

    def __init__(self) -> None:
        super().__init__()
        self._frame: int = 0
        self._textures: list = []

    frame: property = property(get_frame, set_frame)
    textures: property = property(get_textures, set_textures)


# %%
class Sprite(Node):
    atlas: Atlas = Atlas()

    def _draw(self, parent_offset: array = VECTOR_ZERO) -> pygame.Rect:
        self.atlas.image = pygame.transform.scale(
            self.atlas.image, (self.atlas.base_size * self.scale).astype('int'))

        target_pos: array = self.position + parent_offset - \
            array(self.atlas.image.get_size()) * self.anchor

        self.atlas.rect.topleft = target_pos
        rect: pygame.Rect = self.atlas.rect.copy()

        for child in self._children_index:
            rect.union(child._draw(target_pos))

        return rect


# %%
class KinematicBody(Node):
    speed: float = 1.0
    velocity: array = array([0.0, 0.0])

    def move(self) -> None:
        position: list = [self.position[0], self.position[1]]

        for i in range(2):
            position[i] += self.velocity[i] * self.speed

            if position[i] < 0.0:
                position[i] = 0.0
            elif position[i] > SCREEN_SIZE[i]:
                position[i] = SCREEN_SIZE[i]

        self.position = array(position)

    def _input(self) -> None:
        self.velocity = InputEvent.get_input_strength()

    # def _input_event(self, event: InputEvent) -> None:
    #     pass

    def __init__(self, name: str = 'KinematicBody', coords: array = VECTOR_ZERO,
                 color: Color = Color(46, 10, 115)) -> None:
        super().__init__(name, coords=coords)
        self.color = color


# %%
class Label(Entity):
    font: pygame.font.Font = pygame.font.SysFont('roboto', 40, False, False)
    text: str = ''

    def set_text(self, value: str) -> None:
        self.text = value

    def _draw(self):
        return self.font.render(self.text, True, self.color)

    def __init__(self, coords: array = VECTOR_ZERO, color: Color = COLOR_WHITE) -> None:
        super().__init__(coords=coords)
        self.color = color


# %%
class Player(KinematicBody):
    points_changed: Entity.Signal

    def set_points(self, value) -> None:
        self._points = value
        self.points_changed.emit(f'Points: {value}')

    def get_points(self) -> None:
        return self._points

    def __init__(self, name: str = 'Player', coords: tuple = VECTOR_ZERO,
                 color: Color = (15, 92, 105)) -> None:
        super().__init__(name, coords=coords, color=color)
        self._points: int = 0
        self.points_changed = Entity.Signal(self)

    points: property = property(get_points, set_points)


# %%
# Loading Resources
ASSETS_DIR: str = 'assets'
SPRITES_DIR: str = path.join(ASSETS_DIR, 'sprites')
SOUNDS_DIR: str = path.join(ASSETS_DIR, 'sounds')
SPRITES_SCALE: array = array([2, 2])

# Sprites
player_sprite: Sprite = Sprite()
player_sprite.atlas.add_texture(path.join(SPRITES_DIR, 'dino.png'))

sprites: pygame.sprite.Group = pygame.sprite.Group()
sprites.add(player_sprite.atlas)
player_sprite.scale = SPRITES_SCALE

# Sound Streams
death_sfx: Sound = Sound(path.join(SOUNDS_DIR, 'death.wav'))
jump_sfx: Sound = Sound(path.join(SOUNDS_DIR, 'jump.wav'))
score_sfx: Sound = Sound(path.join(SOUNDS_DIR, 'score.wav'))


# %%
# Entities
player: Player = Player(coords=(WIDTH // 2, HEIGHT // 2))
entity: Entity = Entity((randint(0, WIDTH), randint(0, HEIGHT)))
label: Label = Label((450, 40))

label.text = 'Points: 0'
label.color = COLOR_BLACK
player.connect(player.points_changed, label, label.set_text)
player.add_child(player_sprite)
# bg_mirror_pos: array = (bg.get_width(), 0)

while True:
    clock.tick(FIXED_FPS)
    screen.fill(COLOR_WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#         if event.type == KEYDOWN:
#             keys: list = [K_w, K_a, K_s, K_d]
#
#             for key in keys:
#                 if event.key == key:
#                     player._input_event(
#                         InputEvent.InputTypes.JUST_PRESSED, key)

    player._input()
    player.move()
    body_aabb = player._draw()
    entity_aabb = entity._draw()
    sprites.draw(screen)
    sprites.update()
    screen.blit(label._draw(), label.position)

    if body_aabb.colliderect(entity_aabb):
        entity.position = (randint(0, WIDTH), randint(0, HEIGHT))
        player.points += 1
        score_sfx.play()

    pygame.display.update()
