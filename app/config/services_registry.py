from flask_injector import request
from injector import singleton, Binder

from app.adapters.out.database.sqlalchemy_repositories.sqlalchemy_user_reposiroty import UserRepository
from app.application.user_login_usecase import UserLoginUseCase
from app.domain.interfaces.user_interface import IUserRepository
from app.domain.services.authenticate_service import AuthenticateService
from app.domain.services.user_service import UserService


def register_dependencies(binder: Binder):
    """
    Register all dependencies here.
    """

    # Repositories
    binder.bind(IUserRepository, to=UserRepository, scope= request)

    #Services
    binder.bind(UserService, to=UserService, scope= singleton)
    binder.bind(AuthenticateService, to=AuthenticateService, scope= singleton)


    #User Cases
    binder.bind(UserLoginUseCase, to=UserLoginUseCase, scope= singleton)