pygame.init()
font =pygame.font.font(None,30)
def debug(info,y = 10, x =10):
    display_surface =pygame.display.get_surface()
    debug_surf = font.render(str(info), True,'white')
    debug_surf = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface,'Black',debug_rect)
    display_surface.blit(debug_surf,debug_rect)
