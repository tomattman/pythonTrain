class Translation():
    def __init__(self, dict):
        self.package_name = dict.pop("package_name", "translations")
        self.package_group = dict.pop("package_group", "apps.sapdx.i18n.forms")

        self.translations = []
        for key, value in dict.items():
            self.translations.append(value)
