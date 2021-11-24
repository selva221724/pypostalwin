from subprocess import Popen, PIPE


def stringToJSON(string):
    if not string in ['{}']:
        string = string.replace('{  ', '')
        string = string.replace('}', '')
        string = string.replace('"', '')
        string = string.split(",  ")
        stringList = [i.split(': ') for i in string]
        outDictList = []
        for i in stringList:
            outDictList.append({i[0]: i[1].rstrip().lstrip()})
        return outDictList
    else:
        return {}


def outputStripper(result):
    result = result.split('Result:\n\n')[1].split('\n\n> ')[0].replace('\n', '')
    result = stringToJSON(result)
    return result


def removeSpeacialChars(address):
    b = {'≈': '', '≠': '', '>': '', '<': '', '+': '', '≥': '', '≤': '', '±': '', '*': '', '÷': '', '√': '',
         '°': '', '⊥': '', '~': '', 'Δ': '', 'π': '', '≡': '', '≜': '', '∝': '', '∞': '', '≪': '', '≫': '',
         '⌈': '', '⌉': '', '⌋': '', '⌊': '', '∑': '', '∏': '', 'γ': '', 'φ': '', '⊃': '', '⋂': '', '⋃': '',
         'μ': '', 'σ': '', 'ρ': '', 'λ': '', 'χ': '', '⊄': '', '⊆': '', '⊂': '', '⊇': '', '⊅': '', '⊖': '',
         '∈': '', '∉': '', '⊕': '', '⇒': '', '⇔': '', '↔': '', '∀': '', '∃': '', '∄': '', '∴': '', '∵': '',
         'ε': '', '∫': '', '∮': '', '∯': '', '∰': '', 'δ': '', 'ψ': '', 'Θ': '', 'θ': '', 'α': '', 'β': '',
         'ζ': '', 'η': '', 'ι': '', 'κ': '', 'ξ': '', 'τ': '', 'ω': '', '∇': ''}
    for x, y in b.items():
        address = address.replace(x, y)
    return address


class AddressParser:

    def __init__(self):
        self.exePath = r"C:\Workbench\libpostal\src\address_parser.exe"
        self.process = Popen(self.exePath, shell=False, universal_newlines=True,
                             stdin=PIPE, stdout=PIPE, stderr=PIPE)
        pass

    def runParser(self, address):
        address = removeSpeacialChars(address)
        address = address + '\n'
        self.process.stdin.write(address)
        self.process.stdin.flush()

        result = ''
        for line in self.process.stdout:
            if line == '}\n':
                result += line
                break
            result += line
        return outputStripper(result)

    def terminateParser(self):
        self.process.stdin.close()
        self.process.terminate()
        self.process.wait()
