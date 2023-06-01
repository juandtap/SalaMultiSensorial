# codigo para agregar gtk3 al .exe creado con pyinstaller
# se usa gtk3 para generar reportes en formato .pdf

from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all('gi.repository.Gtk')
