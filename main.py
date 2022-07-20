import art
import pdfplumber
from pathlib import Path
from googletrans import Translator, constants
from pprint import pprint


def pdf_to_txt(fp):
    if fp.is_file():
        if fp.suffix != '.pdf':
            print(f'Error - the file \033[1;32m{fp}\033[0m is not pdf!')
        with pdfplumber.open(fp) as pdf:
            translator = Translator()
            pages = [page.extract_text() for page in pdf.pages]
            for i in pages:
                with open(str(fp.parent) + '\\pdf_to_txt.txt', 'a', encoding='utf-8') as file_txt:
                    translation = translator.translate(i)
                    file_txt.write(translation.origin + "\n" + translation.text)
    else:
        print(f'Error - the path \033[1;32m{fp}\033[0m is invalid!')


def main():
    art.tprint("pdf_to_txt")
    fp = Path(input("[+] input path to the file:").strip())
    pdf_to_txt(fp)




if __name__ == '__main__':
    main()
