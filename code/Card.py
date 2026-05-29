import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, name, value, suit, ability=None, frame_type="Normal", rarity="Común"):
        super().__init__() # Inicializa la clase base de Sprite de Pygame
        
        # --- Atributos de Datos ---
        self.name = name
        self.value = value
        self.suit = suit # ej: "Espada", "Basto", "Oro", "Copa" (o palos custom)
        self.ability = ability
        self.frame_type = frame_type # ej: "Foil", "Holográfico", "Oxidado" (estilo Balatro)
        self.rarity = rarity
        
        # --- Atributos Visuales (Pygame) ---
        # self.image es lo que Pygame dibuja. Por ahora es un rectángulo blanco de prueba.
        # Más adelante acá cargaremos las imágenes desde assets/images/
        self.image = pygame.Surface((120, 180)) 
        self.image.fill((255, 255, 255))
        
        # self.rect maneja la posición y las "hitboxes" para los clics
        self.rect = self.image.get_rect()
        
    def trigger_ability(self, game_state):
        """Ejecuta la habilidad especial de la carta si tiene una."""
        if self.ability:
            # Acá irá la lógica para modificar el estado del juego
            # ej: robar carta, multiplicar envido, etc.
            pass

    def apply_frame_effect(self):
        """Aplica los modificadores pasivos del marco."""
        # ej: Si frame_type == "Dorado", suma +3 al truco.
        pass

    def update(self):
        """Método estándar de Pygame para actualizar el estado de la carta en cada frame."""
        # Acá podés poner lógica de animaciones, como hacer que la carta "flote" 
        # o reaccione cuando pasás el mouse por encima.
        pass

    def __str__(self):
        # Útil para printear en consola y debugear rápido
        return f"[{self.rarity}] {self.name} ({self.value} de {self.suit}) | Marco: {self.frame_type}"