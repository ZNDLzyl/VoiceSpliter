# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\Code\\PycharmProjects\\VoiceSpliter\\Start\\MainStart.py',
'D:\\Code\\PycharmProjects\\VoiceSpliter\\VoiceHandler\\VoiceSegment.py',
'D:\\Code\\PycharmProjects\\VoiceSpliter\\UI\\EnglishCarefullListener.py',
'D:\\Code\\PycharmProjects\\VoiceSpliter\\UI\\EnglishCarefullListenerH.py',
'D:\\Code\\PycharmProjects\\VoiceSpliter\\UI\\PlaySoundForm.py'
            ],
             pathex=['D:\\Code\\PycharmProjects\\VoiceSpliter'],
             binaries=[],
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
          name='MainStart',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
