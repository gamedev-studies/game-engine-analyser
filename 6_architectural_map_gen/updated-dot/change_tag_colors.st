|myTags result x|

x := MooseModel root at: 11.
myTags := x tags.

myTags do: [:item | 
	result := item name matchesRegex: '(.*)COR|(.*)EDI|(.*)LLR|(.*)PLA'.
	result
	ifTrue: [ item color: (Color fromHexString: '9c0f01ff') ] 
	ifFalse: [ item color: (Color fromHexString: 'fcdad7ff') ].

].
 