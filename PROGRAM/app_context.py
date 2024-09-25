import os
import sys

from PROGRAM.typing import AppContext


def detect_app_context() -> AppContext:
	frame = sys._getframe(1)

	while frame:
		if os.path.join('PROGRAM', 'jobs') in frame.f_code.co_filename:
			return 'cli'
		if os.path.join('PROGRAM', 'uis') in frame.f_code.co_filename:
			return 'ui'
		frame = frame.f_back
	return 'cli'
