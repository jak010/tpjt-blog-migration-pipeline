from datetime import date


class MarkDownExportTemplate:

    def __init__(self, file_name, file_content):
        self.file_name = file_name
        self.file_content = file_content
        self.file_ext = "md"

    @property
    def get_file_name(self):
        current_date = date.today()
        return f"{current_date}-{self.file_name}.{self.file_ext}"

    def execute(self):
        with open(self.get_file_name, "a") as f:
            f.write(self.file_content)
