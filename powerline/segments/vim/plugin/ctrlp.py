# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

try:
	import vim
except ImportError:
	vim = object()

from powerline.bindings.vim import vim_getvar


def marked(pl):
	'''Returns boolean indicating whether anything is marked or not.

	Highlight groups used: ``ctrlp:marked``.
	'''
	status = vim_getvar('_powerline_ctrlp_status')
	if 'prog' in status:
		return None
	return None if status['marked'] == ' <->' else [{
		'highlight_groups': ['ctrlp:marked'],
		'contents': status['marked'].strip()
	}]


def mode(pl):
	'''Returns current mode.

	Highlight groups used: ``ctrlp:status``.
	'''
	status = vim_getvar('_powerline_ctrlp_status')
	if 'prog' in status:
		return None
	return [{
		'highlight_groups': ['ctrlp:status'],
		'contents': ' ' + status['item'] + ' '
	}]


def mode_prev(pl):
	'''Returns previous mode.

	Highlight groups used: ``ctrlp:status_other``.
	'''
	status = vim_getvar('_powerline_ctrlp_status')
	if 'prog' in status:
		return None
	return [{
		'highlight_groups': ['ctrlp:status_other'],
		'contents': status['prev'] + ' '
	}]


def mode_next(pl):
	'''Returns next mode.

	Highlight groups used: ``ctrlp:status_other``.
	'''
	status = vim_getvar('_powerline_ctrlp_status')
	if 'prog' in status:
		return None
	return [{
		'highlight_groups': ['ctrlp:status_other'],
		'contents': ' ' + status['next'] + ' '
	}]


def prog(pl):
	'''Returns progress status.

	Highlight groups used: ``ctrlp:prog``.
	'''
	status = vim_getvar('_powerline_ctrlp_status')
	if 'prog' not in status:
		return None
	return [{
		'highlight_groups': ['ctrlp:prog'],
		'contents': status['prog']
	}]
