# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from openfisca_qt.plugins.utils import OutNode
from openfisca_qt.plugins.scenario.graph import drawBareme, drawWaterfall


def draw_waterfall(simulation, axes, visible = None):
    currency = simulation.tax_benefit_system.CURRENCY
    data = OutNode.init_from_decomposition_json(
        simulation = simulation,
        decomposiiton_json = None,
        )
    data.setLeavesVisible()
    if visible is not None:
        for code in visible:
            data[code].visible = 1
    axes.clear()
    drawWaterfall(data, axes, currency)


def draw_bareme(simulation, axes, x_axis, reform_simulation = None, visible_lines = None, hide_all = False):
    currency = simulation.tax_benefit_system.CURRENCY
    is_reform = False
    if reform_simulation is not None:
        data = OutNode.init_from_decomposition_json(
            simulation = reform_simulation,
            decomposiiton_json = None,
            )
        reference_data = OutNode.init_from_decomposition_json(
            simulation = simulation,
            decomposiiton_json = None,
            )
        is_reform = True
        data.difference(reference_data)
    else:
        data = OutNode.init_from_decomposition_json(
            simulation = simulation,
            decomposiiton_json = None,
            )
        reference_data = None
    data.setLeavesVisible()
    if visible_lines is not None:
        for code in visible_lines:
            data[code].visible = 1
            data[code].typevar = 2
    data[x_axis].setHidden(changeParent = True)
    if reform_simulation is not None and hide_all is True:
        data.hideAll()
    axes.clear()
    drawBareme(
        data,
        axes,
        x_axis,
        reform = is_reform,
        legend = True,
        reference_data = reference_data,
        currency = currency
        )
