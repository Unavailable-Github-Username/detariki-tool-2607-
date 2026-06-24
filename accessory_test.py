import os
import argparse
from base import *
from config import *
from chara_list import *

parser = argparse.ArgumentParser()

parser.add_argument('-id', help='body id', default=0, type=int)
parser.add_argument('-o', help='output path', default=CACHE_PATH, type=str)


class Accessory(Base):
    def __init__ (self, id: int):
        self.id = id

    def download_all(self, save_dir=''):
        """
        Try to download all possible assets related to this body no.
        """
        """
        chr = 'chara'
        ac = 0
        acs = [i for i in chara_list]
        output_dir = os.path.join(save_dir, CACHE_CHR_ACC, str(chr))
        for ac in acs:
            self.cdn_download(self.accessory_chr_path(ac), output_dir)
            if (ac == acs):
                break

        """
        output_dir = os.path.join(save_dir, CACHE_CHR_ACC, str(self.id))
        for slt in range(0, 4):
            if self.cdn_download(self.accessory_path(self.id, slt), output_dir) >= 0:
                self.cdn_download(self.texture_path(self.id, slt), output_dir)
                p_texture = os.path.join(output_dir, self.texture_name(self.id, slt))
                if os.path.exists(p_texture):
                    self.extract_texture2D(p_texture, output_dir)



    @staticmethod
    def accessory_chr_name(ac: int):
        # chara_parts_accessory_chara_13_0_acc
        return f'chara_parts_accessory_chara_{ac}_0_acc'
    
    @staticmethod
    def accessory_chr_path(ac: int):
        # chara/parts/accessory/chara_parts_accessory_chara_13_0_acc
        return f'chara/parts/accessory/{Accessory.accessory_chr_name(ac)}'
    
    @staticmethod
    def accessory_name(id: int, slt = 0):
        # chara_parts_accessory_body1647_0_acc
        return f'chara_parts_accessory_body{id}_{slt}_acc'
    
    @staticmethod
    def accessory_path(id: int, slt = 0):
        # chara/parts/body/chara_parts_accessory_body1647_0_acc
        return f'chara/parts/accessory/{Accessory.accessory_name(id, slt)}'
    
    @staticmethod
    def texture_name(id: int, slt = 0):
        # chara_parts_accessory_body1647_0_acc_texture_body1647_0_acc_0
        return f'chara_parts_accessory_body{id}_{slt}_acc_texture_body{id}_{slt}_acc_0'
    
    @staticmethod
    def texture_path(id: int, slt = 0):
        # chara/parts/body/body1497_texture/chara_parts_accessory_body1647_0_acc_texture_body1647_0_acc_0
        return f'chara/parts/accessory/body{id}_{slt}_acc_texture/{Accessory.texture_name(id, slt)}'


    @staticmethod
    def possible_id_range() -> list:
        r = []
        for v in ACC_ID_RANGE:
            r += v
        return r
        


if __name__ == '__main__':
    args = parser.parse_args()

    ids = [args.id]
    if args.id == 0:
        ids = Accessory.possible_id_range()

    for id in ids:
        b = Accessory(id)
        b.download_all(args.o)
