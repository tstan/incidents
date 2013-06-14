import os
import itertools


class LogFile():
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return "<LogFile '{}'>".format(self.path)

    @staticmethod
    def _good_line(line):
        fields = line.split("|")
        return len(fields) > 9 and fields[7] and fields[8]
    
    @property
    def lines(self):
        with open(self.path) as open_file:
            return [line.strip() for line in open_file if self._good_line(line)]

class LogDir():
    def __init__(self, path):
        self.path = os.path.join(path, "")
        self.files = [LogFile(self.path + l) for l in os.listdir(path)]

    def __repr__(self):
        return "<LogDir '{}'>".format(self.log_dir)

    @property
    def lines(self):
        for file_ in self.files:
            for line in file_.lines:
                yield line

    @property
    def uniq_lines(self):
        lam = lambda line: line.split("|")[1]
        all_lines = self.lines
        sorted_lines = sorted(all_lines, key=lam)
        grouped_lines = itertools.groupby(sorted_lines, lam)
        return (max(g) for k, g in grouped_lines)

class Incident():
    pass

LOG_DIR = "raw"

log_dir = LogDir(LOG_DIR)

for line in log_dir.uniq_lines:
    print(line)
