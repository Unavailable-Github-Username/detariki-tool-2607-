import os
import argparse
from base import *
from config import *
from chara_list import *

parser = argparse.ArgumentParser()

parser.add_argument('-save', help='save asset bundle files (default: False)', default=False, action='store_true')
parser.add_argument('-o', help='output path', default=CACHE_PATH, type=str)


class Pic(Base):
    def __download(self, path: str, p_name: str, save_dir='', save_ab=False):
        try:
            a_name = os.path.split(path)[1]
            os.makedirs(save_dir, exist_ok=True)
            if save_ab:
                if not os.path.exists(os.path.join(save_dir, path)):
                    self.cdn_download(path, save_dir)
                if not os.path.exists(os.path.join(save_dir, p_name)):
                    self.extract_texture2D(os.path.join(save_dir, a_name), save_dir)
            else:
                if os.path.exists(os.path.join(save_dir, p_name)):
                    return        
                if not os.path.exists(os.path.join(save_dir, a_name)):
                    data = self.cdn_get(path)
                    self.extract_texture2D(data, save_dir)
                else:
                    self.extract_texture2D(os.path.join(save_dir, a_name), save_dir)
        except Exception as e:
            print(f'[ {red(a_name)} ] failed. {e}')
            pass


    """
    def download_illust(self, no: int, save_dir='', save_ab=False):
        # illustration/illustration_illustration_00001
        path = f'titleimage/titleimage_title{no:d}_r'
        p_name = f'title{no:d}_r.png'
        self.__download(path, p_name, os.path.join(save_dir, CACHE_PIC_TITLE), save_ab)
    """
    def download_titleimage(self, no: int, save_dir='', save_ab=False):
        # titleimage/titleimage_title113_r
        if ( no < 10 ):
            path = f'titleimage/titleimage_title{no:02d}_r'
            p_name = f'title{no:02d}_r.png'
        else:
            path = f'titleimage/titleimage_title{no:d}_r'
            p_name = f'title{no:d}_r.png'
        self.__download(path, p_name, os.path.join(save_dir, CACHE_PIC_TITLE), save_ab)

    def download_battlepreparation(self, no: int, save_dir='', save_ab=False):
        # battlepreparation/battlepreparation_ca_battle_preparation_04_d
        path = f'battlepreparation/battlepreparation_ca_battle_preparation_{no:02d}_d'
        p_name = f'ca_battle_preparation_{no:02d}_d.png'
        self.__download(path, p_name, os.path.join(save_dir, CACHE_PIC_LOAD), save_ab)

    def download_battlecutin_chr(self, chr_id: int, save_dir='', save_ab=False):
        # battlecutinicon/battlecutinicon_cutin_icon_00234
        path = f'battlecutinicon/battlecutinicon_cutin_icon_{chr_id:05d}'
        p_name = f'cutin_icon_{chr_id:05d}.png'
        self.__download(path, p_name, os.path.join(save_dir, CACHE_PIC_CUTIN), save_ab)

    def download_chric_large(self, chr_id: int, save_dir='', save_ab=False):
        # charactericonlarge/charactericonlarge_character_icon_large_00234
        path = f'charactericonlarge/charactericonlarge_character_icon_large_{chr_id:05d}'
        p_name = f'character_icon_large_{chr_id:05d}.png'
        self.__download(path, p_name, os.path.join(save_dir, CACHE_PIC_LOBBY), save_ab)

    def download_chric_large_s(self, chr_id: int, save_dir='', save_ab=False):
        # charactericonlarges/charactericonlarges_character_icon_large_s_00002
        path = f'charactericonlarges/charactericonlarges_character_icon_large_s_{chr_id:05d}'
        p_name = f'character_icon_large_s_{chr_id:05d}.png'
        self.__download(path, p_name, os.path.join(save_dir, CACHE_PIC_LOBBY), save_ab)





if __name__ == '__main__':
    args = parser.parse_args()

    p = Pic()

    for id in TITLE_RANGE:
        p.download_titleimage(id, args.o, args.save)

    for id in range(0, 10):
        p.download_battlepreparation(id, args.o, args.save)

    ids = [i for i in chara_list]
    for id in ids:
        p.download_battlecutin_chr(id, args.o, args.save)

    for id in ids:
        p.download_chric_large(id, args.o, args.save)

    for id in ids:
        p.download_chric_large_s(id, args.o, args.save)