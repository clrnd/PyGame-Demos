import pygame
import sys

class StickMan(pygame.sprite.Sprite):

   def __init__(self, position):

      pygame.sprite.Sprite.__init__(self)
      self.screen = pygame.display.get_surface().get_rect()
      self.image = pygame.surface.Surface((10,10))
      self.rect = self.image.get_rect()
      self.rect.x = position[0]
      self.rect.y = position[1]

   def update(self, amount):

      self.rect = self.rect.move(amount)

      # Check for offscreen movements
      if self.rect.x < 0:
         self.rect.x = 0
      elif self.rect.x > (self.screen.width - self.rect.width):
         self.rect.x = self.screen.width - self.rect.width
      if self.rect.y < 0:
         self.rect.y = 0
      elif self.rect.y > (self.screen.height - self.rect.height):
         self.rect.y = self.screen.height - self.rect.height

# Function to erase the sprite
def eraseSprite(screen, rect):
   screen.blit(blank, rect)

pygame.init()
screen = pygame.display.set_mode((256, 256))
pygame.display.set_caption('Collision Detection')
screen.fill((255, 255, 255))

# Create three non-playable stickmen
stick1 = StickMan((25, 25))
stick2 = StickMan((100, 150))
stick3 = StickMan((175, 175))

# Add them each to a group
group1 = pygame.sprite.Group()
group2 = pygame.sprite.Group()
group3 = pygame.sprite.Group()
group1.add(stick1)
group2.add(stick2)
group3.add(stick3)

# Create a playable stickman and add it to a group
player = StickMan((200,10))
playerGroup = pygame.sprite.RenderUpdates()
playerGroup.add(player)

# Create a background piece
blank = pygame.Surface((player.rect.width, player.rect.height))
blank.fill((255, 255, 255))

# Draw each sprite
group1.draw(screen)
group2.draw(screen)
group3.draw(screen)
playerGroup.draw(screen)

pygame.display.update()

while True:

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()

      # Move the player if a key is pressed
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            player.update([-10, 0])
         elif event.key == pygame.K_UP:
            player.update([0, -10])
         elif event.key == pygame.K_RIGHT:
            player.update([10, 0])
         elif event.key == pygame.K_DOWN:
            player.update([0, 10])

         # Check to see if the player has collided with stick1 in group1
         # If a collision is detected, kill stick1 (True)
         collide1 = pygame.sprite.spritecollide(player, group1,True)

         # Check to see if the playerGroup has collided with group2
         # Kill all involved sprites if there is a collision
         collide2 = pygame.sprite.groupcollide(playerGroup,group2, True, True)

         # Check to see if the player has collided with anything in group3
         collide3 = pygame.sprite.spritecollideany(player,group3)

         # Print the test results
         print 'Test 1:', collide1
         print 'Test 2:', collide2
         print 'Test 3:', collide3

         # If the player has died, print a game over message,wait and then quit
         if not player.alive():
            print 'Game Over'
            pygame.time.wait(3000)
            sys.exit()

         # Clear the player's old spot
         playerGroup.clear(screen, eraseSprite)

         # Draw the player
         updateRects = playerGroup.draw(screen)

         # If we need to redraw other things, then do so
         if collide1:
            group1.clear(screen, eraseSprite)
            group1.draw(screen)
            updateRects.append(stick1.rect)
         elif collide2:
            group2.draw(screen)
            updateRects.append(stick2.rect)
         elif collide3:
            group3.draw(screen)
            updateRects.append(stick3.rect)

         # Update everything
         pygame.display.update(updateRects)
