from dataclasses import dataclass, field
import argparse
from pathlib import Path


parser = argparse.ArgumentParser(
    description='Find domain names from your monitored browsing.')
parser.add_argument('-i', '--input', type=str, default='dump', required=True, help='Relative path of input file')
parser.add_argument('-kw', '--keyword_list', nargs='+', default=[''], help='Searching parameters, default empty lists out every domain')

args = parser.parse_args()



@dataclass
class PackageItem:
    domain: list[str] = field(default_factory=list)
    ips: list[str] = field(default_factory=list)


items: list[PackageItem] = []

inputFile = Path(args.input).resolve()
with open(inputFile) as f:
    lines = f.readlines()
    for l in lines:
        for keyword in args.keyword_list:
            # filter empty or incomplete rows
            # filter outgoing packets, has no real data for us
            if keyword in l and (l.split('\t')[0] != '') and ('192' not in l.split('\t')[0]):
                formattedLine = l.strip().split('\t')
                # filter out empty empty columns
                rawItem = list(filter(None, formattedLine[3:7]))
                # index 1 might not be present
                tmpItem = PackageItem(domain=list(set(rawItem[0].split(','))), ips=list(
                    set(rawItem[1].split(','))) if 1 < len(rawItem) else [])
                items.append(tmpItem)

domains = []
# get unique domain names
for item in items:
    for d in item.domain:
        domains.append(d)
# print without quotes
print(*list(set(domains)), sep='\n')
