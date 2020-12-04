import logging
import os
import re
from typing import List, Optional

logging.basicConfig(level=logging.DEBUG)


def read_input(input_path: str):
    input_file = open(input_path, "r")
    lines = input_file.readlines()

    result: List[str] = []
    for line in lines:
        result.append(line.strip())
    return result


_VALID_HCL_PATTERN = re.compile(r"^#[0-9a-f]{6}$")
_VALID_PID_PATTERN = re.compile(r"^[0-9]{9}$")


class Passport:
    def __init__(
        self,
        byr: Optional[str] = "",
        iyr: Optional[str] = "",
        eyr: Optional[str] = "",
        hgt: Optional[str] = "",
        hcl: Optional[str] = "",
        ecl: Optional[str] = "",
        pid: Optional[str] = "",
        cid: Optional[str] = "",
    ):
        """"""
        self._byr = byr
        self._iyr = iyr
        self._eyr = eyr
        self._hgt = hgt
        self._hcl = hcl
        self._ecl = ecl
        self._pid = pid
        self._cid = cid

    def is_valid_hgt(self) -> bool:
        if "cm" in self._hgt:
            return 150 <= int(self._hgt.replace("cm", "")) <= 193
        if "in" in self._hgt:
            return 59 <= int(self._hgt.replace("in", "")) <= 76
        return False

    def is_valid_hcl(self) -> bool:
        return bool(re.match(_VALID_HCL_PATTERN, self._hcl))

    def is_valid_pid(self) -> bool:
        return bool(re.match(_VALID_PID_PATTERN, self._pid))

    def has_valid_props(self) -> bool:
        req_props = [
            self._byr,
            self._iyr,
            self._eyr,
            self._hgt,
            self._hcl,
            self._ecl,
            self._pid,
        ]
        for p in req_props:
            if not bool(p):
                return False
        return True

    def has_valid_prop_values(self) -> bool:
        if not 1920 <= int(self._byr) <= 2002:
            logging.debug(f"invalid byr {self._byr}")
            return False
        if not 2010 <= int(self._iyr) <= 2020:
            logging.debug(f"invalid iyr {self._iyr}")
            return False
        if not 2020 <= int(self._eyr) <= 2030:
            logging.debug(f"invalid eyr {self._eyr}")
            return False
        if not self.is_valid_hgt():
            logging.debug(f"invalid hgt {self._hgt}")
            return False
        if not self.is_valid_hcl():
            logging.debug(f"invalid hcl {self._hcl}")
            return False
        if not self._ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            logging.debug(f"invalid ecl {self._ecl}")
            return False
        if not self.is_valid_pid():
            logging.debug(f"invalid pid {self._pid}")
            return False
        return True


def parse_rows(rows: List[str]) -> List[List[str]]:
    """"""
    parsed: List[List[str]] = []
    current: List[str] = []
    for row in rows:
        if row == "":
            parsed.append(current)
            current = []
            continue
        current.append(row)
    parsed.append(current)
    return parsed


def parse_passport(rows: List[str]) -> Passport:
    """"""
    res = dict()
    for row in rows:
        try:
            split_res = row.split(" ")
            for sr in split_res:
                key, value = sr.split(":")
                res[key] = value
        except ValueError as e:
            logging.error(f"{e}")
    return Passport(
        byr=res.get("byr", ""),
        iyr=res.get("iyr", ""),
        eyr=res.get("eyr", ""),
        hgt=res.get("hgt", ""),
        hcl=res.get("hcl", ""),
        ecl=res.get("ecl", ""),
        pid=res.get("pid", ""),
        cid=res.get("cid", ""),
    )


def run_1():
    input_filepath = input_filepath = os.path.join(
        os.path.dirname(__file__), "input.txt"
    )
    entries = read_input(input_filepath)
    raw_pps = parse_rows(entries)
    passports = [parse_passport(pp_raw) for pp_raw in raw_pps]
    valid_passports = [pp for pp in passports if pp.has_valid_props()]
    logging.debug(f"{len(valid_passports)} valid passports of {len(passports)}.")


def run_2():
    input_filepath = input_filepath = os.path.join(
        os.path.dirname(__file__), "input.txt"
    )
    entries = read_input(input_filepath)
    raw_pps = parse_rows(entries)
    passports = [parse_passport(pp_raw) for pp_raw in raw_pps]
    valid_passports = [
        pp for pp in passports if pp.has_valid_props() and pp.has_valid_prop_values()
    ]
    logging.debug(f"{len(valid_passports)} valid passports of {len(passports)}.")


if __name__ == "__main__":
    run_2()