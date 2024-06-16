if (self.holly.colisaoB(self.mesa1_rect) or self.holly.colisaoB(self.mesa2_rect) or
                    self.holly.colisaoB(self.mesa3_rect) or self.holly.colisaoB(self.mesa4_rect)):
                self.movimento_up = False
            if (self.holly.colisaoC(self.mesa1_rect) or self.holly.colisaoC(self.mesa2_rect) or
                    self.holly.colisaoC(self.mesa3_rect) or self.holly.colisaoC(self.mesa4_rect)):
                self.movimento_down = False

            if (self.holly.colisaoE(self.mesa1_rect) or self.holly.colisaoE(self.mesa2_rect) or
                    self.holly.colisaoE(self.mesa3_rect) or self.holly.colisaoE(self.mesa4_rect)):
                self.movimento_esquerda = False
            if ((self.holly.colisaoD(self.mesa1_rect) or self.holly.colisaoD(self.mesa2_rect) or
                    self.holly.colisaoD(self.mesa3_rect) or self.holly.colisaoD(self.mesa4_rect))
                    or self.holly.rect.right >= self.chao_rect.right):
                self.movimento_direita = False


                def colisaoB(self, objeto):
                    colidiu = False
                    if self.rect.bottom >= objeto.top and self.rect.bottom <= objeto.bottom and \
                            self.rect.right > objeto.left and self.rect.left < objeto.right:
                        colidiu = True
                    return colidiu


                def colisaoC(self, objeto):
                    colidiu = False
                    if self.rect.top <= objeto.bottom and self.rect.top >= objeto.top and \
                            self.rect.right > objeto.left and self.rect.left < objeto.right:
                        colidiu = True
                    return colidiu


                def colisaoE(self, objeto):
                    colidiu = False
                    if self.rect.left <= objeto.right and self.rect.left >= objeto.left and \
                            self.rect.bottom > objeto.top and self.rect.top < objeto.bottom:
                        colidiu = True
                    return colidiu


                def colisaoD(self, objeto):
                    colidiu = False
                    if self.rect.right >= objeto.left and self.rect.right <= objeto.right and \
                            self.rect.bottom > objeto.top and self.rect.top < objeto.bottom:
                        colidiu = True
                    return colidiu

                or self.holly.colisaoD(self.mesa2_rect) or
                self.holly.colisaoD(self.mesa3_rect) or self.holly.colisaoD(self.mesa4_rect)