setDependencies
    "this code goes in MiArchitecturalMap"
	| dict |
	tagNodes do: [ :tagNode | self setDependenciesForTag: tagNode ].
	allEntities do: [ :e | self setDependenciesForEntity: e ].

	dict := Dictionary new.
	tagNodes do: [ :each | 
		dict at: each name put: each rawModel getOutgoing ].
	Transcript show: 'asubsystem,'.
	tagNodes do: [ :each | Transcript show: each name , ',' ].
	tagNodes do: [ :each | 
		(dict includesKey: each name) ifTrue: [ 
			Transcript cr.
			Transcript show: each.
			tagNodes do: [ :each2 | "1halt."
				((dict at: each name) includes: each2 name)
					ifTrue: [ Transcript show: ',1' ]
					ifFalse: [ Transcript show: ',0' ] ] ] ]