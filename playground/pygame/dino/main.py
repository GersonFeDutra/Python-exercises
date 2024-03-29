# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from typing import Callable
from numpy.lib.type_check import _is_type_dispatcher
import pygame
from pygame import Color
from pygame import Surface
from pygame import sprite
from pygame.mixer import Sound
from pygame.locals import *
from sys import exit, argv

# %%
# Other imports
import warnings
from os import path
from random import randint, randrange, choice
from enum import IntEnum
from numpy import array
from numpy.linalg import norm
from collections import deque

pygame.init()
clock = pygame.time.Clock()
IS_DEBUG_ENABLED: bool = '-t' in argv
IS_DEV_MODE_ENABLED: bool = IS_DEBUG_ENABLED and '-d' in argv

# %%

# Color Constants
COLOR_BLACK: Color = Color(0, 0, 0)
COLOR_WHITE: Color = Color(255, 255, 255)
COLOR_RED: Color = Color(255, 0, 0)
COLOR_GREEN: Color = Color(0, 255, 0)
COLOR_BLUE: Color = Color(0, 0, 255)

# Game Constants
CELL_SIZE: int = 32
CELL: tuple = CELL_SIZE, CELL_SIZE

# Tools
GIZMO_RADIUS: int = 2


# %%
# Window

WIDTH: int = 640
HEIGHT: int = 480
SCREEN_SIZE: tuple[int, int] = WIDTH, HEIGHT
TITLE: str = "Hello PyGame World!"
FIXED_FPS: int = 60

screen = pygame.display.set_mode(SCREEN_SIZE)
#alpha_layer = Surface(SCREEN_SIZE, pygame.SRCALPHA)
pygame.display.set_caption(TITLE)


# %%
# Vectors

# Vector Constants
VECTOR_ZERO: tuple[float, float] = 0., 0.
VECTOR_ONE: tuple[float, float] = 1., 1.
# VECTOR_RIGHT: tuple = 1, 0
# VECTOR_LEFT: tuple = -1, 0
# VECTOR_UP: tuple = 0, 1
# VECTOR_DOWN: tuple = 0, -1

# AnchorS
TOP_LEFT: tuple[float, float] = 0., 0.
BOTTOM_RIGHT: tuple[float, float] = 1., 1.
CENTER: tuple[float, float] = .5, .5
CENTER_LEFT: tuple[float, float] = .5, 0.

# Coords aliases
X: int = 0
Y: int = 1

# %%
# Global Helper "Static" Methods


def lerp(_from_: float, _to_: float, _delta_: float) -> float:
    '''Realiza uma interpolação linear de `_from_` para `_to_` em termos de `_delta_`.'''
    return (_from_ - _to_) * _delta_


def draw_bounds(target_pos: array, extents: array, anchor: array, color: Color, fill=False) -> None:
    minor: array = target_pos - extents * anchor
    major: array = target_pos + extents * (1.0 - anchor)
    points: tuple = (
        (minor[X], minor[Y]), (major[X], minor[Y]
                               ), (major[X], major[Y]), (minor[X], major[Y])
    )

    # TODO -> Permitir alpha
    if fill:
        pygame.draw.polygon(screen, color, points)
    else:
        for i in range(4):
            pygame.draw.line(screen, color, points[i], points[(i + 1) % 4])


# %%
class InputEvent:
    '''Data-Class usada como registro de um evento de entrada no sistema do jogo.'''
    input_type: int
    key: int
    tag: str
    target: object

    def __init__(self, input_type: int, key: int, tag: str, target) -> None:
        self.type = input_type
        self.key = key
        self.tag = tag
        self.target = target


# %%
class Entity:
    '''Entidade básica do jogo, que contém informações de espaço (2D).'''
    position: array
    color: Color
    scale: array
    anchor: array

    class SignalNotExists(Exception):
        pass

    class Signal:
        '''Classe responsável por gerenciar o envio de "eventos"/ "mensagens" entre nós.
        Baseado no padrão do observador, inspirado na sua implementação no motor Godot.'''
        owner = None
        name: str  # Metadata # Apenas para auxiliar no debug

        class NotOwner(Exception):
            '''Lançado ao tentar operar o sinal para um objeto que não a pertence'''
            pass

        class AlreadyConnected(Exception):
            '''Lançada ao tentar conectar um sinal a um mesmo observador'''
            pass

        class NotConnected(Exception):
            '''Lançado ao tentar desconectar um sinal de um objeto que não é observador'''
            pass

        # Permitir kwargs?
        def connect(self, owner, observer, method: Callable, *args) -> None:
            '''Conecta o sinal ao método indicado. O mesmo será chamado quando o nó for emitido.'''
            if owner != self.owner:
                raise Entity.Signal.NotOwner

            if self._observers.get(observer) != None:
                raise Entity.Signal.AlreadyConnected

            self._observers[observer] = (method, args)

        def disconnect(self, owner, observer) -> None:
            '''Desconecta o método pertencente ao nó indicado desse sinal.'''
            if owner != self.owner:
                raise Entity.Signal.NotOwner

            if self._observers.pop(observer) == None:
                raise Entity.Signal.NotConnected

        def emit(self, *args) -> None:
            '''Emite o sinal, propagando chamadas aos métodos conectados.
            Os argumentos passados para as funções conectadas são, respectivamente:
            os argumentos passados ao conectar a função, em seguida,
            os argumentos passados na emissão.'''

            for observer, data in self._observers.items():
                data[0](*(data[1] + args))

        def __init__(self, owner, name: str) -> None:
            self.owner = owner
            self.name = name
            self._observers: dict[Node, tuple[Callable, ]] = {}

    def _draw(self, target_pos: tuple[int, int] = None, target_scale: tuple[float, float] = None,
              offset: tuple[int, int] = None) -> None:
        '''Atualiza as pinturas na tela.
        Recebe uma posição, escala e deslocamento pré-calculados.'''

        if not IS_DEBUG_ENABLED:
            return

        cell: array = self.get_cell()

        if target_pos is None:
            target_pos = self.position

        if target_scale is None:
            target_scale = self.scale

        # Desenha o Gizmo
        extents: array = GIZMO_RADIUS * target_scale
        pygame.draw.line(screen, self.color,
                         (target_pos[X] - extents[X], target_pos[Y]),
                         (target_pos[X] + extents[X], target_pos[Y]))
        pygame.draw.line(screen, self.color,
                         (target_pos[X], target_pos[Y] - extents[Y]),
                         (target_pos[X], target_pos[Y] + extents[Y]))

        if cell[X] != 0 or cell[Y] != 0:
            # Desenha as bordas da caixa delimitadora
            extents = cell * target_scale

            anchor: array = array(self.anchor)
            draw_bounds(target_pos, extents, anchor, self.color,
                        fill=self._debug_fill_bounds)

    def set_cell(self, value: tuple[int, int]) -> None:
        '''Método virtual para determinar um tamanho/ espaço customizado para a célula.'''
        return

    def get_cell(self) -> tuple[int, int]:
        '''Retorna o tamanho/espaço da célula que envolve o nó.'''
        return VECTOR_ZERO

    def connect(self, signal, observer, method, *args) -> None:
        '''Realiza a conexão de um sinal que pertence ao nó.'''
        try:
            signal.connect(self, observer, method, *args)
        except Entity.Signal.NotOwner:
            raise Entity.SignalNotExists

    def disconnect(self, signal, observer) -> None:
        '''Desconecta um sinal pertencente ao nó.'''
        try:
            signal.disconnect(self, observer)
        except Entity.Signal.NotOwner:
            raise Entity.SignalNotExists

    def get_x(self) -> int:
        return self.position[X]

    def get_y(self) -> int:
        return self.position[Y]

    def __init__(self, coords: tuple[int, int] = VECTOR_ZERO) -> None:
        self.position = array(coords)
        self.scale = array(VECTOR_ONE)
        self.anchor = array(CENTER)
        self.color = Color(0, 185, 225, 125)
        self._debug_fill_bounds: bool = False


