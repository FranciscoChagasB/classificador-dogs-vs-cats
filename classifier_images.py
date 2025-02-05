import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Classificação de imagens
model = tf.keras.models.load_model('modelo_gato_cachorro_mobilenet.h5')
input_size = (160, 160)
input_folder = './imagens_para_classificar'
output_folder = './output'
os.makedirs(output_folder, exist_ok=True)

# Processar todas as imagens da pasta
for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)
    
    # Verifica se é uma imagem válida
    if not img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue
    
    # Carregar e processar a imagem
    img = image.load_img(img_path, target_size=input_size)
    img_array = image.img_to_array(img) / 255.0  # Normalização
    img_array = np.expand_dims(img_array, axis=0)

    # Fazer a predição
    prediction = model.predict(img_array)[0][0]
    label = "Cachorro" if prediction > 0.5 else "Gato"
    
    # Carregar a imagem com OpenCV para desenhar o rótulo
    img_cv = cv2.imread(img_path)
    
    # Ajustar tamanho do texto e posição
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_position = (20, 40)  # Coordenadas do texto (x, y)
    font_scale = 1
    color = (0, 255, 0)  # Verde
    thickness = 2

    # Desenhar o texto na imagem
    cv2.putText(img_cv, label, text_position, font, font_scale, color, thickness)

    # Salvar a imagem processada
    output_path = os.path.join(output_folder, img_name)
    cv2.imwrite(output_path, img_cv)

print(f'Classificação concluída! Imagens salvas em "{output_folder}".')