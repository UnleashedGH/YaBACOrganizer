from yabac.panels.types import BasePanel


class TransparencyEffectPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.transparency_flags = self.add_hex_entry(self.entry_page, 'Transparency Flags')
        self.dilution = self.add_num_entry(self.entry_page, 'Dilution')
        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E', max=0xFFFF)
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.red = self.add_float_entry(self.entry_page, 'Red')
        self.green = self.add_float_entry(self.entry_page, 'Green')
        self.blue = self.add_float_entry(self.entry_page, 'Blue')
        self.f_20 = self.add_float_entry(self.unknown_page, 'F_20')
        self.f_24 = self.add_float_entry(self.unknown_page, 'F_24')
        self.f_28 = self.add_float_entry(self.unknown_page, 'F_28')
        self.f_2c = self.add_float_entry(self.unknown_page, 'F_2C')
        self.f_30 = self.add_float_entry(self.unknown_page, 'F_30')
        self.f_34 = self.add_float_entry(self.unknown_page, 'F_34')
        self.f_38 = self.add_float_entry(self.unknown_page, 'F_38')
        self.f_3c = self.add_float_entry(self.unknown_page, 'F_3C')
