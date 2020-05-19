from application import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    episode = db.Column(db.Integer, nullable=False)
    character = db.Column(db.String(100), nullable=False )
    from_year = db.Column(db.Integer, nullable=False)
    to_year = db.Column(db.Integer, nullable=False)
    event = db.Column(db.String(100), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))


    def __repr__(self):
        return ''.join([
            'EventID: ', str(self.id), '\r\n',
            'Season/Episode: ', self.season, '/', self.episode, '\r\n',
            'Character: ', self.character, '\r\n',
            'CharacterID: ', self.character_id, '\r\n',
            'From: ', self.from_year, '\r\n',
            'To: ', self.to_year, '\r\n', 
            'Event: ', self.event, '\r\n'
            ])

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mother = db.Column(db.String(100), nullable=True)
    father = db.Column(db.String(100), nullable=True)
    hair_colour = db.Column(db.String(30), nullable=False)
    eye_colour = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'CharacterID: ', str(self.id), '\r\n',
            'Name: ', self.name, '\r\n',
            'Mother: ', self.mother, '\r\n',
            'Father: ', self.father, '\r\n',
            'Hair Colour: ', self.hair_colour, '\r\n',
            'Eye Colour: ', self.eye_colour, '\r\n',
            'Status: ', self.status, '\r\n'
            ])
