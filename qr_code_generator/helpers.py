#!/usr/bin/env python3
import yaml


class Config(dict):
    """
    Configuration class, behaves just like a dict
    """
    def __init__(self, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)

        # Basic configuration values
        self['API_URI'] = 'https://api.qr-code-generator.com/v1/create?'
        self['FORCE_OVERWRITE'] = False
        self['REQUIRED_PARAMETERS'] = [
            'access-token',
            'qr_code_text'
        ]
        self['OUT_FOLDER'] = 'out'
        self['OUTPUT_FOLDER'] = 'output'
        self['VERBOSE'] = False

    def load(self, file):
        """
        Load a .yaml file into the current configuration object.

        Parameters
        ----------
        file : str
            The relative location of the file that should be used to import settings.

        Returns
        -------
        None
        """
        settings = load_yaml(file)

        for key, value in settings.items():
            self.set(key, value)


class Settings(dict):
    """
    Settings class, behaves just like a dict
    """
    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)

        # Default settings for QR code generation
        self['access_token'] = None
        self['qr_code_text'] = None
        self['image_format'] = 'SVG'
        self['image_width'] = 500
        self['download'] = 0
        self['foreground_color'] = '#000000'
        self['background_color'] = '#FFFFFF'
        self['marker_left_inner_color'] = '#000000'
        self['marker_left_outer_color'] = '#000000'
        self['marker_right_inner_color'] = '#000000'
        self['marker_right_outer_color'] = '#000000'
        self['marker_bottom_inner_color'] = '#000000'
        self['marker_bottom_outer_color'] = '#000000'
        self['marker_left_template'] = 'version1'
        self['marker_right_template'] = 'version1'
        self['marker_bottom_template'] = 'version1'
        self['qr_code_logo'] = 'no-logo'
        self['frame_color'] = '#000000'
        self['frame_text'] = None
        self['frame_text_color'] = '#ffffff'
        self['frame_icon_name'] = 'app'
        self['frame_name'] = 'no-frame'

    def load(self, file):
        settings = load_yaml(file)

        for key, value in settings.items():
            self.set(key, value)


def is_yaml(file):
    extension = file.split('.')[-1]
    if not extension == 'yaml':
        return False
    return True


def load_yaml(file):
    if not is_yaml(file):
        raise ValueError()

    with open(file, "r") as f:
        items = yaml.load(f, Loader=yaml.FullLoader)

    return items
