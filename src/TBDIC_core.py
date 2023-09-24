class TBDIC_core:
    def __init__(self):
        pass

    def handleCommandText(self, command_text: list):
        """
        This function handles the command text.
        """

        for index, line in enumerate(command_text):
            if 'exit' or 'close' in line:
                return -1

            line = self.sliceTextLine(line)
            command_text[index] = line

        return command_text

    def sliceTextLine(self, text_line: str) -> list:
        return re.split(r'(\s)', text_line)
