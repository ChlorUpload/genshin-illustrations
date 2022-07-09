import os
from pathlib import Path
import shutil


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

            os.chdir('datagen/detector2')
            os.system(f'python main.py -i ../../{country}/{character} -crop-location ../../process_result/train/{character}/img -crop-height 128 -crop-width 128')
            os.chdir('../..')

    for country in countries:
        characters = os.listdir(country)
        for character in characters:
            images = os.listdir(f"process_result/train/{character}")
            
            valid_idx = int(len(images) * 0.8)
            for image in images:
                image_path = Path(f"process_result/train/{character}/{image}")
                if valid_idx <= int(image_path.stem[3:]):
                    shutil.move(image_path, f'process_result/valid/{character}/{image_path.stem}{image_path.suffix}')

            # images = os.listdir(f"process_result/valid/{character}")
            # for image in images:
            #     image_path = Path(f"process_result/valid/{character}/{image}")
            #     shutil.move(image_path, f'process_result/train/{character}/{image_path.stem[:-1]}{image_path.suffix}')

if __name__ == "__main__":
    process()
