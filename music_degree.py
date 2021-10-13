"""The name is a joke. This provides a set of utilities that you would more likely
learn in an introductory music course, including standard keys, their frequencies,
as well as functions to collect major and minor scales.
Frequencies obtained from https://pages.mtu.edu/~suits/notefreqs.html"""

tone_map = {'C0': 16.35,
            'C_sharp_0/D_flat_0': 17.32,
            'D0': 18.35,
            'D_sharp_0/E_flat_0': 19.45,
            'E0': 20.60,
            'F0': 21.83,
            'F_sharp_0/G_flat_0': 23.12,
            'G0': 24.50,
            'G_sharp_0/A_flat_0': 25.96,
            'A0': 27.50,
            'A_sharp_0/B_flat_0': 29.14,
            'B0': 30.87,
            'C1': 32.70,
            'C_sharp_1/D_flat_1': 34.65,
            'D1': 36.71,
            'D_sharp_1/E_flat_1': 38.89,
            'E1': 41.20,
            'F1': 43.65,
            'F_sharp_1/G_flat_1': 46.25,
            'G1': 49.00,
            'G_sharp_1/A_flat_1': 51.91,
            'A1': 55.00,
            'A_sharp_1/B_flat_1': 58.27,
            'B1': 61.74,
            'C2': 65.41,
            'C_sharp_2/D_flat_2': 69.30,
            'D2': 73.42,
            'D_sharp_2/E_flat_2': 77.78,
            'E2': 82.41,
            'F2': 87.31,
            'F_sharp_2/G_flat_2': 92.50,
            'G2': 98.00,
            'G_sharp_2/A_flat_2': 103.83,
            'A2': 110.00,
            'A_sharp_2/B_flat_2': 116.54,
            'B2': 123.47,
            'C3': 130.81,
            'C_sharp_3/D_flat_3': 138.59,
            'D3': 146.83,
            'D_sharp_3/E_flat_3': 155.56,
            'E3': 164.81,
            'F3': 174.61,
            'F_sharp_3/G_flat_3': 185.00,
            'G3': 196.00,
            'G_sharp_3/A_flat_3': 207.65,
            'A3': 220.00,
            'A_sharp_3/B_flat_3': 233.08,
            'B3': 246.94,
            'C4': 261.63,
            'C_sharp_4/D_flat_4': 277.18,
            'D4': 293.66,
            'D_sharp_4/E_flat_4': 311.13,
            'E4': 329.63,
            'F4': 349.23,
            'F_sharp_4/G_flat_4': 369.99,
            'G4': 392.00,
            'G_sharp_4/A_flat_4': 415.30,
            'A4': 440.00,
            'A_sharp_4/B_flat_4': 466.16,
            'B4': 493.88,
            'C5': 523.25,
            'C_sharp_5/D_flat_5': 554.37,
            'D5': 587.33,
            'D_sharp_5/E_flat_5': 622.25,
            'E5': 659.25,
            'F5': 698.46,
            'F_sharp_5/G_flat_5': 739.99,
            'G5': 783.99,
            'G_sharp_5/A_flat_5': 830.61,
            'A5': 880.00,
            'A_sharp_5/B_flat_5': 932.33,
            'B5': 987.77,
            'C6': 1046.50,
            'C_sharp_6/D_flat_6': 1108.73,
            'D6': 1174.66,
            'D_sharp_6/E_flat_6': 1244.51,
            'E6': 1318.51,
            'F6': 1396.91,
            'F_sharp_6/G_flat_6': 1479.98,
            'G6': 1567.98,
            'G_sharp_6/A_flat_6': 1661.22,
            'A6': 1760.00,
            'A_sharp_6/B_flat_6': 1864.66,
            'B6': 1975.53,
            'C7': 2093.00,
            'C_sharp_7/D_flat_7': 2217.46,
            'D7': 2349.32,
            'D_sharp_7/E_flat_7': 2489.02,
            'E7': 2637.02,
            'F7': 2793.83,
            'F_sharp_7/G_flat_7': 2959.96,
            'G7': 3135.96,
            'G_sharp_7/A_flat_7': 3322.44,
            'A7': 3520.00,
            'A_sharp_7/B_flat_7': 3729.31,
            'B7': 3951.07,
            'C8': 4186.01,
            'C_sharp_8/D_flat_8': 4434.92,
            'D8': 4698.63,
            'D_sharp_8/E_flat_8': 4978.03,
            'E8': 5274.04,
            'F8': 5587.65,
            'F_sharp_8/G_flat_8': 5919.91,
            'G8': 6271.93,
            'G_sharp_8/A_flat_8': 6644.88,
            'A8': 7040.00,
            'A_sharp_8/B_flat_8': 7458.62,
            'B8': 7902.13}

def get_key(base_note, scale='major'):
    """Returns a set of tones and their frequencies in either a major
    or a minor key

    Args:
        base_note (str): The key to play in, with an optional setting of
                         numbers to denote pitch of the key. 'C0' is an octave
                         lower than 'C1' for instance.
        scale (str, optional): Either minor or major. Defaults to 'major'.

    Returns:
        dict: dictionary of 
    """
    if base_note not in tone_map:
        if base_note + '4' in tone_map:
            base_note = base_note + '4'
        else:
            print(f'Base note {base_note} not in available notes.\n'
                  'Using C4 Major instead. (Middle C)')
            return get_key('C4', key_type='major')
    keys_in_order = list(tone_map.keys())
    index_of_base_key = keys_in_order.index(base_note)
    potential_keys = keys_in_order[index_of_base_key:]
    key_type_scale = [0, 2, 4, 5, 7, 9, 11, 12] if scale == 'major'\
        else [0, 2, 3, 5, 7, 8, 10, 12]
    keys_in_scale = [potential_keys[_] for _ in key_type_scale
                   if len(potential_keys) > _]
    returnable = {key: tone_map[key] for key in keys_in_scale}
    # this adds rest notes
    returnable[''] = 0.0
    return returnable
