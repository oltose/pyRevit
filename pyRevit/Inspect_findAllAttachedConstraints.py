from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

cl = FilteredElementCollector(doc)
clconst = cl.OfCategory( BuiltInCategory.OST_Constraints ).WhereElementIsNotElementType()

constlst = set()

def listConsts( el, clconst ):
	print('THIS OBJECT ID: {0}'.format(el.Id))
	for cnst in clconst:
		refs = [(x.ElementId, x) for x in cnst.References]
		elids = [x[0] for x in refs]
		if el.Id in elids:
			constlst.add( cnst )
			print("CONST TYPE: {0} # OF REFs: {1} CONST ID: {2}".format(cnst.GetType().Name.ljust(28), str(cnst.References.Size).ljust(24), cnst.Id))
			for t in refs:
				ref = t[1]
				elid = t[0]
				if elid == el.Id:
					elid = str(elid) + ' (this)'
				print("     {0} LINKED OBJ CATEGORY: {1} ID: {2}".format(	ref.ElementReferenceType.ToString().ljust(35),
																			doc.GetElement( ref.ElementId ).Category.Name.ljust(20),
																			elid ))
			print('\n')
	print('\n')

for elId in uidoc.Selection.GetElementIds():
	el = doc.GetElement( elId )
	listConsts(el, clconst)