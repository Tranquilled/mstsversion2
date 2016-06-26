from flask_login import LoginManager

# settings for login manager are put here to allow for easier importing in modules
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = "users.login"

login_manager.refresh_view = "users.reauthenticate"
login_manager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)
login_manager.needs_refresh_message_category = "info"