# %%
class Node(Entity):
    '''Classe fundamental que representa um objeto quaisquer do jogo.
    Permite a composição desses objetos em uma estrutura de árvore.
    Sua principal vantagem é a propagação de ações e eventos.'''

    class PauseModes(IntEnum):
        '''Bit-flags para verificação do modo de parada no processamento da árvore.'''
        # Flag para alterar o processamento da árvore (1 == em pausa, 0 == ativo).
        TREE_PAUSED: int = 1
        STOP: int = 2  # Interrompe o processamento do nó e seus filhos
        # Interrompe o processamento do nó, mas continua processando os filhos.
        CONTINUE: int = 4
        IGNORE: int = 8  # Mantém o processando o nó.

    pause_mode: int = PauseModes.IGNORE

    class EmptyName(Exception):
        pass

    class InvalidChild(Exception):
        '''Lançado ao tentar adicionar um filho que já tem um pai, ou, a si mesmo'''
        pass

    class DuplicatedChild(InvalidChild):
        '''Lançado ao tentar inserir um filho de mesmo nome'''
        pass

    def add_child(self, node, at: int = -1) -> None:
        '''Registra um nó na árvore como filho do nó atual.'''
        if node == self or node._parent:
            raise Node.InvalidChild

        if self._children_refs.get(node.name, False):
            raise Node.DuplicatedChild

        if at == -1:
            self._children_index.append(node)
        else:
            self._children_index.insert(at, node)

        self._children_refs[node.name] = node
        node._parent = self

        if self._is_on_tree:
            node._enter_tree()

    def remove_child(self, node=None, at: int = -1):
        '''Remove os registros do nó, se for filho.'''

        if not self._children_refs:
            return None

        if node == None:
            node = self._children_index.pop(at)
        else:
            self._children_index.remove(node)

        node = self._children_refs.pop(node.name, None)
        node._parent = None

        if self._is_on_tree:
            node._exit_tree()

        return node

    def toggle_process(self) -> None:
        self.pause_mode = self.pause_mode ^ Node.PauseModes.TREE_PAUSED

    def pause(self, do_pause: bool = False) -> None:

        if do_pause:
            # Adiciona a flag de pausa, se já não inserida.
            self.pause_mode = self.pause_mode | Node.PauseModes.TREE_PAUSED
        else:
            # Remove a flag de pausa, se estiver inserida.
            self.pause_mode = self.pause_mode & ~Node.PauseModes.TREE_PAUSED

    def get_child(self, name: str = '', at: int = -1):
        '''Busca um nó filho, por nome ou índice.'''

        if name:
            return self._children_refs.get(name, None)
        else:
            return self._children_index[at]

    def get_parent(self):
        return self._parent

    def get_global_position(self) -> list:
        '''Calcula a posição do nó, considerando a hierarquia
        (posições relativas aos nós ancestrais.'''

        if self._parent:
            return self._parent.get_global_position() + self.position
        else:
            return self.position

    # def _parent

    def _enter_tree(self) -> None:
        '''Método virtual que é chamado logo após o nó ser inserido a árvore.
        Chamado após este nó ou algum antecedente ser inserido como filho de outro nó na árvore.'''
        self._is_on_tree = True

        for child in self._children_index:
            child._enter_tree()

    def _exit_tree(self) -> None:
        '''Método virtual que é chamado logo após o nó ser removido da árvore.
        Chamado após este nó ou algum antecedente ser removido de outro nó na árvore.'''
        self._is_on_tree = False

        for child in self._children_index:
            child._exit_tree()

    def _draw(self, target_pos: tuple[int, int], target_scale: tuple[float, float],
              offset: tuple[int, int]) -> None:
        '''Método virtual chamado no passo de renderização dos nós.
        Os argumentos passados são: a posição global do objeto, a escala global,
        e o deslocamento na célula (sobre seu ponto de ancoragem).'''
        super()._draw(target_pos, target_scale, offset)

    def _input(self) -> None:
        '''Método virtual chamado no passo de captura de entradas dos nós.'''
        pass

    def _input_event(self, event: InputEvent) -> None:
        '''Método virtual chamado quando um determinado evento de entrada ocorrer.'''
        pass

    def _propagate(self, parent_offset: array = array(VECTOR_ZERO),
                   parent_scale: array = array(VECTOR_ONE), tree_pause: int = 0):
        '''Propaga os métodos virtuais na hierarquia da árvore, da seguinte forma:
        Primeiro as entradas são tomadas e então os desenhos são renderizados na tela.
        Logo em seguida, após a propagação nos filhos, o método `_process` é executado.'''
        global root

        target_scale: array = self.scale * parent_scale
        target_pos: array = self.position + parent_offset
        offset: array = self.get_cell() * target_scale * self.anchor
        physics_helper: PhysicsHelper = PhysicsHelper(self)

        self._input()
        self._draw(target_pos, target_scale, offset)

        tree_pause = tree_pause | root.tree_pause | self.pause_mode
        self._subpropagate(target_pos, target_scale,
                           physics_helper.children, tree_pause)

        if not (tree_pause & Node.PauseModes.STOP or
                tree_pause & Node.PauseModes.TREE_PAUSED
                and not(self.pause_mode & Node.PauseModes.CONTINUE)):

            self._process()

        return physics_helper.check_collisions()

    def _subpropagate(self, target_pos: array, target_scale: array,
                      physics_helpers: deque, tree_pause: int) -> None:
        '''Método auxiliar para propagar métodos virtuais nos nós filhos.'''

        for child in self._children_index:
            physics_helpers.append(child._propagate(target_pos, target_scale))

    def _process(self):
        '''Método virtual para processamento de dados em cada passo/ frame.'''
        pass

    def __init__(self, name: str = 'Node', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(coords=coords)

        if not name:
            raise Node.EmptyName

        self.name: str = name
        self._is_on_tree: bool = False
        self._children_index: list[Node] = []
        self._children_refs: dict[str, Node] = {}
        self._parent: Node = None
        self._current_groups: list[str] = []


# %%
class Input:
    '''Classe responsável por gerenciar eventos de entrada.'''
    _instance = None
    events: dict = {}

    class NotANode(Exception):
        '''Lançado ao tentar registrar um evento em um objeto que não e do tipo `Node`.'''
        pass

    def register_event(self, to: Node, input_type: int, key: int, tag: str = "") -> None:

        if not isinstance(to, Node):
            raise Input.NotANode

        event_type: dict = self.events.get(input_type)
        if not event_type:
            event_type = {}
            self.events[input_type] = event_type

        event_key: list = event_type.get(key)
        if not event_key:
            event_key = []
            event_type[key] = event_key

        event_key.append(InputEvent(input_type, key, tag, to))

    def get_input_strength() -> array:
        '''Método auxiliar para calcular um input axial.'''
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

    def _tick(self) -> None:
        '''Passo de captura dos inputs, convertendo-os em eventos.'''

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            event_type: dict = self.events.get(event.type, False)
            if not event_type:
                continue

            event_key: list = event_type.get(event.key)
            if not event_key:
                continue

            for event in event_key:
                node: Node = event.target
                node._input_event(event)

    def __new__(cls):
        # Torna a classe em uma Singleton
        if cls._instance is None:
            # Criação do objeto
            cls._instance = super(Input, cls).__new__(cls)

        return cls._instance


# %%
class Atlas(sprite.Sprite):
    '''Classe do PyGame responsável por gerenciar sprites e suas texturas.'''
    base_size: array
    is_paused: bool = False
    _static: bool = True
    _speed: float = 0.06
    _current_time: float = 0.0

    def update(self) -> None:
        '''Processamento dos quadros da animação.'''

        if self._static or self.is_paused:
            return

        self._current_time = (self._current_time +
                              self._speed) % len(self.textures)
        self._frame = int(self._current_time)
        self.__update_frame()

    def _update_frame(self) -> None:
        '''Método auxiliar para atualização dos quadros.'''

        if self.textures:
            self.__update_frame()

    def __update_frame(self) -> None:
        ''''Atualiza um frame da animação.'''
        self.image: Surface = self.textures[self.frame]
        self.rect = self.image.get_rect()
        self.base_size = array(self.image.get_size())

    def add_texture(self, *paths: str) -> None:
        '''Adciona uma textura ao atlas.'''

        for path in paths:
            self.textures.append(pygame.image.load(path))

        if len(self.textures) > 1:
            self._static = False

        self._update_frame()

    def add_spritesheet(self, texture: Surface, h_slice: int = 1, v_slice: int = 1,
                        coords: tuple[int, int] = VECTOR_ZERO,
                        sprite_size: tuple[int, int] = None) -> None:
        '''Realiza o fatiamento da textura de uma spritesheet como sprites de uma animação.'''

        if sprite_size is None:
            sprite_size = (texture.get_width() / h_slice,
                           texture.get_height() / v_slice)

        for i in range(h_slice):
            for j in range(v_slice):
                self.textures.append(texture.subsurface(
                    array(coords) + (i, j) * array(sprite_size), sprite_size))

            if len(self.textures) > 1:
                self._static = False

            self._update_frame()

    def load_spritesheet(self, path: str, h_slice: int = 1, v_slice: int = 1,
                         coords: tuple[int, int] = VECTOR_ZERO,
                         sprite_size: tuple[int, int] = None) -> None:
        '''Faz o carregamento de uma textura como uma spritesheet, com o devido fatiamento.'''
        self.add_spritesheet(pygame.image.load(
            path), h_slice=h_slice, v_slice=v_slice, coords=coords, sprite_size=sprite_size)

    def set_textures(self, value: list) -> None:
        self._textures = value
        self._frame = 0
        self._static = len(self._textures) <= 1
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
        self.base_size = array([0, 0])

    frame: property = property(get_frame, set_frame)
    textures: property = property(get_textures, set_textures)


# %%
class Sprite(Node):
    '''Nó que configura um sprite do Pygame como um objeto de jogo
    (que pode ser inserido na árvore da cena).'''
    atlas: Atlas
    group: str

    def _enter_tree(self) -> None:
        sprites_groups[self.group].add(self.atlas)
        super()._enter_tree()

    def _exit_tree(self) -> None:
        sprites_groups[self.group].remove(self.atlas)
        super()._exit_tree()

    def _draw(self, target_pos: tuple[int, int], target_scale: tuple[float, float],
              offset: tuple[int, int]) -> None:
        super()._draw(target_pos, target_scale, offset)

        # REFACTOR -> Fazer as transforms serem recalculadas _JIT_ (Just In Time).
        self.atlas.image = pygame.transform.scale(
            self.atlas.image, (self.atlas.base_size * target_scale).astype('int'))
        self.atlas.rect.topleft = array(target_pos) - offset

    def get_cell(self) -> array:
        return array(self.atlas.base_size)

    def __init__(self, name: str = 'Sprite', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        global DEFAULT_GROUP
        super().__init__(name=name, coords=coords)

        self.atlas = Atlas()
        self.group = DEFAULT_GROUP


# %%
# TODO -> Make Parallax Background using Surfaces
'''
class ParallaxBackground(Node):
    offset: array
    distance: float = 1.0

    def _process(self):
        self.offset[0] = self.offset[0] + self.distance

    def _subpropagate(self, target_pos: array, target_scale: array, rect: pygame.Rect, children_data: list[dict]):
        return super()._subpropagate(target_pos, target_scale, rect, children_data)

    def __init__(self, name: str = 'Node', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)
        self.offset = array([0.0, 0.0])
'''

# %%


class Shape(Node):
    '''Nó que representa uma forma usada em cálculos de colisão.
    Deve ser adicionada como filha de um `KinematicBody`.'''
    rect_changed: Entity.Signal
    base_size: array([int, int])

    class CollisionType(IntEnum):
        PHYSICS = 1  # Área usada para detecção de colisão entre corpos
        AREA = 2  # Área usada para mapeamento (renderização, ou localização).

    type: int = CollisionType.PHYSICS

    def _draw(self, target_pos: tuple[int, int], target_scale: tuple[float, float],
              offset: tuple[int, int]) -> None:
        super()._draw(target_pos, target_scale, offset)
        self._rect.size = self.base_size * target_scale
        self._rect.topleft = array(target_pos) - offset

    def get_cell(self) -> array:
        return array(self.base_size)

    def set_rect(self, value: Rect) -> None:
        self.base_size = array(value.size)
        self._rect = value
        self.rect_changed.emit(self)

    def get_rect(self) -> Rect:
        return self._rect

    def bounds(self) -> Rect:
        '''Retorna a caixa delimitadora da forma.'''
        return self._rect

    def __init__(self, name: str = 'Shape', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)
        self._rect: Rect = None
        self.rect_changed = Entity.Signal(self, 'rect_changed')
        self._debug_fill_bounds = True

    rect: property = property(get_rect, set_rect)


# %%
class VisibilityNotifier(Shape):
    SCREEN_RECT: Rect = Rect(VECTOR_ZERO, SCREEN_SIZE)
    screen_entered: Node.Signal
    screen_exited: Node.Signal
    is_on_screen: bool = None

    def _draw(self, target_pos: tuple[int, int],
              target_scale: tuple[float, float], offset: tuple[int, int]) -> None:
        super()._draw(target_pos, target_scale, offset)
        is_colliding: bool = self._rect.colliderect(
            VisibilityNotifier.SCREEN_RECT)

        if is_colliding != self.is_on_screen:
            self._shift(is_colliding)

    def shift_on_screen(self, _to: bool = None) -> None:

        if self.is_on_screen:
            self.screen_exited.emit()
        else:
            self.screen_entered.emit()

        self.is_on_screen = not self.is_on_screen

    def set_on_screen(self, to: bool = None) -> None:
        self.is_on_screen = to
        self._shift = self.shift_on_screen

    def __init__(self, name: str = 'VisibilityNotifier',
                 coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)
        self.type = Shape.CollisionType.AREA
        self.color = Color(118, 10, 201)

        self.screen_exited = Node.Signal(self, 'screen_exited')
        self.screen_entered = Node.Signal(self, 'screen_entered')
        self._was_draw_once: bool = False
        self._shift: Callable = self.set_on_screen


# %%
class KinematicBody(Node):
    '''Nó com capacidades físicas (permite colisão).'''
    collided: Entity.Signal

    def add_child(self, node: Node, at: int = -1) -> None:
        super().add_child(node, at=at)

        if isinstance(node, Shape) and node.type & Shape.CollisionType.PHYSICS:
            self._on_Shape_rect_changed(node)
            node.connect(node.rect_changed, self, self._on_Shape_rect_changed)

    def remove_child(self, node=None, at: int = -1):
        super().remove_child(node=node, at=at)

        if node is Shape:
            self._on_Shape_rect_changed(node)
            node.disconnect(node.rect_changed, self,
                            self._on_Shape_rect_changed)

    def _enter_tree(self) -> None:
        super()._enter_tree()

        if not self.has_shape():
            warnings.warn(
                "A `Shape` node must be added as a child to process collisions.", category=Warning)

    def _process(self) -> None:
        self._physics_process()

    def _physics_process(self) -> None:
        pass

    def _on_Shape_rect_changed(self, _shape: Shape) -> None:

        if _shape.bounds():
            self._active_shapes.append(_shape)
            self._was_shapes_changed = True

    # def _expand_bounds(self, with_shape: Rect) -> None:
    #     '''Método auxiliar para expandir a caixa delimitadora desse corpo físico.'''
    #
    #     if self._bounds:
    #         self._bounds = self._bounds.union(with_shape)

    def has_shape(self) -> bool:
        return bool(self._active_shapes)

    def is_colliding(self, target) -> bool:
        ''''Verifica colisões com o corpo indicado.'''

        for a in self._active_shapes:
            for b in target._active_shapes:
                if a.rect.colliderect(b.rect):
                    return True

        return False

    def bounds(self) -> Rect:
        '''Retorna a caixa delimitadora do corpo.'''

        if self._was_shapes_changed:
            self._cached_bounds = None
            self._was_shapes_changed = False

        if self._cached_bounds:
            return self._cached_bounds

        elif self._active_shapes:
            # Calcula novas fronteiras
            self._cached_bounds = self._active_shapes[0].rect

            for shape in self._active_shapes[1:]:
                self._cached_bounds.union(shape.bounds())

        return self._cached_bounds

    def __init__(self, name: str = 'KinematicBody', coords: tuple[int, int] = VECTOR_ZERO,
                 color: Color = Color(46, 10, 115)) -> None:
        super().__init__(name, coords=coords)
        self.color = color
        self.collided = Entity.Signal(self, 'collided')
        self._active_shapes: list[Shape] = []

        self._bounds: Rect = None

        self._was_shapes_changed: False
        self._cached_bounds: Rect = None


# %%
class Label(Node):
    '''Nó usado para apresentar texto na tela.'''
    font: pygame.font.Font = pygame.font.SysFont('roboto', 40, False, False)

    def set_text(self, value: str) -> None:
        self._text = value
        self._surface = self.update_surface

    def get_text(self) -> None:
        return self._text

    def get_surface(self) -> Surface:
        return self._current_surface

    def update_surface(self) -> Surface:
        self._current_surface = self.font.render(self.text, True, self.color)
        self._surface = self.get_surface

        return self._current_surface

    def _draw(self, target_pos: tuple[int, int] = None, target_scale: tuple[float, float] = None,
              offset: tuple[int, int] = None) -> None:
        global render_queue

        super()._draw(target_pos, target_scale, offset)
        render_queue.append(
            (self._surface(), target_pos - offset))

    def get_cell(self) -> tuple[int, int]:
        return self._surface().get_size()

    def __init__(self, name: str = 'Label', coords: tuple[int, int] = VECTOR_ZERO,
                 color: Color = COLOR_WHITE, text: str = '') -> None:
        super().__init__(name=name, coords=coords)
        self.color = color
        self.anchor = array(TOP_LEFT)

        self._current_surface: Surface
        self._surface: Callable = self.update_surface
        self._text: str
        self.set_text(text)

    text: property = property(get_text, set_text)


# %%
class PhysicsHelper():
    '''Objeto responsável pelo tratamento de colisões entre corpos físicos.'''
    _container_type: int = 0
    rect: Rect = None
    head: Node
    children = None

    class ContainerTypes(IntEnum):
        '''Enum para classificação dos nós entre contêineres ou corpos.'''
        EMPTY = 0  # Sem conteúdo
        SOLID = 1  # Corpo físico
        SHELL = 2  # Não é um corpo físico, mas contém filhos que o são

    def __init__(self, head: Node) -> None:
        self.head = head
        helper: PhysicsHelper = self
        self.children: deque[PhysicsHelper] = deque()

    def check_collisions(self):
        '''Verifica as colisões entre nós colisores. Retorna um auxiliar para permitir a construção
        de contêineres delimitadores em formato de árvore.'''
        is_solid: bool = isinstance(
            self.head, KinematicBody) and self.head.has_shape()
        self._container_type = int(is_solid)

        content: list = []  # Estrutura auxiliar para indexar os elementos posteriormente
        content_n: int = 0  # Quantidade de elementos do contêiner
        # Contêiner que armazenará nós colisores e outros contêineres
        container: PhysicsHelper = PhysicsHelper(self.head)
        # um contêiner é uma "casca/ invólucro" quando comporta elementos (nó interno ou raiz).
        container._container_type = PhysicsHelper.ContainerTypes.SHELL

        def non_empty(c: PhysicsHelper) -> Rect:
            '''O corpo/ contêiner é adicionado à fila do novo contêiner.
            retorna seu colisor/ caixa delimitadora, respectivamente.'''
            nonlocal content, content_n, container

            content.append(c)
            container.children.append(c)
            content_n += 1

            return c.rect

        # def empty(c: PhysicsHelper) -> None:
        #     return None

        _match: dict[int, Callable[[PhysicsHelper], Rect]] = {
            # Nada será feito, o conteúdo se perde.
            PhysicsHelper.ContainerTypes.EMPTY: lambda c: None,
            PhysicsHelper.ContainerTypes.SOLID: non_empty,
            PhysicsHelper.ContainerTypes.SHELL: non_empty,
        }

        if is_solid:
            # Se for sólido, se adiciona no topo da fila (para mantê-lo como uma folha na árvore).
            self.rect = self.head.bounds()
            container.rect = non_empty(self)

        while self.children and not container.rect:
            # Busca o primeiro nó para iniciar a caixa delimitadora do contêiner.
            child: PhysicsHelper = self.children.popleft()
            container.rect = _match[child._container_type](child)

        while self.children:
            # Adiciona os nós restantes.
            child: PhysicsHelper = self.children.popleft()
            rect: Rect = _match[child._container_type](child)

            if rect:
                container.rect = container.rect.union(rect)

        # Finaliza a configuração da raiz.
        if content_n > 1:
            # Verifica colisões nos filhos
            PhysicsHelper._check_collisions(container.children, content_n)
        elif content_n == 1:
            # Caso o contêiner tenha apenas um elemento, este não será necessário.
            container = container.children[0]
        else:
            # Retornará a si mesmo (um contêiner vazio).
            # Note que jamais será sólido pois, se assim fosse, teria sido adicionado no contêiner
            # e o bloco acima seria aplicada.
            container = self

        return container

    @staticmethod
    def _check_collisions(helpers: list, helpers_n: int) -> None:
        '''Algoritmo iterativo que checa as colisões nos filhos do nó passado.
        Sempre em direção às folhas.'''
        next_children: deque[dict[str, list]] = deque()

        # Verifica as combinações de elementos.
        for i in range(helpers_n):
            for j in range(i + 1, helpers_n):
                PhysicsHelper._check_collision(
                    helpers[i], helpers[j], next_children)

        while next_children:
            next: dict = next_children.popleft()

            for a in next['a']:
                for b in next['b']:
                    PhysicsHelper._check_collision(a, b, next_children)

    @staticmethod
    def _check_collision(a, b, next_children: deque[dict[str, list]]) -> None:
        '''Função auxiliar que verifica a colisão entre nós
        (verifica intersecção dos colisores dos contêineres aos corpos físicos).'''

        if a.rect.colliderect(b.rect):
            is_all_leaf: bool = True

            # Se o nó tiver filhos, fazemos a verificação entre eles e o outro nó colisor.
            if a.children:
                next_children.append({
                    'a': a.children,
                    'b': [b],
                })
                is_all_leaf = False

            elif b.children:
                next_children.append({
                    'a': [a],
                    'b': b.children
                })
                is_all_leaf = False

            if is_all_leaf:
                node_a: KinematicBody = a.head
                node_b: KinematicBody = b.head

                # Quando houver colisão nas folhas, o sinal `collided` é emitido para cada colisor.
                if node_a.is_colliding(node_b):
                    node_a.collided.emit(node_b)
                    node_b.collided.emit(node_a)


# %%
# root
class SceneTree(Node):
    '''Nó singleton usado como a rais da árvore da cena.
    Definido dessa forma para facilitar acessos globais.'''
    pause_toggled: Node.Signal

    _instance = None
    tree_pause: int = 0
    groups: dict[str, list[Node]] = {}

    class AlreadyInGroup(Exception):
        '''Chamado ao tentar adicionar o nó a um grupo ao qual já pertence.'''
        pass

    def pause_tree(self, pause_mode: int = Node.PauseModes.TREE_PAUSED) -> None:
        self.tree_pause = pause_mode
        self.pause_toggled.emit(
            bool((pause_mode ^ self.pause_mode) & Node.PauseModes.TREE_PAUSED))

    def add_to_group(self, node: Node, group: str) -> None:
        '''Adciona o nó a um grupo determinado.
        Se o grupo não existir, cria um novo.'''

        if node in node._current_groups:
            raise SceneTree.AlreadyInGroup

        nodes: list[Node] = self.groups.get(group)  # Stack

        if nodes:
            nodes.append(node)
        else:
            self.groups[group] = [node]

        node._current_groups.append(group)

    def remove_from_group(self, node: Node, group: str) -> None:
        '''Remove o nó do grupo determinado.
        Remove o grupo, caso o nó seja o único elemento deste.'''
        nodes: dict[Node, ] = self.groups.get(group)

        if nodes:
            nodes.pop(node, None)  # Remove silenciosamente

    def call_group(self, group: str, method_name: str, *args) -> deque[tuple[Node, ]]:
        '''Faz uma chamada de método em todos os nós pertencentes a um determinado grupo.
        Retorna uma fila de tuplas com os respectivos nós e seus retornos.'''
        queue: deque[tuple[Node, ]] = deque()

        for node in self.groups.get(group, ()).keys():
            deque.append((node, getattr(node, method_name)(*args)))

        return queue

    def is_on_group(self, node: Node, group: str) -> bool:
        '''Verifica se o nó pertence a um grupo determinado.'''
        return group in node._current_groups

    def __new__(cls):
        # Torna a classe em uma Singleton
        if cls._instance is None:
            # Criação do objeto
            cls._instance = super(SceneTree, cls).__new__(cls)

        return cls._instance

    def __init__(self, name: str = 'root', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)

        self._is_on_tree = True

        # Events
        self.pause_toggled = Node.Signal(self, 'pause_toggled')


# %%
# Game Nodes
class Player(KinematicBody):
    '''Objeto único de jogo. É o ator/ personagem principal controlado pelo jogador.'''
    JUMP: str = "jump"
    GRAVITY: float = 0.1

    points_changed: Entity.Signal
    scored: Entity.Signal
    died: Entity.Signal

    _velocity: array
    _jump_strength: float = 0.0
    _floor: float
    _start_position: tuple[int, int]

    was_collided: bool = False
    speed: float = 1.0
    jump_force: float = 5.0
    sprite: Sprite

    def _process(self) -> None:
        global score_sfx

        self.points += 1

        if self.points % 500 == 0:
            score_sfx.play()
            self.scored.emit()

        super()._process()

    def _physics_process(self) -> None:
        self._move_()

    def _move(self) -> None:
        self.position = array(
            [self._run(self.position[X]), self._jump(self.position[Y])], dtype=int)

    def _float(self) -> None:
        position: list = [self.position[0], self.position[1]]

        for i in range(2):
            position[i] += self._velocity[i] * self.speed

            if position[i] < 0.0:
                position[i] = 0.0
            elif position[i] > SCREEN_SIZE[i]:
                position[i] = SCREEN_SIZE[i]

        self.position = array(position)

    def _run(self, x: float) -> float:
        x += self._velocity[X] * self.speed

        if x < 0.0:
            x = 0.0
        elif x > SCREEN_SIZE[X]:
            x = SCREEN_SIZE[X]

        return x

    def _jump(self, y: float) -> float:

        if y < self._floor:
            # Aplicação da gravidade quando não está no chão
            self._velocity[Y] -= self.GRAVITY

        y = min((y - self._velocity[Y], self._floor))
        self._velocity[Y] += self._jump_strength * 0.1

        if self._jump_strength > 0.0:
            self._jump_strength = max((self._jump_strength - lerp(
                self._jump_strength, 0.0, self.GRAVITY), 0.0))

            if self._jump_strength < 0.2:
                self._jump_strength = 0.0

        return y

    def _input(self) -> None:
        self._apply_velocity_()

    def _apply_x_velocity(self) -> None:
        self._velocity[X] = Input.get_input_strength()[0]

    def _apply_xy_velocity(self) -> None:
        self._velocity = Input.get_input_strength()

    def _input_event(self, event: InputEvent) -> None:

        if event.tag is self.JUMP and self.position[Y] >= self._floor:
            # Reseta a velocidade com o impulso do pulo
            self._velocity[Y] -= self._velocity[Y]
            self._jump_strength = self.jump_force

    def _on_Body_collided(self, body: KinematicBody) -> None:
        global root, death_sfx, ENEMY_GROUP

        if self.was_collided:
            return

        if root.is_on_group(body, ENEMY_GROUP):
            root.pause_tree()
            self.sprite.atlas.is_paused = True
            death_sfx.play()
            self.was_collided = True
            self.died.emit()

    def _on_Game_resumed(self) -> None:
        self.was_collided = False
        self.position = self._start_position
        self.sprite.atlas.is_paused = False
        self.points = 0

    def set_points(self, value) -> None:
        self._points = value
        self.points_changed.emit(f'Points: {value}')

    def get_points(self) -> None:
        return self._points

    def __init__(self, name: str = 'Player', coords: tuple[int, int] = VECTOR_ZERO,
                 color: Color = (15, 92, 105)) -> None:
        global root, _input, spritesheet, root, SPRITE_SIZE, SPRITES_SCALE, PLAYER_GROUP
        super().__init__(name, coords=coords, color=color)

        self.scale = array(SPRITES_SCALE)
        self._points: int = 0

        self._velocity = array([0.0, 0.0])
        self._floor = self.position[Y]
        self._start_position = coords

        _input.register_event(self, KEYDOWN, K_SPACE, self.JUMP)
        self.collided.connect(self, self, self._on_Body_collided)

        # Set the Sprite
        sprite: Sprite = Sprite()
        sprite.atlas.add_spritesheet(
            spritesheet, h_slice=3, sprite_size=SPRITE_SIZE)
        sprite.group = PLAYER_GROUP
        self.sprite = sprite
        root.add_to_group(self, PLAYER_GROUP)
        self.add_child(sprite)

        # Set the Shape
        shape: Shape = Shape()
        rect: Rect = Rect(sprite.atlas.rect)
        rect.size -= array([16, 16])
        shape.rect = rect
        self.add_child(shape)

        # Signals
        self.points_changed = Entity.Signal(self, 'points_changed')
        self.scored = Entity.Signal(self, 'scored')
        self.died = Entity.Signal(self, 'died')

        # Connections

        # Shift methods when testing
        self._move_: Callable
        self._apply_velocity_: Callable

        if IS_DEV_MODE_ENABLED:
            self._move_ = self._float
            self._apply_velocity_ = self._apply_xy_velocity
            self.speed += 1.0
        else:
            self._move_ = self._move
            self._apply_velocity_ = self._apply_x_velocity

    points: property = property(get_points, set_points)


class Clouds(Node):
    '''Objeto único de jogo. Controla a aparição de elementos visuais decorativos.'''

    def rearrange(self) -> Node:

        for child in self._children_index:
            child.position = randrange(50, 200, 100), randrange(50, 200, 50)

    def _spawn_clouds(self) -> None:
        global spritesheet, sprites_groups, SPRITE_SIZE, SPRITES_SCALE

        for i in range(1, 5):
            cloud: Sprite = Sprite(name=f'Cloud{i}', coords=(
                randrange(50, 200, 100), randrange(50, 200, 50)))
            cloud.atlas.add_spritesheet(spritesheet, coords=(
                SPRITE_SIZE[0] * 7, 0), sprite_size=SPRITE_SIZE)
            cloud.scale = array(SPRITES_SCALE)
            self.add_child(cloud)

    def __init__(self, name: str = 'Clouds', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)
        self._spawn_clouds()


class Floor(Node):
    '''Objeto único de jogo. Decorativo.'''

    def _spawn_floor(self) -> None:
        global spritesheet, sprites_groups, SPRITE_SIZE, SPRITES_SCALE

        for i in range(WIDTH // CELL_SIZE):
            piece: Sprite = Sprite(name=f'Piece{i}', coords=array(
                [(CELL_SIZE * SPRITES_SCALE[0]) * i - WIDTH, HEIGHT - CELL_SIZE]))
            piece.atlas.add_spritesheet(spritesheet, coords=(
                SPRITE_SIZE[0] * 6, 0), sprite_size=SPRITE_SIZE)
            piece.scale = array(SPRITES_SCALE)
            self.add_child(piece)

    def __init__(self, name: str = 'Floor', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)
        self.anchor = array(VECTOR_ZERO, dtype=float)
        self._spawn_floor()


class BackGround(Node):
    '''Objeto único de jogo. Controla o plano de fundo na tela.'''
    clouds: Clouds
    scroll_speed: int

    def speed_up(self) -> None:
        self.scroll_speed += 1

    def _process(self) -> None:
        global SPRITES_SCALE

        self.position[X] = self.position[X] - self.scroll_speed

        if self.position[X] < -(WIDTH // 2):
            self.position[X] = WIDTH
            self.clouds.rearrange()

    def __init__(self, scroll_speed: int = 1, name: str = 'BackGround',
                 coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)
        self.scroll_speed = scroll_speed
        self.anchor = array(VECTOR_ZERO, dtype=float)
        self.clouds = Clouds(coords=(0, 50))
        self.add_child(Floor())
        self.add_child(self.clouds)


'''
class Spawn(KinematicBody):
    collected: Node.Signal

    def _on_Collided(self, node: Node) -> None:
        if not (node._parent.name == 'Player'):
            return
        player: Player = node._parent
        player.points += 1
        self.collected.emit()
        self.position = randint(0, WIDTH), randint(0, HEIGHT)

    def __init__(self, name: str = 'Spawn', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)
        # self.connect(self.collided, self, self._on_Collided)
        self.collected = Node.Signal(self, 'collected')
'''


class Runner(KinematicBody):
    speed: float = 1.0
    notifier: VisibilityNotifier

    def _physics_process(self) -> None:
        edge: int = self.sprite.get_cell()[X] * self.scale[X]
        self.position[X] = (self.position[X] -
                            int(self.speed) + edge) % (WIDTH + edge * 2) - edge

    def __init__(self, name: str = 'Runner', coords: tuple[int, int] = VECTOR_ZERO, color: Color = Color(46, 10, 115)) -> None:
        super().__init__(name=name, coords=coords, color=color)

        # Set the VisibilityNotifier
        notifier: VisibilityNotifier = VisibilityNotifier()
        self.notifier = notifier
        self.add_child(notifier)


class Cactus(Runner):
    '''Objeto único de jogo. Objeto que pode colidir com o personagem protagonista.'''
    sprite: Sprite

    def __init__(self, name: str = 'Cactus', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        global spritesheet, sprites_groups, root, SPRITES_SCALE, ENEMY_GROUP
        super().__init__(name=name, coords=coords)
        self.scale = array(SPRITES_SCALE)

        # Set the sprite
        sprite: Sprite = Sprite()
        sprite.atlas.add_spritesheet(spritesheet, coords=(
            CELL_SIZE * 5, 0), sprite_size=CELL)
        sprite.group = ENEMY_GROUP
        root.add_to_group(self, ENEMY_GROUP)
        self.sprite = sprite
        self.add_child(sprite)

        # Set the shape
        shape: Shape = Shape()
        rect: Rect = Rect(sprite.atlas.rect)
        rect.size = rect.size - array([16, 8])
        shape.rect = rect
        self.add_child(shape)
        self.notifier.rect = Rect((0, 0), rect.size + array([6, 6]))


class PteroDino(Runner):
    sprite: Sprite

    def _on_Game_pause_toggled(self, paused: bool = False) -> None:
        self.sprite.atlas.is_paused = paused

    def __init__(self, name: str = 'PteroDino', coords: tuple[int, int] = VECTOR_ZERO,
                 color: Color = Color(46, 10, 115)) -> None:
        super().__init__(name=name, coords=coords, color=color)
        global spritesheet, sprites_groups, root, SPRITES_SCALE, SPRITE_SIZE, ENEMY_GROUP
        self.scale = array(SPRITES_SCALE)
        self.notifier.rect = Rect((0, 0), (24, 20))

        # Set the Sprite
        sprite: Sprite = Sprite()
        sprite.atlas.add_spritesheet(spritesheet, h_slice=2, coords=(
            CELL_SIZE * 3, 0), sprite_size=array(SPRITE_SIZE))
        sprite.group = ENEMY_GROUP
        self.sprite = sprite
        root.add_to_group(self, ENEMY_GROUP)
        self.add_child(sprite)

        # Set the Shape
        shape: Shape = Shape()
        rect: Rect = Rect(sprite.atlas.rect)
        rect.size -= array([16, 16])
        shape.rect = rect
        self.add_child(shape)

        # Connect to events
        root.connect(root.pause_toggled, self, self._on_Game_pause_toggled)


class Spawner(Node):
    '''Objeto único de jogo. Nó responsável pela aparição de obstáculos na tela.'''
    current_speed: int
    cactus: Cactus = None
    pterodino: PteroDino = None
    spawns: list[Node] = None

    def _on_Game_resumed(self) -> None:

        for child in self._children_index:
            child.position[X] = self._SPAWN_POS

    def set_speed(self, value: float) -> None:
        self.current_speed = value
        self.cactus.speed = value
        self.pterodino.speed = value

    def speed_up(self) -> None:
        self.set_speed(self.current_speed + 1)

    def _on_Notifier_screen_exited(self, node: Node) -> None:
        self.remove_child(node)
        self.add_child(choice(self.spawns))

    def _setup_spawn(self) -> None:
        global FLOOR_COORD
        notifier: VisibilityNotifier

        self.cactus = Cactus(
            coords=(self._SPAWN_POS, FLOOR_COORD + CELL_SIZE // 2))
        notifier = self.cactus.notifier
        notifier.connect(notifier.screen_exited, self,
                         self._on_Notifier_screen_exited, self.cactus)

        self.pterodino = PteroDino(coords=(self._SPAWN_POS, HEIGHT // 2 + 100))
        notifier = self.pterodino.notifier
        notifier.connect(notifier.screen_exited, self,
                         self._on_Notifier_screen_exited, self.pterodino)

        self.spawns = [self.cactus, self.pterodino]
        self.add_child(choice(self.spawns))

    def __init__(self, name: str = 'Spawner', coords: tuple[int, int] = VECTOR_ZERO, speed: int = 1) -> None:
        global root
        super().__init__(name=name, coords=coords)

        self._SPAWN_POS: int = WIDTH + CELL_SIZE * SPRITES_SCALE[X]
        self._setup_spawn()
        self.anchor = array(BOTTOM_RIGHT)
        self.set_speed(speed)


class GameOverDisplay(Node):
    RESTART: str = 'restart'
    label: Label
    game_resumed: Node.Signal

    def _input_event(self, event: InputEvent) -> None:
        global root
        # if event.tag is self.RESTART:
        
        if root.tree_pause & Node.PauseModes.TREE_PAUSED:
            self.remove_child(self.label)
            self.game_resumed.emit()
            root.pause_tree(0)

    def show(self) -> None:
        self.add_child(self.label)

    def __init__(self, name: str = 'GameOverDisplay', coords: tuple[int, int] = VECTOR_ZERO) -> None:
        super().__init__(name=name, coords=coords)

        self.label = Label(coords=array(SCREEN_SIZE) // 2,
                           color=COLOR_BLACK, text='Game Over')
        self.label.anchor = CENTER
        # self.label.position = array(SCREEN_SIZE) // 2 - \
        #     array(self.label.update_surface().get_size()) // 2

        _input.register_event(self, KEYDOWN, K_SPACE, self.RESTART)
        self.game_resumed = Node.Signal(self, 'game_resumed')


# %%
# Loading Resources
ROOT_DIR: str = path.dirname(__file__)
ASSETS_DIR: str = path.join(ROOT_DIR, 'assets')

SPRITES_DIR: str = path.join(ASSETS_DIR, 'sprites')
SOUNDS_DIR: str = path.join(ASSETS_DIR, 'sounds')

SPRITES_SCALE: tuple[float, float] = 3., 3.
FLOOR_COORD: float = HEIGHT - CELL_SIZE * SPRITES_SCALE[Y]

# Groups
DEFAULT_GROUP: str = 'default'
ENEMY_GROUP: str = 'enemy'
PLAYER_GROUP: str = 'player'

# Sprites
SPRITE_SIZE: tuple[int, int] = 32, 32

spritesheet: Surface = pygame.image.load(
    path.join(SPRITES_DIR, 'dino.png'))

sprites_groups: dict[str, sprite.Group] = {
    'default': sprite.Group(),
    PLAYER_GROUP: sprite.Group(),
    ENEMY_GROUP: sprite.Group(),
}

# Sound Streams
death_sfx: Sound = Sound(path.join(SOUNDS_DIR, 'death.wav'))
jump_sfx: Sound = Sound(path.join(SOUNDS_DIR, 'jump.wav'))
score_sfx: Sound = Sound(path.join(SOUNDS_DIR, 'score.wav'))

# %%
# Singletons
_input: Input = Input()
# %%
root: SceneTree = SceneTree()
bg: BackGround = BackGround(3)
spawner: Spawner = Spawner(speed=bg.scroll_speed)
# spawn: Spawn = Spawn(coords=(randint(0, WIDTH), randint(0, HEIGHT)))

player: Player = Player(coords=array(
    [WIDTH // 2, FLOOR_COORD + CELL_SIZE // 2]) + (16, 16))
# player: Player = Player(coords=(WIDTH // 2, HEIGHT // 2))
player.scale = array(SPRITES_SCALE)

# GUI
label: Label = Label((40, 40), color=COLOR_BLACK, text='Points: 0')
display: GameOverDisplay = GameOverDisplay()

# Construção da árvore
root.add_child(bg)
# root.add_child(spawn)
root.add_child(player)
root.add_child(spawner)
root.add_child(label)
root.add_child(display)

# Conexões
# spawn.connect(spawn.collected, score_sfx, score_sfx.play)
player.connect(player.points_changed, label, label.set_text)
player.connect(player.scored, bg, bg.speed_up)
player.connect(player.scored, spawner, spawner.speed_up)
player.connect(player.died, display, display.show)
display.connect(display.game_resumed, spawner, spawner._on_Game_resumed)
display.connect(display.game_resumed, player, player._on_Game_resumed)

# Fila de renderização (para labels e outras superfícies)).
render_queue: deque[Surface, tuple[int, int]] = deque()

# %%
# Main Loop
while True:
    clock.tick(FIXED_FPS)
    screen.fill(COLOR_WHITE)
    # Preenche a tela

    _input._tick()
    # Propaga as entradas

    root._propagate()
    # Propaga o processamento

    for id, sprites in sprites_groups.items():
        # Desenha os sprites
        sprites.draw(screen)
        sprites.update()

    while render_queue:
        # Desenha a GUI
        screen.blit(*render_queue.pop())

    pygame.display.update()
