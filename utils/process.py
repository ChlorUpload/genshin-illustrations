import os
import cv2
import pathlib
from anime_face_detect import detect


countries = ["mondstadt", "liyue", "inazuma"]

def process():
    if not os.path.exists('process_result'):
        os.mkdir('process_result')

    for country in countries:
        characters = os.listdir(country)
        print(f"processing country: {country}")

        for character in characters:
            character_dir = f"{country}/{character}"
            if not os.path.isdir(character_dir):
                continue
            print(f"processing character: {character}")
            images = os.listdir(character_dir)
            for image in images:
                img, faces = detect(f"{country}/{character}/{image}")

                image_path = pathlib.Path(image)
                stem = image_path.stem
                suffix = image_path.suffix
                
                for idx, face in enumerate(faces):
                    x, y, w, h = face
                    cropped = img[y:y+h, x:x+w]
                    resized = cv2.resize(cropped, (128, 128))
                    cv2.imwrite(f'process_result/{country}-{character}-{stem}-{idx}{suffix}', resized)
                    
                

if __name__ == "__main__":
    process()