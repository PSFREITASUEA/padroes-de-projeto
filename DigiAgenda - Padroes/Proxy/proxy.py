'''
1 ImageProxy primeiro cria um ImageIcon e começa a carregá-lo a partir de um
URL da rede.
2 Enquanto os bytes da imagem estão sendo recuperados, ImageProxy
exibe “Carregando a capa do CD, aguarde ...”.
3 Quando a imagem está totalmente carregada, ImageProxy delega todos os métodos
chamados para o ícone da imagem, incluindo paintIcon(), getWidth() e
getHeight().
4 Se o usuário solicitar uma nova imagem, criaremos um novo proxy e
recomeçaremos o processo.

'''


from abc import ABC, abstractmethod

class ImageProxy:
    retrieving = False
    imageURL = ""
    def __init__(url):
        self.imageURL = url
    

    def getIconWidth():
        if imageIcon != None:
            return imageIcon.getIconWidth()
        else:
            return 800
        

    def getIconHeight():
        if imageIcon != None:
            return imageIcon.getIconHeight()
        else:
            return 600
    
    def setImageIcon(imageIcon):
        self.imageIcon = imageIcon
    
    def paintIcon(c, g, x, y):
        if imageIcon != None:
            imageIcon.paintIcon(c,g,x,y)

        else:
            print("Carregando capa do CD, por favor, espere...", x+300, y+190)
            if not retrieving:
                retrieving = True
                retrievalThread = Thread(Runnable()
                    def run():
                        try: 
                            setImageIcon(ImageIcon(imageURL, "album cover"))
                            c.repaint()
                        catch (Exception e):
                            e.printStackTrace()
                )

                retrievalThread = Thread(() ->
                    try:
                        setImageIcon(ImageIcon(imageURL, "album cover"))
                        c.repaint()

                    catch (Exception e):
                    e.printStackTrace()
                )
                retrievalThread.start()