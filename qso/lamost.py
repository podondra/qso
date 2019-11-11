from os import path

import pandas as pd


def read_general_catalog(catalog_path):
    return pd.read_csv(
	catalog_path,
	dtype={"offsets": "bool"},
	index_col="obsid",
	low_memory=False,
	na_values={
	    'z': -9999.0,
	    "z_err": -9999.0,
	    "snru": -9999.0,
	    "snrg": -9999.0,
	    "snrr": -9999.0,
	    "snri": -9999.0,
	    "snrz": -9999.0,
	    "offset_v": 99.0
	},
	parse_dates=["obsdate"],
	sep='|',
    )


def get_spec_filename(spec):
    lmjd = spec["lmjd"]
    planid = spec["planid"]
    spid = spec["spid"]
    fiberid = spec["fiberid"]
    filename_str = "spec-{}-{}_sp{:02d}-{:03d}.fits.gz"
    return filename_str.format(lmjd, planid, spid, fiberid)


def get_spec_filepath(spec, filename):
    planid = spec["planid"]
    obsdate = spec["obsdate"].strftime("%Y%m%d")
    return path.join(obsdate, planid, filename)
