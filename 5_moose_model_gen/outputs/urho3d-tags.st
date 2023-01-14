|model foldersTags tagsColors files modelFolders projName|
projName := 'urho3d'.
model := MooseModel root at: x.
foldersTags := Dictionary newFrom: {
'include/Urho3D/AngelScript' -> 'GMP' .'include/Urho3D/Audio' -> 'AUD' .'include/Urho3D/Base' -> 'COR' .'include/Urho3D/Container' -> 'COR' .'include/Urho3D/Core' -> 'COR' .'include/Urho3D/Engine' -> 'COR' .'include/Urho3D/Graphics' -> 'LLR' .'include/Urho3D/GraphicsAPI' -> 'LLR' .'include/Urho3D/IK' -> 'SKA' .'include/Urho3D/Input' -> 'HID' .'include/Urho3D/IO' -> 'COR' .'include/Urho3D/LuaScript' -> 'GMP' .'include/Urho3D/Math' -> 'COR' .'include/Urho3D/Network' -> 'OMP' .'include/Urho3D/Physics' -> 'PHY' .'include/Urho3D/Physics2D' -> 'PHY' .'include/Urho3D/Resources' -> 'RES' .'include/Urho3D/Scene' -> 'SGC' .'include/Urho3D/UI' -> 'FES' .'include/Urho3D/Urho2D' -> 'LLR' .'Source/Urho3D/AngelScript' -> 'GMP' .'Source/Urho3D/Audio' -> 'AUD' .'Source/Urho3D/Base' -> 'COR' .'Source/Urho3D/Container' -> 'COR' .'Source/Urho3D/Core' -> 'COR' .'Source/Urho3D/Engine' -> 'COR' .'Source/Urho3D/Graphics' -> 'LLR' .'Source/Urho3D/GraphicsAPI' -> 'LLR' .'Source/Urho3D/IK' -> 'SKA' .'Source/Urho3D/Input' -> 'HID' .'Source/Urho3D/IO' -> 'COR' .'Source/Urho3D/LuaScript' -> 'GMP' .'Source/Urho3D/Math' -> 'COR' .'Source/Urho3D/Network' -> 'OMP' .'Source/Urho3D/Physics' -> 'PHY' .'Source/Urho3D/Physics2D' -> 'PHY' .'Source/Urho3D/Resources' -> 'RES' .'Source/Urho3D/Scene' -> 'SGC' .'Source/Urho3D/UI' -> 'FES' .'Source/Urho3D/Urho2D' -> 'LLR' .'ThirdParty' -> 'SDK' .}.
tagsColors := Dictionary newFrom: { 'AUD' -> '#f0e442'. 'OMP' -> '#ff0000'. 'HID' -> '#ea9999'. 'DEB' -> '#cccccc'. 'SGC' -> '#009e73'. 'LLR' -> '#00b816'. 'VFX' -> '#b8f100'. 'FES' -> '#6de900'. 'PLA' -> '#8288f1'. 'GMP' -> '#af93f8'. 'SDK' -> '#f8beff'. 'SKA' -> '#fce5cd'. 'PHY' -> '#fbbc04'. 'RES' -> '#efefef'. 'COR' -> '#4fc8e5'. 'EDI' -> '#56b4e9' }.
modelFolders := model allWithType: FamixCPreprocFolder.
tagsColors keys do: [ :key | (model tagNamed: projName , '-' , key) color: (Color fromHexString: (tagsColors at: key))].

foldersTags keys do: [ 
    :key | key includes: $/
        ifTrue: [
            splitted := key splitOn: '/'.
            filteredFolders := modelFolders
            filteredFolders := modelFolders select: [:fd2 | fd2 name = splitted last]
            filteredFolders do: [ :x |
                hasParent := (x allDeclaredProperties select: [ :each | 
                            each name = 'parentFolder' ]) size.
                hasParent >= 1
                ifTrue: [ 
                    x parentNode name = splitted at: (splitted size) - 1 
                    ifTrue: [ 
                        :x | x tagWith: (model tagNamed: projName , '-' ,(foldersTags at: key))
                    ]
                ]
            ]
        
        ],
        ifFalse: [
            (modelFolders select: [:folder | folder name = key])
            do: [ 
                :folder | folder tagWith: (model tagNamed: projName , '-' ,(foldersTags at: key))
            ]
        ]
]

"foldersTags keys do: [ :key | (modelFolders select: [:file | file name = key]) do: [ :file | file tagWith: (model tagNamed: projName , '-' ,(foldersTags at: key))] ]."