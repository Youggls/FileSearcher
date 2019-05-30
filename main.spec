# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/Raymond/Documents/GitHub/FileSearcher'],
             binaries=[('./bin/config.json', 'bin')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='FileSearcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='FileSearcher.app',
             icon='DVA.icns',
             bundle_identifier=None),
             info_plist={
                'CFBundleName': "FileSearcher",
                'CFBundleDisplayName': "FileSearcher",
                'CFBundleGetInfoString': "Youggls & RaymondY",
                'CFBundleIdentifier': "com.uinote.FileSearcher",
                'CFBundleVersion': "0.0.1",
                'CFBundleShortVersionString': "0.0.1",
                'NSHighResolutionCapable': True,
                'NSHumanReadableCopyright': u"Copyright © 2019, UINOTE, All Rights Reserved"
            })
