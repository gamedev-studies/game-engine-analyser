getOutgoing

	"Returns a list of all tags this tag depends on according to the arch map. This version works when only files are tagged, not folders"

	| taggedFolders tagsOutgoing tagFound |
	taggedFolders := (self taggedEntities flatCollect: [ :each | 
		                  each queryAllOutgoing opposites ]) asSet asArray.

	tagsOutgoing := taggedFolders flatCollect: [ :each | each tags ].
	tagsOutgoing := tagsOutgoing asSet.
	tagsOutgoing := tagsOutgoing collect: [ :each | each name ].

	^ tagsOutgoing