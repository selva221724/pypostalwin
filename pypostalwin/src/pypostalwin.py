import subprocess
import json
import os
import logging


class AddressParser:
    def __init__(self, address_parser_path, libpostal_path):
        self.address_parser_path = self._validate_file(address_parser_path, "Address parser")
        self.libpostal_path = self._validate_file(libpostal_path, "Libpostal")

    @staticmethod
    def _validate_file(file_path, name):
        if not os.path.isfile(file_path) or not os.access(file_path, os.X_OK):
            raise ValueError(f"{name} path is not a valid executable file: {file_path}")
        return file_path

    @staticmethod
    def _validate_address(address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Address must be a non-empty string")

    @staticmethod
    def _remove_special_chars(address):
        special_chars = r"≈≠><+≥≤±*÷√°⊥~Δπ≡≜∝∞≪≫⌈⌉⌋⌊∑∏γφ⊃⋂⋃μσρλχ⊄⊆⊂⊇⊅⊖∈∉⊕⇒⇔↔∀∃∄∴∵ε∫∮∯∰δψΘθαβζηικξτω∇’"
        translator = str.maketrans("", "", special_chars)
        return address.translate(translator)

    def _run_command(self, command, input_data=None):
        try:
            process = subprocess.Popen(command, shell=False, universal_newlines=True,
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(input_data)
            return stdout.strip()

        except subprocess.CalledProcessError as e:
            logging.exception("Error occurred during command execution: %s", e)
            raise

    def parse_address(self, address):
        self._validate_address(address)
        address = self._remove_special_chars(address)
        address = address + '\n'
        command = [self.address_parser_path]
        result = self._run_command(command, input_data=address)
        json_start = result.find('{')
        json_end = result.rfind('}') + 1
        json_data = result[json_start:json_end]
        return json.loads(json_data)

    def expand_address(self, address):
        self._validate_address(address)
        address = self._remove_special_chars(address)
        command = [self.libpostal_path, address, '--json']
        result = self._run_command(command)
        json_data = json.loads(result)
        return json_data.get("expansions", [])

    def terminate_parser(self):
        pass


if __name__ == '__main__':
    address_parser_path = r'C:\Workbench\libpostal\src\address_parser.exe'
    libpostal_path = r'C:\Workbench\libpostal\src\libpostal.exe'

    logging.basicConfig(level=logging.INFO)

    parser = AddressParser(address_parser_path, libpostal_path)

    address = 'District Science Cntr, Kokkirakulam’ Rd, Tirunelveli, Tamil Nadu 627009'
    try:
        parsed_address = parser.parse_address(address)
        logging.info("Parsed Address: %s", parsed_address)
    except (FileNotFoundError, RuntimeError) as e:
        logging.exception("Failed to parse address: %s", e)

    try:
        expanded_address = parser.expand_address(address)
        logging.info("Expanded Address: %s", expanded_address)
    except (FileNotFoundError, RuntimeError) as e:
        logging.exception("Failed to expand address: %s", e)
