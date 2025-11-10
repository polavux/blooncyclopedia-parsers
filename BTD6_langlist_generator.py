import xml.etree.ElementTree as ET
import pyperclip
import argparse

def n(lang, key):
    root = ET.parse(lang + ".xml",parser=ET.XMLParser(encoding="utf-8")).getroot()
    for parent_node in root[0]:
        for child_node in parent_node:
            if child_node.attrib["id"] == key: return child_node.text

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("key", type=str, help="The localization key (enclose it in quotation marks if it contains any spaces)")
    parser.add_argument("--label", type=str, help="Adds a label to the langlist")
    parser.add_argument("--collapsed", action="store_true", help="Flags the langlist as collapsed by default")

    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    output = f"""{{{{langlist
|key={args.key}
|label={args.label if args.label else ""}
|collapsed={args.collapsed if args.collapsed else ""}
|ar   ={n("Arabic", args.key)}
|da   ={n("Danish", args.key)}
|de   ={n("German", args.key)}
|es   ={n("Spanish", args.key)}
|es-la={n("Spanish (LATAM)", args.key)}
|fi   ={n("Finnish", args.key)}
|fr   ={n("French", args.key)}
|it   ={n("Italian", args.key)}
|ja   ={n("Japanese", args.key)}
|ko   ={n("Korean", args.key)}
|nl   ={n("Dutch", args.key)}
|no   ={n("Norwegian", args.key)}
|pl   ={n("Polish", args.key)}
|pt-br={n("Portuguese (Brazil)", args.key)}
|ru   ={n("Russian", args.key)}
|sv   ={n("Swedish", args.key)}
|th   ={n("Thai", args.key)}
|tr   ={n("Turkish", args.key)}
|zh-cn={n("ChineseSimplified", args.key)}
|zh-tw={n("ChineseTraditional", args.key)}
}}}}"""

    print()
    print(output)
    pyperclip.copy(output)