|rows csvPath sum avg engines|
engines := #('cocos2d' 'flaxengine' 'gameplay' 'godot' 'o3de' 'olc' 'panda3d' 'piccolo' 'unrealengine' 'urho3d').

sum := 0.
avg := 0.
engines do: [:en | csvPath := '/home/gabrielullmann/Documents/game-engine-analyser/6_architectural_map_gen/updated-dot/gephi-metrics/' , en, '.csv'.
rows := (csvPath asFileReference readStreamDo: [ :stream | 
				               (NeoCSVReader on: stream readStream)
				                  separator: $;;
										addField;
										addField;
										addField;
										addIntegerField;
										addIntegerField;
										addFloatField;
					               upToEnd ]) sliceFrom: 1.
rows := rows select: [ :item | (item at: 1) matchesRegex: '^((?!OTH).)*$' ].
rows := rows select: [ :item | (item at: 1) matchesRegex: '(.*)VFX' . ].

rows isNotEmpty ifTrue: [ 
	rows := rows first.
	rows size >= 4 ifTrue: [ Transcript show: (rows at: 4). Transcript show: '	'.]
	ifFalse: [ Transcript show: '0'. Transcript show: '	'.]
]
ifFalse: [ Transcript show: '0'. Transcript show: '	'.].
].
Transcript cr.

