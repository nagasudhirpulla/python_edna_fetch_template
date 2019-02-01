class EdnaMeas:
    name = "default_name"
    edna_id = "ednaId"
    ext_id = "extId"

    def getDict(self):
        return{
            "name": self.name,
            "edna_id": self.edna_id,
            "ext_id": self.ext_id
        }

    def fromDict(self, dictObj):
        configObj = EdnaMeas()
        keys = [str(keyStr) for keyStr in dictObj.keys()]
        if "name" in keys:
            configObj.name = dictObj['name']
        if "edna_id" in keys:
            configObj.edna_id = dictObj['edna_id']
        if "extId" in keys:
            configObj.extId = dictObj['extId']
        return configObj
