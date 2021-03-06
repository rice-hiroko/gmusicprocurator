# -*- coding: utf-8 -*-
#
# Copyright (C) 2014  Mark Lee
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Flask view module loader for GMusicProcurator."""

from ..app import app, heapy
from . import proxy  # noqa
if app.config['GMP_CHROMECAST_ENABLED']:
    from . import chromecast  # noqa
if app.config['GMP_FRONTEND_ENABLED']:
    from . import ui  # noqa
    if heapy:
        from . import debug  # noqa
