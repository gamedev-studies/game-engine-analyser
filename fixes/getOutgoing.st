"Adhoc code, FamixTag"

getOutgoing
	"Nicolas and Gabriel, 2022-2023"
	"Returns a list of all tags this tag depends on according to the arch map. This version works when only files are tagged, not folders"

	| taggedFolders tagsOutgoing tagFound opposites|
	tagsOutgoing := OrderedCollection new.
	opposites := (self taggedEntities flatCollect: [ :each | 
		                  each queryAllOutgoing opposites ]).
	taggedFolders := (opposites collect:
		                 [ :each | each parentFolder ]) asSet asArray.

	taggedFolders do: [ :each | 
		tagFound := self getOutgoingSearch: each fallback: self.
		"tagFound name ~= self mooseName ifTrue: [ tagsOutgoing add: tagFound name ] ]."
		tagsOutgoing add: tagFound name ].
	^ tagsOutgoing asSet

getOutgoing
	"Gabriel, 2023"
	"Returns a list of all tags this tag depends on according to the arch map"

	| taggedEntities tagsOutgoing tagFound opposites |
	tagsOutgoing := OrderedCollection new.

	opposites := self taggedEntities flatCollect: [ :each | 
		       each queryAllOutgoing opposites ].
	taggedEntities := opposites asSet asArray.

	taggedEntities do: [ :each | 
		tagFound := self getOutgoingSearch: each fallback: self.
		tagsOutgoing add: tagFound name ].
	^ tagsOutgoing asSet

getOutgoingSearch: file fallback: fallbackTag
	"Nicolas and Gabriel, 2022-2023"
	"Receives a file as input. If it has a tag return the tag, otherwise go up in the file hierarchy until finding a tag. If no tag is found, return callback"

	| hasParent |
	file className = 'FamixCPreprocFolder'
		ifTrue: [ 
			file tags size = 1
				ifTrue: [ ^ file tags at: 1 ]
				ifFalse: [ ^ fallbackTag ] ]
		ifFalse: [ 
			hasParent := (file allDeclaredProperties select: [ :each | 
				              each name = 'parentFolder' ]) size.
			hasParent >= 1
				ifTrue: [ 
				^ self getOutgoingSearch: file parentFolder fallback: fallbackTag ]
				ifFalse: [ ^ fallbackTag ] ]

getOutgoingSearch: entity fallback: fallbackTag

	"Gabriel, 2023"
	"Receives a file as input. If it has a tag return the tag, otherwise go up in the file hierarchy until finding a tag. If no tag is found, return callback"

	| hasParent |
	entity ifNil: [ ^ fallbackTag ].
	entity tags isNotEmpty
		ifTrue: [ ^ entity tags first ]
		ifFalse: [ 
			hasParent := entity allDeclaredProperties select: [ :each | 
				             each name = 'parentFolder' ].
			hasParent isNotEmpty
				ifTrue: [ 
				^ self
					  getOutgoingSearch: entity parentFolder
					  fallback: fallbackTag ]
				ifFalse: [ ^ fallbackTag ] ]
			