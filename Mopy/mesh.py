# -*- coding: cp1252 -*-
#
# mesh.py
#
# Extension for Wrye Mash 0.8.4
#
# (c) D.C.-G. <00:06 14/07/2010>
#
# Published under the exact same terms as the other files of Wrye Mash.
#
# SettingsWindow objects
#
import wx

from mosh import _

class SettingsWindow(wx.MiniFrame):
	"""Class for the settings window."""
	# defining some variables before initialisation
	settings = None
	init = True

	def __init__(self, parent=None, id=-1, size=(wx.DefaultSize[0],-1), pos = wx.DefaultPosition,
				style=wx.DEFAULT_FRAME_STYLE, settings=None):
		"""..."""
		wx.MiniFrame.__init__(self, parent=parent, id=id, size=size, pos=pos, style=style)
		self.EnableCloseButton(False)
		self.SetTitle(_("Wrye Mash Settings"))
		if settings != None:
			self.settings = settings
		else:
			self.settings = {}
		p = self.Panel = wx.Panel(self)
		# components and sizers
		btnOK = wx.Button(p, wx.ID_OK, _("Ok"), name="btnOK")
		btnCancel = wx.Button(p, wx.ID_CANCEL, _("Cancel"), name="btnCancel")
		btnBrowseMw = wx.Button(p, wx.ID_OPEN, _("..."), size=(-1,-1))
		boxMwDir = wx.StaticBox(p, -1, _("Morrowind directory"))
		self.fldMwDir = wx.TextCtrl(p, -1)
		sizerBoxMwDir = wx.StaticBoxSizer(boxMwDir, wx.HORIZONTAL)
		sizerBoxMwDir.AddMany([(self.fldMwDir,1,wx.EXPAND),((2,0)),(btnBrowseMw,0)])
		sizerBoxInstallersDir = wx.BoxSizer(wx.VERTICAL)
		sizerFields = wx.BoxSizer(wx.VERTICAL)
		sizerFields.AddMany([(sizerBoxMwDir,0,wx.EXPAND),((0,2)),(sizerBoxInstallersDir,0,wx.EXPAND)])
		sizerBtn = wx.BoxSizer(wx.HORIZONTAL)
		sizerBtn.AddMany([(btnOK),((2,0),0,wx.EXPAND),(btnCancel)])
		sizerWin = wx.BoxSizer(wx.VERTICAL)
		sizerWin.AddMany([(sizerFields,0,wx.EXPAND),((0,2)),(sizerBtn)])
		p.SetSizer(sizerWin)
		sizer = wx.BoxSizer()
		sizer.Add(p,1,wx.EXPAND)
		self.SetSizer(sizer)
		sizer.Fit(p)
		self.SetSizeHints(self.GetSize()[0], sizerWin.Size[1])
		self.Fit()
		wx.EVT_BUTTON(self, wx.ID_CANCEL, self.OnCancel)
		wx.EVT_BUTTON(self, wx.ID_OK, self.OnOk)
		wx.EVT_BUTTON(self, wx.ID_OPEN, self.OnBrowseMw)
		wx.EVT_SIZE(self, self.OnSize)

	def OnSize(self, event):
		"""..."""
		self.Layout()
		if self.init == True:
			self.SetSizeHints(*self.GetSize())
			self.init = False

	def OnBrowseMw(self, event):
		"""Chosing Morrowind directory."""
		dialog = wx.DirDialog(self, _("Morrowind directory selection"))
		if dialog.ShowModal() != wx.ID_OK:
			dialog.Destroy()
			return
		path = dialog.GetPath()
		dialog.Destroy()
		self.fldMwDir.SetValue(path)

	def OnCancel(self, event):
		"""Cancel button handler."""
		self.Close()

	def OnOk(self, event):
		"""Ok button handler."""
		self.settings["mwDir"] = self.fldMwDir.GetValue()
		self.Close()

	def Close(self):
		"""..."""
		self.settings["mash.settings.show"] = False
		# self.settings.save()
		wx.MiniFrame.Close(self)

	def SetSettings(self, settings):
		"""External settings change."""
		self.settings = settings
		self.fldMwDir.SetValue(settings["mwDir"])
