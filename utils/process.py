import os
import cv2
import pathlib
from anime_face_detect import detect


countries = ["mondstadt", "liyue", "inazuma"]


def process():
    if not os.path.exists('process_result'):
        os.mkdir('process_result')

    if not os.path.exists('process_result/train'):
        os.mkdir('process_result/train')

    if not os.path.exists('process_result/valid'):
        os.mkdir('process_result/valid')

    for country in countries:
        characters = os.listdir(country)
        print(f"processing country: {country}")

        for character in characters:
            character_dir = f"{country}/{character}"
            if not os.path.isdir(character_dir):
                continue
            print(f"processing character: {character}")
            for filter in ['train', 'valid']:
                if not os.path.exists(f'process_result/{filter}/{character}'):
                    os.mkdir(f'process_result/{filter}/{character}')

            images = os.listdir(character_dir)
            num_trains = int(len(images) * 0.8)
            for img_idx, image in enumerate(images):
                img, faces = detect(f"{country}/{character}/{image}")
                image_path = pathlib.Path(image)
                stem = image_path.stem
                suffix = image_path.suffix
                filter = 'train' if img_idx < num_trains else 'valid'

                for idx, face in enumerate(faces):
                    x, y, w, h = face
                    cropped = img[y:y+h, x:x+w]
                    resized = cv2.resize(cropped, (128, 128))
                    cv2.imwrite(
                        f'process_result/{filter}/{character}/{stem}-{idx}{suffix}', resized)


if __name__ == "__main__":
    process()
