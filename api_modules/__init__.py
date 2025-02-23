from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Configuración de la app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Configuración de seguridad para Swagger
authorizations_supper = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Introduce el token JWT en el formato: Bearer <token>"
    },
    'API Key': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY',
        'description': "Proporcione su clave API en el encabezado X-API-KEY"
    }
}

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Introduce el token JWT en el formato: Bearer <token>"
    }
}


# Inicializar la API con autenticación
api = Api(
    app,
    title="User CRUD API",
    description="API para gestionar usuarios con múltiples métodos de autenticación",
    authorizations=authorizations,
    security=[{'Bearer Auth': []}]
)


# Modelo de la base de datos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Esquemas para la documentación y validación
user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='ID del usuario'),
    'username': fields.String(required=True, description='Nombre de usuario'),
    'password': fields.String(required=True, description='Contraseña del usuario')
})

auth_model = api.model('Auth', {
    'username': fields.String(required=True, description='Nombre de usuario'),
    'password': fields.String(required=True, description='Contraseña')
})

# Namespace para usuarios
ns = api.namespace('users', description='Operaciones CRUD de usuarios')

# Endpoints
@ns.route('/')
class UserList(Resource):
    @ns.marshal_with(user_model, as_list=True)
    @jwt_required()
    def get(self):
        """Obtener todos los usuarios (requiere token JWT)"""
        return User.query.all()

    @ns.expect(user_model, validate=True)
    def post(self):
        """Crear un nuevo usuario"""
        data = request.json
        if User.query.filter_by(username=data['username']).first():
            return {'message': 'El usuario ya existe'}, 400
        user = User(username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'Usuario creado exitosamente'}, 201

@ns.route('/<int:id>')
class UserDetail(Resource):
    @ns.marshal_with(user_model)
    @jwt_required()
    def get(self, id):
        """Obtener un usuario por ID (requiere token JWT)"""
        user = User.query.get_or_404(id)
        return user

    @ns.expect(user_model, validate=True)
    @jwt_required()
    def put(self, id):
        """Actualizar un usuario por ID (requiere token JWT)"""
        user = User.query.get_or_404(id)
        data = request.json
        user.username = data['username']
        user.password = data['password']
        db.session.commit()
        return {'message': 'Usuario actualizado exitosamente'}

    @jwt_required()
    def delete(self, id):
        """Eliminar un usuario por ID (requiere token JWT)"""
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'Usuario eliminado exitosamente'}




# Namespace para autenticación
auth_ns = api.namespace(
    'auth',
    description='Operaciones de autenticación',
    authorizations=authorizations_supper,  # Aquí especificas el esquema de autorización adicional
    security=[{'Bearer Auth': []}, {'API Key': []}]  # Puedes añadir ambos tipos de autenticación aquí
)

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(auth_model, validate=True)
    def post(self):
        """Iniciar sesión y obtener un token JWT"""
        data = request.json
        user = User.query.filter_by(username=data['username'], password=data['password']).first()
        if not user:
            return {'message': 'Credenciales inválidas'}, 401
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}




# Inicializar base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
