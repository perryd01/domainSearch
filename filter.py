import sys
from dataclasses import dataclass, field

args = sys.argv[1:]


@dataclass
class PackageItem:
    domain: list[str] = field(default_factory=list)
    ips: list[str] = field(default_factory=list)


items: list[PackageItem] = []

with open(args[0]) as f:
    lines = f.readlines()
    for l in lines:
        for keyword in args[1].split(','):
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
