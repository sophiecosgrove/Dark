from application import db

class Events(db.Model):
    season = db.Column(db.Integer, primary_key=True)
    episode = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(100), primary_key=True)
    from_year = db.Column(db.Integer, nullable=False)
    to_year = db.Column(db.Integer, nullable=False)
    event = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return ''.join([
            'Season/Episode: ', self.season, '/', self.episode, '\r\n',
            'Character: ', self.character, '\r\n',
            'From: ', self.from_year, '\r\n',
            'To: ', self.to_year, '\r\n', 
            'Event: ', self.event, '\r\n'
            ])

