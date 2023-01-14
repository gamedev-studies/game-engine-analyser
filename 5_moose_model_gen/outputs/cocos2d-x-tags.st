|model foldersTags tagsColors files modelFolders projName|
projName := 'cocos2d-x'.
model := MooseModel root at: x.
foldersTags := Dictionary newFrom: {
'audio' -> 'AUD' .'base' -> 'COR' .'math' -> 'COR' .'cocostudio' -> 'EDI' .'ui' -> 'FES' .'GUI' -> 'FES' .'scripting' -> 'GMP' .'renderer' -> 'LLR' .'network' -> 'OMP' .'physics' -> 'PHY' .'physics3d' -> 'PHY' .'physics-nodes' -> 'PHY' .'platform' -> 'PLA' .'templates' -> 'PLA' .'assets-manager' -> 'RES' .'spine' -> 'SKA' .'2d' -> 'VFX' .'3d' -> 'VFX' .'Particle3D' -> 'VFX' .}.
tagsColors := Dictionary newFrom: { 'AUD' -> '#f0e442'. 'OMP' -> '#ff0000'. 'HID' -> '#ea9999'. 'DEB' -> '#cccccc'. 'SGC' -> '#009e73'. 'LLR' -> '#00b816'. 'VFX' -> '#b8f100'. 'FES' -> '#6de900'. 'PLA' -> '#8288f1'. 'GMP' -> '#af93f8'. 'SDK' -> '#f8beff'. 'SKA' -> '#fce5cd'. 'PHY' -> '#fbbc04'. 'RES' -> '#efefef'. 'COR' -> '#4fc8e5'. 'EDI' -> '#56b4e9' }.
modelFolders := model allWithType: FamixCPreprocFolder.
tagsColors keys do: [ :key | (model tagNamed: projName , '-' , key) color: (Color fromHexString: (tagsColors at: key))].
foldersTags keys do: [ :key | (modelFolders select: [:file | file name = key]) do: [ :file | file tagWith: (model tagNamed: projName , '-' ,(foldersTags at: key))] ].