import os
import argparse
from base import *
from config import *

parser = argparse.ArgumentParser()

parser.add_argument('-save', help='save asset bundle files (default: False)', default=True, action='store_true')
parser.add_argument('-o', help='output path', default=CACHE_PATH, type=str)


class Gacha(Base):
    def __download(self, path: str, p_name: str, save_dir='', save_ab=True):
        try:
            a_name = os.path.split(path)[1]
            os.makedirs(save_dir, exist_ok=True)
            if save_ab:
                if not os.path.exists(os.path.join(save_dir, path)):
                    self.cdn_download(path, save_dir)
                #if not os.path.exists(os.path.join(save_dir, p_name)):
                    #self.extract_texture2D(os.path.join(save_dir, a_name), save_dir)
            else:
                if os.path.exists(os.path.join(save_dir, p_name)):
                    return        
                if not os.path.exists(os.path.join(save_dir, a_name)):
                    data = self.cdn_get(path)
                    #self.extract_texture2D(data, save_dir)
                #else:
                    #self.extract_texture2D(os.path.join(save_dir, a_name), save_dir)
        except Exception as e:
            print(f'[ {red(a_name)} ] failed. {e}')
            pass


    def download_all(self, id: int, save_dir='', save_ab=True):
        # video/gacha_03501_r
        path = f'video/video_gacha_{id:05d}_r'
        p_name = f'gacha_{id:05d}_r'
        self.__download(path, p_name, os.path.join(save_dir, CACHE_VID_GACHA), save_ab)

    @staticmethod
    def possible_id_range() -> list:
        r = []
        for v in GACHA_RANGE:
            r += v
        return r


if __name__ == '__main__':
    args = parser.parse_args()

    g = Gacha()

    for id in g.possible_id_range():
        g.download_all(id, args.o, args.save)