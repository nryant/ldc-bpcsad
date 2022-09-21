# Copyright (c) 2012-2022, Trustees of the University of Pennsylvania
# Authors: nryant@ldc.upenn.edu (Neville Ryant)
# License: BSD 2-clause
"""Functions for reading/writing various segmentation file formats."""
from .audacity import load_audacity_label_file, write_audacity_label_file
from .htk import load_htk_label_file, write_htk_label_file
from .rttm import load_rttm_file, write_rttm_file
from .textgrid import write_textgrid_file

__all__ = ['load_audacity_label_file', 'load_htk_label_file', 'load_rttm_file',
           'write_audacity_label_file', 'write_htk_label_file',
           'write_rttm_file', 'write_textgrid_file']
