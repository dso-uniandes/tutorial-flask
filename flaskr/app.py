from flaskr import create_app
from .modelos import db, Cancion, Album
from .modelos import AlbumSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()  

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id_cancion>')

# Prueba
with app.app_context():
    album_schema = AlbumSchema()
    A = Album(titulo="Album Test", anio=2023, descripcion="Test Album", medio="CD")
    db.session.add(A)
    db.session.commit()
    print([album_schema.dumps(album) for album in Album.query.all()])   