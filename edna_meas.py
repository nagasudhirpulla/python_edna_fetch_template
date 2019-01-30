class EdnaMeas:
    name = "default_name"
    edna_id = "ednaId"
    ext_id = "extId"
    def getDict(self):
        return{
            'name': self.name,
            'edna_id': self.edna_id,
            'ext_id': self.ext_id
        }