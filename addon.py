import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
cmd = addon.getSetting("cmd")

if(xbmcgui.Dialog().yesno(addonname, "Run command?", cmd)):
    xbmc.executebuiltin('System.Exec(' + cmd + ')')