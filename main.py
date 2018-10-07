from utils.auth import login
from utils.problem import ProblemSystem
import json

record_filepath = 'data/record.json'
record = json.load(open(record_filepath))

min_value = min(record.values())

for cls in record:
    cookies = login("crack" + cls, "1358282318")

    if record[cls] >= min_value + 5:
        continue

    cur = 0
    while cur < 5:
        try:
            ps = ProblemSystem(record[cls])
            ps.ac(cookies)
            if ps.score > 10:
                cur += 1
            print("{} [{}] {}".format(cls, ps.title, ps.score))
        except:
            pass
        finally:
            record[cls] += 1
    json.dump(record, open(record_filepath, 'w'), indent=4)
