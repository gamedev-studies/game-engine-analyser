|rows dotPath subsystems engines base decoded content count line fileLine|
base := '/home/gabrielullmann/Documents/game-engine-analyser/6_architectural_map_gen/updated-dot/dot/'.
engines := #('cocos2d' 'flaxengine' 'gameplay' 'godot' 'o3de' 'olc' 'panda3d' 'piccolo' 'unrealengine' 'urho3d').
subsystems := #('AUD' 'COR' 'DEB' 'EDI' 'FES' 'GMP' 'HID' 'LLR' 'OMP' 'PHY' 'PLA' 'RES' 'SDK' 'SGC' 'SKA' 'VFX').
line := ''.
subsystems do: [:source | 
    subsystems do: [:target | 
        count := 0.
        engines do: [:eng | 
            dotPath := (base,eng,'.dot') asFileReference.
            content := dotPath contents.
            fileLine := content includesSubstring: (source,'"->"', target).
 				fileLine ifTrue: [count := count + 1].
        ].
		Transcript show: (source,'->', target).
        Transcript show: ',',(count asString).
        Transcript cr.
    ].
].



				