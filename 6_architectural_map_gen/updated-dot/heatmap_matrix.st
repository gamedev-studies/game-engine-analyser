|rows dotPath subsystems engines base decoded content count line tico|
base := '/home/gabrielullmann/Documents/game-engine-analyser/6_architectural_map_gen/updated-dot/dot/'.
engines := #('cocos2d' 'flaxengine' 'gameplay' 'godot' 'o3de' 'olc' 'panda3d' 'piccolo' 'unrealengine' 'urho3d').
subsystems := #('AUD' 'COR' 'DEB' 'EDI' 'FES' 'GMP' 'HID' 'LLR' 'OMP' 'PHY' 'PLA' 'RES' 'SDK' 'SGC' 'SKA' 'VFX').
line := ''.
subsystems do: [:source | 
	 Transcript show: source.
    subsystems do: [:target | 
        count := 0.
        engines do: [:eng | 
            dotPath := (base,eng,'.dot') asFileReference.
            content := dotPath contents.
            tico := content includesSubstring: (source,'"->"', target).
 				tico ifTrue: [count := count + 1].
        ].
        Transcript show: ',',(count asString).
    ].
    Transcript cr.
].