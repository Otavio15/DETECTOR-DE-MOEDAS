import cv2

imagem_moeda = cv2.imread("moeda.jpg") #captura a imagem

#Algoritmos de pré processamento
imagem_cinza = cv2.cvtColor(imagem_moeda, cv2.COLOR_BGR2GRAY) #converte em escala de cinza
aux, imagem_binaria = cv2.threshold(imagem_cinza, 180, 255, cv2.THRESH_BINARY) #binariza a imagem

#algoritmos de segmentação
contornos, hierarquia = cv2.findContours(imagem_binaria, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #captura os contornos

for cnt in contornos: #percorre os contornos
    perimetro = cv2.arcLength(cnt, True)
    if (perimetro > 700):
        (x,y,a,l) = cv2.boundingRect(cnt)
        if (a-l < 5):
            if (a > 200 and a < 230):
                cv2.rectangle(imagem_moeda, (x, y), (x + a, y + l), (0, 255, 0), 2)
                cv2.putText(imagem_moeda, '10 Centavos', (x + 5, y + 100), cv2.FONT_ITALIC, (1.0), (0, 255, 0), 2)
            elif (a > 230 and a < 250):
                cv2.rectangle(imagem_moeda, (x, y), (x + a, y + l), (0, 0, 255), 2)
                cv2.putText(imagem_moeda, '5 Centavos', (x + 5, y + 100), cv2.FONT_ITALIC, (1.0), (0, 0, 255), 2)
            elif (a > 250 and a < 270):
                cv2.rectangle(imagem_moeda, (x, y), (x + a, y + l), (255, 0, 0), 2)
                cv2.putText(imagem_moeda, '50 Centavos', (x + 5, y + 100), cv2.FONT_ITALIC, (1.0), (255, 0, 0), 2)
            elif (a > 270 and a < 290):
                cv2.rectangle(imagem_moeda, (x, y), (x + a, y + l), (0, 0, 0), 2)
                cv2.putText(imagem_moeda, '25 Centavos', (x + 5, y + 100), cv2.FONT_ITALIC, (1.0), (0, 0, 0), 2)
            elif (a > 290 and a < 310):
                cv2.rectangle(imagem_moeda, (x, y), (x + a, y + l), (0, 255, 255), 2)
                cv2.putText(imagem_moeda, '1 Real', (x + 5, y + 100), cv2.FONT_ITALIC, (1.0), (0, 255, 255), 2)
#saída
cv2.imshow("Moedas", imagem_moeda)
cv2.waitKey()